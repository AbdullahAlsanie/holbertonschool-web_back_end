# NodeJS Basics

This project contains basic Node.js exercises covering fundamental concepts like:
- Running JavaScript using NodeJS
- Using NodeJS modules
- Reading files with specific Node JS modules
- Accessing command line arguments and environment with process
- Creating HTTP servers using Node JS and Express JS
- Creating advanced routes with Express JS
- Using ES6 with Node JS through Babel-node
- Using Nodemon for faster development

## Requirements

- Ubuntu 20.04 LTS
- Node.js (version 20.x.x)
- Jest for testing
- ESLint for linting

## Setup

Install dependencies:
```bash
npm install
```

## Tasks

### 0. Executing basic javascript with Node JS
File: `0-console.js` - Function that prints a string argument to STDOUT

### 1. Using Process stdin
File: `1-stdin.js` - Program that reads from stdin and displays user input

### 2. Reading a file synchronously with Node JS
File: `2-read_file.js` - Function that reads a CSV file synchronously

### 3. Reading a file asynchronously with Node JS
File: `3-read_file_async.js` - Function that reads a CSV file asynchronously

### 4. Create a small HTTP server using Node's HTTP module
File: `4-http.js` - Basic HTTP server on port 1245

### 5. Create a more complex HTTP server using Node's HTTP module
File: `5-http.js` - HTTP server with routing

### 6. Create a small HTTP server using Express
File: `6-http_express.js` - Basic Express server on port 1245

### 7. Create a more complex HTTP server using Express
File: `7-http_express.js` - Express server with routing

### 8. Organize a complex HTTP server using Express
Directory: `full_server/` - Organized Express server with controllers and routes

## Testing

Run tests:
```bash
npm test
```

Run linting:
```bash
npm run check-lint
```

Run full test (lint + tests):
```bash
npm run full-test
```

## Author

Holberton School Student
