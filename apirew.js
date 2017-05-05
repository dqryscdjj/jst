// include dependencies
var express = require('express');
var proxy = require('http-proxy-middleware');

// proxy middleware options
var options = {
  //        target: 'http://172.31.22.2:8181', // target host
  target: 'http://127.0.0.1:8181', // target host
  changeOrigin: true, // needed for virtual hosted sites
  ws: true, // proxy websockets
  pathRewrite: {
    '^/api': '/onos/v1' // rewrite path
  },
  //        router: {
  // when request.headers.host == 'dev.localhost:3000',
  // override target 'http://www.example.org' to 'http://localhost:8000'
  //            'dev.localhost:3000' : 'http://localhost:8000'
  //        }
};

// create the proxy (without context)
var exampleProxy = proxy(options);

// mount `exampleProxy` in web server
var app = express();
app.use('/api', exampleProxy);
app.listen(3000);
