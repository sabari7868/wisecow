const http = require("http");
const { execSync } = require("child_process");

const port = 4499;

const requestHandler = (req, res) => {
  let output;
  try {
    // Use full paths for fortune and cowsay
    output = "hi, hello...!" //execSync("/usr/games/fortune | /usr/games/cowsay").toString();
  } catch (err) {
    output = "Error generating wisdom!\n" + err.message;
  }
  res.writeHead(200, { "Content-Type": "text/html" });
  res.end(`<pre>${output}</pre>`);
};

const server = http.createServer(requestHandler);

server.listen(port, "0.0.0.0", () => {
  console.log(`Wisdom server running on port ${port}`);
});

