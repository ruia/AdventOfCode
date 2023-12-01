const fs = require('fs');
const isTest = process.env.npm_config_test || false;

console.log('Problem: 01');
console.log('Is Test: ', isTest);

try {
    let digits = [];
    let sum = 0;
    let lines = [];

    lines = fs.readFileSync(__dirname + '/input' + (isTest ? '_test_part1' : ''), 'utf8').split('\n');
    lines.forEach(line => {
        let tmpDigits = [];
        [...line].forEach(char => {
            if (!isNaN(parseInt(char))) {
                tmpDigits.push(parseInt(char));
            }
        });
        digits.push(tmpDigits);
    });

    digits.forEach(line => {
        sum += parseInt((line[0] + line.slice(-1)));
    });
    console.log('TOTAL PART 1: ', sum);

    // PART 2

    let numbers = new Object();
    numbers['1'] = 1;
    numbers['2'] = 2;
    numbers['3'] = 3;
    numbers['4'] = 4;
    numbers['5'] = 5;
    numbers['6'] = 6;
    numbers['7'] = 7;
    numbers['8'] = 8;
    numbers['9'] = 9;
    numbers['one'] = 1;
    numbers['two'] = 2;
    numbers['three'] = 3;
    numbers['four'] = 4;
    numbers['five'] = 5;
    numbers['six'] = 6;
    numbers['seven'] = 7;
    numbers['eight'] = 8;
    numbers['nine'] = 9;

    digits = [];
    sum = 0;

    lines = fs.readFileSync(__dirname + '/input' + (isTest ? '_test_part2' : ''), 'utf8').split('\n');
    lines.forEach(line => {
        let lastPos = 0;
        let tmpDigits = [];

        for (let key in numbers) {
            let pos = line.indexOf(key);
            while (pos > -1) {
                tmpDigits.push({ num: numbers[key], pos: pos });
                pos = line.indexOf(key, pos + 1);
            }
        }
        tmpDigits = tmpDigits.sort(function (a, b) {
            return a.pos - b.pos;
        });
        digits.push(tmpDigits);

    });

    digits.forEach(line => {
        sum += parseInt('' + line[0].num + line.slice(-1)[0].num);
    });

    console.log('TOTAL PART 2: ', sum);
} catch (err) {
    console.error(err);
}