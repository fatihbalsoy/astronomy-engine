var Astronomy = require('../source/js/astronomy.js');
const observer = Astronomy.MakeObserver(29, -81, 10);
var body = 'Mercury';
var time = Astronomy.MakeTime(-109572.5);
var pos = Astronomy.GeoVector(body, time);
var sky = Astronomy.SkyPos(pos, observer);
console.log(`J2000  RA  = ${sky.j2000.ra.toFixed(16)}`);
console.log(`J2000  DEC = ${sky.j2000.dec.toFixed(16)}`);
console.log(`ofdate RA  = ${sky.ofdate.ra.toFixed(16)}`);
console.log(`ofdate DEC = ${sky.ofdate.dec.toFixed(16)}`);