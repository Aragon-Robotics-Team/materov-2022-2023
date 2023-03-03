var http = require('http'); //create the server with module
 http.createServer(function (req, res) { 
   res.writeHead(200, {'Content-Type': 'text/html'}); //(200 = ok status) sets the http status code of the response, which indicates how well an http request was handled by the server
   res.end('Hello World!'); //writes the http response back --> returns data the server has to return
 }).listen(8080); //binds the server to a network address

 //to run only this file, type http://localhost:8080/ into webserver to run webserver but not the html file 

