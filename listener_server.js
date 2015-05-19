// node listener server
/*
* This is the node.js listener server. It writteh wtih NOde.js, witch is a form of javascript.
* Node is a non-blocking language, it is perfect for real time projects. Peter had 
* mentioned 

*/
(function(){
var WebSocketServer = require('ws').Server;
var wss = new WebSocketServer({ port: 8080 });
var http = require('http');
var data = undefined; 

var sql  = require('mssql');

var config = {
    user: 'sd_admin',
    password: 'aaaaaaaa',
    server: 'csc687-instance.civ7qi4ah44w.us-west-1.rds.amazonaws.com',
    database: 'test_db',
    port: '1433',
    
    options: {
        encrypt: false // Use this if you're on Windows Azure 
    }
};

 console.log('created server');
///////////////////////////////////////////////
var body = 'Node Listener for datatrip application. Please visit our main site: <a href="http://plotdatatrip.com/">plotdatatrip.com</a>' 
var server = http.createServer(function(request, response) {
    console.log((new Date()) + ' Received request for ' + request.url);
    response.writeHead(200,{
        'Content-Length': body.length,
        'Content-Type': 'text/html',
    });
    response.end(body);
});
server.listen(8080, function() {
    console.log((new Date()) + ' Server is listening on port 8080');
});

///////////////////////////////////////////
 
 
wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
    
    data = JSON.parse(message);
    console.log(data);
    // check data for runnable...
    /////////////////////////
   var connection = new sql.Connection(config, function(err) {
       
        // ... error checks 
        if(err){
        console.log(err);
        }
        
        
        
        
        // input 
        console.log('starting transaction');
        var transaction = new sql.Transaction(connection);
        transaction.begin(function(err) {
            // ... error checks 
            if(err){
            console.log(err);
            }
         
            console.log('creating request');
            var request = new sql.Request(transaction);
            // INSERT INTO tReading (iTypeKey, iUnitKey, datDateTime, dValue) VALUES (20, 15, '04/22/2015 3:55 am', 115)
            var str_input = ('insert into DogsData.dbo.tReading (iTypeKey, iUnitKey, datDateTime, dValue) values (' + data['iTypeKey'] + ', ' + 
                data['iUnitKey'] +', \'' + data['datDateTime'] +'\', ' + data['dValue'] +')');
            console.log(str_input)
            request.query(str_input, function(err, recordset) {
                // ... error checks 
                if(err){
                        console.log(err);
                       }
                console.log('commiting transaction');
                transaction.commit(function(err, recordset) {
                    // ... error checks 
                        if(err){
                        console.log(err);
                        ws.send('Transaction failed')
                       }
                    console.log(recordset);
                    console.log("Transaction commited.");
                    ws.send('transaction Success')
                });
            });
        });
   }); 
   /////////////////////////
   if(data["Runnable"]){
       //querry database
       ws.send({"runnable": true})
   }
  });
 
  ws.send('updated DB...');
});

}());