// take a bullet for this city

var RLDB = true; // print lots of shit
var usecached = true; // use local file... don't re-download

debugprint("hi there"); // friendly

// node shit
var http = require('http');
var fs = require('fs');

// URL shit
var APIep = "http://data.nola.gov/resource/jsyu-nz5r.json"; // endpoint for NOLA open data
var APIquery = "?typetext=DISCHARGING%20FIREARM&$order=timecreate%20DESC"; // query we want
var queryURL = APIep + APIquery; // the whole enchilada

// local file shit
var destFile = "foo.json"; // where are we stashing this locally?

// data shit
var thestuff; // holder for JSON
var gunQueue = new Array(); // gun queue
var backdate = 7; // use week old data


//
// FUNCTION BLOCK:
//

// download the SODA stuff asynchronously and fire off a callback
var downloadJSON = function(url, dest, cb) {
  	var file = fs.createWriteStream(dest);
  	debugprint("about to download...");
  	var request = http.get(url, function(response) {
    response.pipe(file);
    file.on('finish', function() {
      file.close(cb(dest));  // close() is async, call cb after close completes.
    });
  });
}

// callback out of downloadJSON... loads and parses the file and continues
function gotFile(destFile)
{
	debugprint("parsing file...");	
	thestuff = (JSON.parse(fs.readFileSync(destFile, "utf8")));
	//debugprint(thestuff);

	// parse JSON into queue
	debugprint("generating queue...");
	gunQueue = JSONtoQueue(thestuff, backdate);
	// dump Queue to screen
	debugprint("dumping queue...");
	dumpQueue(gunQueue);
}

// parses JSON and returns Array object of Date elements
// Date elements are to be queued based on old data set by 'backdate'
function JSONtoQueue(stuff, bd)
{
	// new array
	q = new Array();

	// date shit
	var threedays = bd*24*60*60*1000; // milliseconds
	var today = new Date();
	var tda = new Date(today.getTime() - threedays); // three days ago
	debugprint("Today is: " + tda);

	for(var i=0;i<stuff.length;i++){
        var d = new Date(Date.parse(stuff[i].timecreate));

        // date matches three days ago... add to queue
        if(d.getDate()==tda.getDate()
         && d.getFullYear()==tda.getFullYear()
          && d.getMonth()==tda.getMonth()) {
          	// strip duplicates
          	if(stuff[i].disposition!="DUP")
          	{
	          	q.push(d);
          	}
        }
     }
     q.reverse();
     return(q);
}

// print out queue
function dumpQueue(q)
{
	for(var i = 0;i<q.length;i++)
	{
		debugprint("schedule gun at: " +q[i]);
	}
}


function debugprint(stuff)
{
	if(RLDB) console.log(stuff);
}

// MASTER BLOCK
if(usecached)
{
	gotFile(destFile);
}
else {
	downloadJSON(queryURL, destFile, gotFile);
}


