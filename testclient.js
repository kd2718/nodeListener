var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

console.log('my test');

ws.on('open', function open() {
  console.log('connected')
  ws.send('something');
});

ws.on('message', function(data, flags) {
  // flags.binary will be set if a binary data is received.
  // flags.masked will be set if the data was masked.
  console.log(data);
});