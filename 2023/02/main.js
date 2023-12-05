const { constants } = require('buffer');
const fs = require('fs');
const isTest = process.env.npm_config_test || false;

console.log('Problem: 02');
console.log('Is Test: ', isTest);

try {
    let sumIdGames = 0;
    const maxes = { red: 12, green: 13, blue: 14 };
    const lines = fs.readFileSync(__dirname + '/input' + (isTest ? '_test_part1' : ''), 'utf8').split('\n');

    lines.forEach(line => {
        const gameLine = line.split(': ');
        const gameId = gameLine[0].split(' ')[1];
        let illegal = false;
        gameLine[1].split(';').forEach(set => {
            set = set.trim();
            set.split(',').forEach(subSet => {
                subSet = subSet.trim();
                const x = subSet.split(' ');
                val = parseInt(x[0]);
                if (val > maxes[x[1]]) {
                    illegal = true;
                }
            });
        });

        if (!illegal) {
            sumIdGames += parseInt(gameId);
        }
    });

    console.log('TOTAL:', sumIdGames);
    // PART 2

    let sumPowers = 0;
    let powers = { red: 0, green: 0, blue: 0 };
    lines.forEach(line => {
        const gameLine = line.split(': ');
        const gameId = gameLine[0].split(' ')[1];
        gameLine[1].split(';').forEach(set => {
            set = set.trim();
            set.split(',').forEach(subSet => {
                subSet = subSet.trim();
                const x = subSet.split(' ');
                val = parseInt(x[0]);
                if (val > powers[x[1]]) {
                    powers[x[1]] = val;
                }
            });
        });
        sumPowers += powers.red * powers.green * powers.blue;
        powers = { red: 0, green: 0, blue: 0 };
    });

    console.log('TOTAL:', sumPowers);

} catch (err) {
    console.error(err);
}