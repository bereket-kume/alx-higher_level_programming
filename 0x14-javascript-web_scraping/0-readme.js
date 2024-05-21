#!usr/bin/node

const fs = require('fs')

const args = process.argv;
const filePath = args[2]


fs.readFile(filePath, 'utf-8', (err, data) => {
    if (err){
        console.log(err)
    } else {
        process.stdout.write(data)
    }
});