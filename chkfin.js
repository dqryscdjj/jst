var mysql = require('mysql');

var usdcny;

var currconfig = require("./config");
var btcnum = currconfig.btcnum;
var ltcnum = currconfig.ltcnum;
var ethnum = currconfig.ethnum;
var ethonpolo = currconfig.ethonpolonum;
var btconpolo = currconfig.btconpolonum;
var usdcnyrate = currconfig.usdcnyratenum;
//console.log(nbtcnum, nltcnum, nethnum, nethonpolo, nbtconpolo, nusdcnyrate);

var exec = require('child_process').exec;
var arg1 = '-i'
var arg2 = 'USDCNY'
exec('python getchg.py ' + arg1 + ' ' + arg2 + ' ', function(error, stdout, stderr) {
  if (stdout.length > 1) {
    usdcny = stdout;
  } else {
    usdcny = stdout
  }
  if (error) {
    usdcny = usdcnyrate
  }
});

var request = require('request');
request('https://poloniex.com/public?command=returnTicker', function(error, response, body) {
  console.log('error:', error); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  //console.log('body:', body); // Print the HTML for the Google homepage.
  poloticker = JSON.parse(body);

  btcusd = poloticker.USDT_BTC.last * btcnum;
  ethusd = poloticker.USDT_ETH.last * ethnum;
  ltcusd = poloticker.USDT_LTC.last * ltcnum;
  polousd = poloticker.USDT_BTC.last * btconpolo + poloticker.USDT_ETH.last * ethonpolo + ltcusd;
  console.log('usdcny rate :', usdcny);
  btccny = btcusd * usdcny;
  ethcny = ethusd * usdcny;
  ltccny = ltcusd * usdcny;
  polocny = polousd * usdcny;
  console.log('price btc ', poloticker.USDT_BTC.last, ' eth ', poloticker.USDT_ETH.last, ' ltc ', poloticker.USDT_LTC.last);
  console.log("usd btc ", btcusd, " etc ", ethusd, " polo ", polousd, " sumvalue ", btcusd + ethusd + polousd);
  console.log("cny btc ", btccny, " etc ", ethcny, " polo ", polocny, " sumvalue ", btccny + ethcny + polocny);

  insbtc = 'insert into etradehist(market,value) values(\'btcrmb\',' + btccny + ')';
  inseth = 'insert into etradehist(market,value) values(\'dao2ethrmb\',' + ethcny + ')';
  inspolo = 'insert into etradehist(market,value) values(\'prmb\',' + polocny + ')';


  var connection = mysql.createConnection({
    host: 'localhost',
    user: 'udfin',
    password: 'udfin',
    database: 'bcmsa'
  });

  connection.connect(function(err) {
    if (err) {
      console.error('error connecting: ' + err.stack);
      return;
    }
    console.log('connected as id ' + connection.threadId);
  });

  /*  connection.query('select * from own;', function(err, rows, fields) {
      if (err) throw err;

      console.log('The old own is: ', rows[0].ownvalue);
    });*/
  //console.log(insbtc);
  var updatebtc = '/usr/bin/python /home/dev/chkfin/updb.py -i \"' + insbtc + '\"';
  exec(updatebtc, function(error, stdout, stderr) {
    //console.log("stdout len :", stdout.length, "insbtc len :", insbtc.length);
    if (stdout.length > 1) {
      console.log('update btc error ', stdout);
    } else {
      console.log('update btc ok');
    }
    if (error) {
      console.log('update btc error ', error);
    }
  });
  //console.log(inseth);
  exec('/usr/bin/python /home/dev/chkfin/updb.py -i \"' + inseth + '\"', function(error, stdout, stderr) {
    if (stdout.length > 1) {
      console.log('update eth error', stdout);
    } else {
      console.log('update eth ok');
    }
    if (error) {
      console.log('update btc error ', error);
    }
  });
  //console.log(inspolo);
  exec('/usr/bin/python /home/dev/chkfin/updb.py -i \"' + inspolo + '\"', function(error, stdout, stderr) {
    if (stdout.length > 1) {
      console.log('update polo error ', stdout);
    } else {
      console.log('update polo ok');
    }
    if (error) {
      console.log('update polo error ', error);
    }
  });

  connection.query('select * from own;', function(err, rows1, fields1) {
    if (err) throw err;

    console.log('The new own is: ', rows1[0].ownvalue);
    udpownvalue = 'insert into ownvaluelist(ownvalue) values(\"' + rows1[0].ownvalue + '\")';
    //console.log(udpownvalue);
    exec('/usr/bin/python /home/dev/chkfin/updb.py -i \"' + udpownvalue + '\"', function(error, stdout, stderr) {
      if (stdout.length > 1) {
        console.log('update ownvalue error ', stdout);
      } else {
        console.log('update ownvalue ok', stdout);
      }
      if (error) {
        console.log('update ownvalue error ', error);
      }
    });
  });

  connection.end();
});
