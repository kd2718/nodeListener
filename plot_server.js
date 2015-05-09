// node listener server
/*
* This is the node.js listener server. It writteh wtih NOde.js, witch is a form of javascript.
* Node is a non-blocking language, it is perfect for real time projects. Peter had 
* mentioned 

*/
(function(){
//var WebSocketServer = require('ws').Server;
//var wss = new WebSocketServer({ port: 8080 });
var http = require('http');
var data = undefined; 

var sql  = require('mssql');

// Learn about API authentication here: https://plot.ly/nodejs/getting-started
// Find your api_key here: https://plot.ly/settings/api

var plotly = require('plotly')('kd2718','qlrq59nuu4');
var trace1 = {
  x: [1, 2, 3, 4], 
  y: [10, 15, 13, 17], 
  type: "scatter"
};
var trace2 = {
  x: [1, 2, 3, 4], 
  y: [16, 5, 11, 9], 
  type: "scatter"
};
var data = [trace1, trace2];
var graphOptions = {filename: "basic-line", fileopt: "overwrite"};
plotly.plot(data, graphOptions, function (err, msg) {
    console.log(msg);
});

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
            // INSERT INTO tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) VALUES (20, 15, '04/22/2015 3:55 am', 115)
            var str_input = ('insert into DogsData.dbo.tReading (iTypeNumber, iUnitNumber, datDateTime, dValue) values (' + data['iTypeNumber'] + ', ' + 
                data['iUnitNumber'] +', \'' + data['datDateTime'] +'\', ' + data['dValue'] +')');
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