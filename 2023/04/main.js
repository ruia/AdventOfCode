const { constants } = require('buffer');
const fs = require('fs');
const isTest = process.env.npm_config_test || false;

console.log('Problem: 04');
console.log('Is Test: ', isTest);

try {
    let total = 0;
    const lines = fs.readFileSync(__dirname + '/input' + (isTest ? '_test_part1' : ''), 'utf8').split('\n');
    lines.forEach(line => {
        let tmpTotal = 0;
        let tmp = line.split(': ')[1].split(' | ');
        let winingNumbers = tmp[0].split(' ').filter(number => number != '');
        let numbers = tmp[1].split(' ').filter(number => number != '');

        const filteredArray = winingNumbers.filter(value => numbers.includes(value));
        filteredArray.forEach((arr, index) => {
            if (index == 0) {
                tmpTotal = 1;
            } else {
                tmpTotal = tmpTotal * 2;
            }
        });
        total += tmpTotal;
    });

    console.log('TOTAL:', total);

    // PART 2
    let scratchCards = [];
    total = 0;
    lines.forEach((line, index) => {
        let tmpTotal = 0;
        let tmp = line.split(': ')[1].split(' | ');
        let winingNumbers = tmp[0].split(' ').filter(number => number != '');
        let numbers = tmp[1].split(' ').filter(number => number != '');
        scratchCards.push({winingNumbers: winingNumbers, numbers: numbers, total: 1});
    });

    scratchCards.forEach((card, index) => {
        const numberOfMatches = card.winingNumbers.filter(value => card.numbers.includes(value)).length;
        for (let i = 0; i < card.total; i++) {
            let j = 0;
            while (j < numberOfMatches) {
                scratchCards[index+j+1].total += 1;
                j += 1;
            }
        }
        total += card.total;
    });
    console.log('TOTAL:', total);

} catch (err) {
    console.error(err);
}