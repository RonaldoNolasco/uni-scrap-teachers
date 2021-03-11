const fs = require('fs');

let json = require('./profe.json');
console.log(json, 'the json obj');

for (let i =0;i< json.length;i++){
    json[i].imageUrl = "https://www.orce.uni.edu.pe/profesores/" + json[i].dni + ".jpg"
}

// convert JSON object to string
const data = JSON.stringify(json);

// write JSON string to a file
fs.writeFile('profe2.json', data, (err) => {
    if (err) {
        throw err;
    }
    console.log("JSON data is saved.");
});