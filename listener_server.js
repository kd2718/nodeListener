// node listener server
(function(){
var WebSocketServer = require('ws').Server;
var wss = new WebSocketServer({ port: 8080 });
var http = require('http');
var data = undefined; 

var sql  = require('mssql'); 

 console.log('created server');

 
wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
    console.log(message);
    data = JSON.parse(message);
    if(data["myNum"]) {
    console.log("number received: " + data["myNum"])
    }
    
    if(data["CRAZY"]){
    console.log("crazy stuff");
    } else {
    console.log("crazy not sent");
    }
    console.log(data["myNum"]);
  });
 
  ws.send('something');
});

}());