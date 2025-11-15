import readDatabase from '../utils';

/**
 * Students Controller
 */
class StudentsController {
  /**
   * Returns all students grouped by field
   * @param {Object} req - Express request object
   * @param {Object} res - Express response object
   */
  static getAllStudents(req, res) {
    const databasePath = process.argv[2];

    readDatabase(databasePath)
      .then((fields) => {
        let output = 'This is the list of our students\n';
        const sortedFields = Object.keys(fields).sort((a, b) => (
          a.toLowerCase().localeCompare(b.toLowerCase())
        ));

        sortedFields.forEach((field, index) => {
          output += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`;
          if (index < sortedFields.length - 1) {
            output += '\n';
          }
        });

        res.status(200).send(output);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  /**
   * Returns students filtered by major
   * @param {Object} req - Express request object
   * @param {Object} res - Express response object
   */
  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const databasePath = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(databasePath)
      .then((fields) => {
        const students = fields[major] || [];
        res.status(200).send(`List: ${students.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
