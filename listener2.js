var WebSocketServer = require('ws').Server;
var http = require('http');

var server = http.createServer(function(request, response) {
    // process HTTP request. Since we're writing just WebSockets server
    // we don't have to implement anything.
});
server.listen(8080, function() { });

// create the server

var wsServer = new WebSocketServer({
    server: server
});


//var wsServer = new WebSocketServer({ port: 8080 });

// WebSocket server
wsServer.on('request', function(request) {
    var connection = request.accept(null, request.origin);

    // This is the most important callback for us, we'll handle
    // all messages from users here.
    connection.on('message', function(message) {
        if (message.type === 'utf8') {
            // process WebSocket message
            console.log(message);
        }
    });

    connection.on('close', function(connection) {
        // close user connection
    });
});