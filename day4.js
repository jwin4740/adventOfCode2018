const moment = require("moment");
const fs = require("fs")

console.log("he");

let dat;
fs.readFileSync("values4.txt", 'utf8', function (err, data) {
    if (err) throw err;


    dat = data

});

console.log(dat);