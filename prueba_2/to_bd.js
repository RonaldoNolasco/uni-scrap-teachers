const fs = require('fs');

let json = require('./profe2.json');

console.log(json.length);

/*
for (let i=0 ; i<json.length ; i++){
    string = "insert into file (mime, public_url, created_at, updated_at) values ('image/jpeg', '" + String(json[i]['imageUrl']) + "', NOW(), NOW());"
    console.log(string);
}
*/

for (let i =0;i< json.length;i++){
    string = "update person set picture = " + String(i+3) + " where id = " + String(i+3) + ";"
    console.log(string);
}
