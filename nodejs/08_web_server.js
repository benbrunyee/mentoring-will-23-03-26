// =============================================================================
// WEB SERVER
// Concepts: express, routing, middleware, how HTTP works,
//           serving HTML, request/response cycle
// =============================================================================
//
// Run this script with:  node 08_web_server.js
// Then open http://localhost:8080 in your browser.
// Press Ctrl+C in the terminal to stop the server.
//
// =============================================================================

const express = require("express");

const PORT = 8080;

// ---------------------------------------------------------------------------
// The HTML pages we'll serve — stored as JS template literals.
// In a real web app you'd keep these in separate .html files.
// ---------------------------------------------------------------------------

const HOME_PAGE = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Node.js Web Server</title>
    <style>
        body  { font-family: Arial, sans-serif; max-width: 700px; margin: 60px auto; padding: 0 20px; background: #f5f5f5; }
        h1    { color: #2c3e50; }
        p     { color: #555; line-height: 1.6; }
        .card { background: white; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
        code  { background: #eee; padding: 2px 6px; border-radius: 3px; font-size: 0.9em; }
        a     { color: #3498db; }
    </style>
</head>
<body>
    <h1>Hello from Node.js!</h1>

    <div class="card">
        <p>This page is being served by a Node.js script using the
        <code>express</code> library.</p>
        <p>Every time you reload this page, your browser sends an <strong>HTTP GET
        request</strong> to Node.js, which responds with this HTML.</p>
    </div>

    <div class="card">
        <h2>Try these URLs</h2>
        <ul>
            <li><a href="/">/</a> &mdash; This page (HTML)</li>
            <li><a href="/time">/time</a> &mdash; Current server time (JSON)</li>
            <li><a href="/about">/about</a> &mdash; About page</li>
        </ul>
    </div>
</body>
</html>`;

const ABOUT_PAGE = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About - Node.js Web Server</title>
    <style>
        body  { font-family: Arial, sans-serif; max-width: 700px; margin: 60px auto; padding: 0 20px; background: #f5f5f5; }
        h1    { color: #2c3e50; }
        .card { background: white; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
        a     { color: #3498db; }
    </style>
</head>
<body>
    <h1>About</h1>
    <div class="card">
        <p>This is a simple web server written in Node.js for learning purposes.</p>
        <p>It demonstrates how HTTP works: your browser sends a <strong>request</strong>,
        the server processes it and sends back a <strong>response</strong>.</p>
        <p><a href="/">Back to home</a></p>
    </div>
</body>
</html>`;

// ---------------------------------------------------------------------------
// Set up Express and define routes — each route decides what to send back
// for a given URL path. This is Express's equivalent of the Python
// RequestHandler class.
// ---------------------------------------------------------------------------

const app = express();

app.get("/", (req, res) => {
  res.send(HOME_PAGE);
});

app.get("/about", (req, res) => {
  res.send(ABOUT_PAGE);
});

app.get("/time", (req, res) => {
  const now = new Date();

  const time = now.toLocaleTimeString("en-GB", { hour12: false });
  const date = now.toLocaleDateString("en-GB", {
    weekday: "long",
    day: "2-digit",
    month: "long",
    year: "numeric",
  });

  res.json({ time, date });
});

// Express calls this handler for any route that wasn't matched above.
app.use((req, res) => {
  res.status(404).send("<h1>404 - Page Not Found</h1>");
});

// ---------------------------------------------------------------------------
// Start the server
// ---------------------------------------------------------------------------

app.listen(PORT, () => {
  console.log("=== Node.js Web Server ===\n");
  console.log(`Starting server on port ${PORT}...`);
  console.log(`Open your browser and go to:  http://localhost:${PORT}`);
  console.log("Press Ctrl+C to stop.\n");
});
