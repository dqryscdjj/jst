var http = require('http');
var fs = require('fs');

http.createServer(function (req, res) {

    res.writeHead(200, {'Content-Type': 'text/plain'});
    fs.readFile('/home/dev/chkfin/nowvalue', function(err, data){
        res.write(data);
        res.end('End for Love\n');
    });

}).listen(1337, '0.0.0.0');

console.log('Server running at 1337 port');
