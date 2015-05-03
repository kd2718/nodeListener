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
}

 console.log('created server');
///////////////////////////////////////////////

///////////////////////////////////////////
 
 
wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    console.log('received: %s', message);
    
    data = JSON.parse(message);
    console.log(data);
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
    // INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '04/22/2015 3:55 am', 115)
    var str_input = ('insert into DogsData.dbo.tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) values (' + data['iTypeNumber'] + ', ' + data['iUnitNumber'] +', \'' + data['datDateTime'] +'\', ' + data['dValue'] +')');
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
               }
            console.log(recordset);
            console.log("Transaction committed.");
        });
    });
});
    

   }); 
    /////////////////////////
    
    if(data["myNum"]) {
    console.log("number received: " + data["myNum"])
    }
    
    if(data["CRAZY"]){
    console.log("crazy stuff");
    } else {
    console.log("crazy not sent");
    }
    //console.log(data["myNum"]);
  });
 
  ws.send('updated DB...');
});

}());