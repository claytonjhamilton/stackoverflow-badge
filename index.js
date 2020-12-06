// Load & cache Javascript modules
const http = require('http');
const url = require('url');
const fetch = require('node-fetch');
const StackOverflowBadge = require('./src/StackOverflowBadge');

// Reach out to stackexchange api and generate badge
http.createServer(async (req, res) => {
  const reqURL = url.parse(req.url, true);
  const { userID } = reqURL.query;

  if (!userID) {
    res.write(JSON.stringify({error: 'Add your StackOverflow userID to the url string. Check the stackoverflow-badge README for an example.'}));
    res.end();
    return;
  }

  const responseArticles = await fetch(`https://api.stackexchange.com/2.2/users/${userID}?site=stackoverflow&filter=!--1nZv)deGu1`);
  const json = await responseArticles.json();

  if (!json.items || json.items.length === 0) {
    res.write(JSON.stringify({error: 'Your userID is incorrect'}));
    res.end();
    return;
  }

  const result = await StackOverflowBadge(json.items[0]);

  res.setHeader('Cache-Control', 'private, no-cache, no-store, must-revalidate');
  res.setHeader('Expires', '-1');
  res.setHeader('Pragma', 'no-cache');
  res.writeHead(200, { 'Content-Type': 'image/svg+xml' });

  res.write(result);
  res.end();

}).listen(process.env.PORT || 3000, function(){
 console.log("server start at port 3000");
});