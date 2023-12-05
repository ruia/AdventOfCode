const { constants } = require('buffer');
const fs = require('fs');
const isTest = process.env.npm_config_test || false;

console.log('Problem: 03');
console.log('Is Test: ', isTest);

try {
    let total = 0;
    const lines = fs.readFileSync(__dirname + '/input' + (isTest ? '_test_part1' : ''), 'utf8').split('\n');
    let numbers = [];


    lines.forEach(line => {
        line.split('').forEach((char, index) => {
            console.log(index, char);
        });
    });



    console.log('TOTAL:', total);
    // PART 2


} catch (err) {
    console.error(err);
}

function isNumber(value) {
    return typeof value === 'number';
  }