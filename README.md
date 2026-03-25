# Beginner Scripts

A collection of beginner-friendly scripts for GCSE Computer Science students, written in Python and JavaScript (Node.js).
Each script focuses on a core concept and is heavily commented to explain what's happening and why.

## Folder Structure

```
├── python/
│   ├── requirements.txt
│   └── scripts/
│       └── *.py
└── nodejs/
    ├── package.json
    └── 08_web_server.js
```

## Setup

### Python

Make sure you have Python 3 installed:

```bash
python3 --version
```

Install the one external dependency (only needed for the API script):

```bash
pip install -r python/requirements.txt
```

### Node.js

Make sure you have Node.js installed:

```bash
node --version
```

Install dependencies:

```bash
cd nodejs && npm install
```

## Scripts

### Python (`python/scripts/`)

| File | Topic | Concepts Covered |
|------|-------|-----------------|
| `01_number_guesser.py` | Game | `random`, `while` loops, `if/elif/else`, input validation |
| `02_quiz_game.py` | Quiz | Lists, dictionaries, `for` loops, functions, score tracking |
| `03_password_generator.py` | Strings | `string` module, `random`, list comprehensions, `join` |
| `04_file_creator.py` | File I/O | `os`, `random`, writing files with `open()` |
| `05_file_searcher.py` | File I/O | Reading files, string searching, looping over directories |
| `06_todo_app.py` | Terminal App | CRUD operations, `json` persistence, menus, functions |
| `07_api_requests.py` | Networking | HTTP requests, JSON parsing, `requests` library |
| `08_web_server.py` | Web | Built-in `http.server`, how HTTP works |
| `09_gui_calculator.py` | GUI | `tkinter`, event-driven programming, widgets |

### Node.js (`nodejs/`)

| File | Topic | Concepts Covered |
|------|-------|-----------------|
| `08_web_server.js` | Web | `express`, routing, middleware, request/response cycle |

## Running a Script

### Python

From the `python/scripts/` folder:

```bash
python3 01_number_guesser.py
```

### Node.js

From the `nodejs/` folder:

```bash
node 08_web_server.js
```

Or using npm:

```bash
npm start
```

## Notes

- Python scripts `04` and `05` work together — run `04` first to create the files, then `05` to search them.
- Both `08_web_server.py` and `08_web_server.js` start a web server on `http://localhost:8080`. Press `Ctrl+C` to stop.
- Python script `09` opens a window — make sure you're not running it over SSH without a display.
