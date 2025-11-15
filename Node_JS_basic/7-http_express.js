const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

/**
 * Counts students in a CSV data file asynchronously
 * @param {string} path - The path to the CSV file
 * @returns {Promise<string>} - Promise that resolves with the student count info
 */
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');

      if (lines.length <= 1) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const students = lines.slice(1);
      let output = `Number of students: ${students.length}\n`;

      const fields = {};
      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');
        if (field) {
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        }
      });

      const fieldNames = Object.keys(fields);
      fieldNames.forEach((field, index) => {
        output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
        if (index < fieldNames.length - 1) {
          output += '\n';
        }
      });

      resolve(output);
    });
  });
}

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];
  countStudents(databasePath)
    .then((output) => {
      res.send(`This is the list of our students\n${output}`);
    })
    .catch((error) => {
      res.send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

module.exports = app;
