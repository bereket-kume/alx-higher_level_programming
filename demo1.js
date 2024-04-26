var http = require('http');
http.createServer(function(req,res){
    res.write("hello node js");
    res.end()
}).listen(8080);