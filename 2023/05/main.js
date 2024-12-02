const fs = require('fs');
const { nextTick } = require('process');
const isTest = process.env.npm_config_test || false;

console.log('Problem: 05');
console.log('Is Test: ', isTest);
console.log('');

try {
    const lines = fs.readFileSync(__dirname + '/input' + (isTest ? '_test_part1' : ''), 'utf8').split('\n');
    let almanac = {};
    let lastMapping = '';
    let finalVar = [];

    lines.forEach(line => {
        if (line !== '') {
            if (line.indexOf(':') > -1) {
                const title = line.split(': ');
                if (title.length > 1) {
                    almanac[title[0]] = title[1].split(' ').map(val => parseInt(val));
                } else {
                    lastMapping = title[0];
                }
            }
            if (lastMapping && line !== lastMapping) {
                let title = lastMapping.split(' ')[0];
                title = title.split('-to-')[1];
                if (!almanac[title]) {
                    almanac[title] = [];
                }
                let values = line.split(' ');
                almanac[title].push({ destinationStartPos: parseInt(values[0]), sourceStartPos: parseInt(values[1]), len: parseInt(values[2]) });
            }
        }
    });

    almanac.seeds.forEach((seed, index) => {
        let row = {
            seed: 0,
            soil: 0,
            fertilizer: 0,
            water: 0,
            light: 0,
            temperature: 0,
            humidity: 0,
            location: 0,
        }
        let valueChanged = false;

        row.seed = seed;
        almanac.soil.forEach(value => {
            if (seed >= value.sourceStartPos && seed <= (value.sourceStartPos + value.len - 1)) {
                const diff = value.destinationStartPos - value.sourceStartPos;
                row.soil = seed + diff;
                valueChanged = true;
            }
            if (!valueChanged) {
                row.soil = seed;
            }
        });

        valueChanged = false;
        almanac.fertilizer.forEach(value => {
            if (row.soil >= value.sourceStartPos && row.soil <= (value.sourceStartPos + value.len - 1)) {
                const diff = value.destinationStartPos - value.sourceStartPos;
                row.fertilizer = row.soil + diff;
                valueChanged = true;
            }
            if (!valueChanged) {
                row.fertilizer = row.soil;
            }
        });

        valueChanged = false;
        almanac.water.forEach(value => {
            if (row.fertilizer >= value.sourceStartPos && row.fertilizer <= (value.sourceStartPos + value.len - 1)) {
                const diff = value.destinationStartPos - value.sourceStartPos;
                row.water = row.fertilizer + diff;
                valueChanged = true;
            }
            if (!valueChanged) {
                row.water = row.fertilizer;
            }
        });

        valueChanged = false;
        almanac.light.forEach(value => {
            if (row.water >= value.sourceStartPos && row.water <= (value.sourceStartPos + value.len - 1)) {
                const diff = value.destinationStartPos - value.sourceStartPos;
                row.light = row.water + diff;
                valueChanged = true;
            }
            if (!valueChanged) {
                row.light = row.water;
            }
        });

        valueChanged = false;
        almanac.temperature.forEach(value => {
            if (row.light >= value.sourceStartPos && row.light <= (value.sourceStartPos + value.len - 1)) {
                const diff = value.destinationStartPos - value.sourceStartPos;
                row.temperature = row.light + diff;
                valueChanged = true;
            }
            if (!valueChanged) {
                row.temperature = row.light;
            }
        });

        valueChanged = false;
        almanac.humidity.forEach(value => {
            if (row.temperature >= value.sourceStartPos && row.temperature <= (value.sourceStartPos + value.len - 1)) {
                const diff = value.destinationStartPos - value.sourceStartPos;
                row.humidity = row.temperature + diff;
                valueChanged = true
            }
            if (!valueChanged) {
                row.humidity = row.temperature;
            }
        });

        valueChanged = false;
        almanac.location.forEach(value => {
            if (row.humidity >= value.sourceStartPos && row.humidity <= (value.sourceStartPos + value.len - 1)) {
                const diff = value.destinationStartPos - value.sourceStartPos;
                row.location = row.humidity + diff;
                valueChanged = true
            }
            if (!valueChanged) {
                row.location = row.humidity;
            }
        });
        finalVar.push(row);
    });
    let propertyName = 'location';
    let rowWithLowestLocation = finalVar.reduce((minRow, currentRow) => {
        return currentRow[propertyName] < minRow[propertyName] ? currentRow : minRow;
    }, finalVar[0]);

    console.log('Lowest position:', rowWithLowestLocation.location);

    // PART 2
    console.log('');
    console.log('');
    console.log('PART 2');
    console.log('');

    console.time('p2');

    almanac = {};
    lastMapping = '';
    finalVar = [];

    lines.forEach(line => {
        if (line !== '') {
            if (line.indexOf(':') > -1) {
                const title = line.split(': ');
                if (title.length > 1) {
                    const chunkSize = 2;
                    let original = title[1].split(' ').map(val => parseInt(val));
                    almanac[title[0]] = original;
                } else {
                    lastMapping = title[0];
                }
            }
            if (lastMapping && line !== lastMapping) {
                let title = lastMapping.split(' ')[0];
                title = title.split('-to-')[1];
                if (!almanac[title]) {
                    almanac[title] = [];
                }
                let values = line.split(' ');
                almanac[title].push({ destinationStartPos: parseInt(values[0]), sourceStartPos: parseInt(values[1]), len: parseInt(values[2]) });
            }
        }
    });
    console.log('almanac:', almanac);

    for (let i = 0; i < almanac.seeds.length; i += 2) {
        console.log('chunk:', Math.ceil((i+1)/2));
        let chunk = almanac.seeds.slice(i, i + 2);
        let oriSeed = chunk[0];
        chunk[0] = 0;
        for (let j = 0; j < chunk[1]; j++) {
            const seed = oriSeed + j;
            // console.log(seed);
            // tmpSeeds.push(index);
            let row = {
                seed: 0,
                soil: 0,
                fertilizer: 0,
                water: 0,
                light: 0,
                temperature: 0,
                humidity: 0,
                location: 0,
            }
            let valueChanged = false;

            row.seed = seed;
            almanac.soil.forEach(value => {
                if (seed >= value.sourceStartPos && seed <= (value.sourceStartPos + value.len - 1)) {
                    const diff = value.destinationStartPos - value.sourceStartPos;
                    row.soil = seed + diff;
                    valueChanged = true;
                }
                if (!valueChanged) {
                    row.soil = seed;
                }
            });

            valueChanged = false;
            almanac.fertilizer.forEach(value => {
                if (row.soil >= value.sourceStartPos && row.soil <= (value.sourceStartPos + value.len - 1)) {
                    const diff = value.destinationStartPos - value.sourceStartPos;
                    row.fertilizer = row.soil + diff;
                    valueChanged = true;
                }
                if (!valueChanged) {
                    row.fertilizer = row.soil;
                }
            });

            valueChanged = false;
            almanac.water.forEach(value => {
                if (row.fertilizer >= value.sourceStartPos && row.fertilizer <= (value.sourceStartPos + value.len - 1)) {
                    const diff = value.destinationStartPos - value.sourceStartPos;
                    row.water = row.fertilizer + diff;
                    valueChanged = true;
                }
                if (!valueChanged) {
                    row.water = row.fertilizer;
                }
            });

            valueChanged = false;
            almanac.light.forEach(value => {
                if (row.water >= value.sourceStartPos && row.water <= (value.sourceStartPos + value.len - 1)) {
                    const diff = value.destinationStartPos - value.sourceStartPos;
                    row.light = row.water + diff;
                    valueChanged = true;
                }
                if (!valueChanged) {
                    row.light = row.water;
                }
            });

            valueChanged = false;
            almanac.temperature.forEach(value => {
                if (row.light >= value.sourceStartPos && row.light <= (value.sourceStartPos + value.len - 1)) {
                    const diff = value.destinationStartPos - value.sourceStartPos;
                    row.temperature = row.light + diff;
                    valueChanged = true;
                }
                if (!valueChanged) {
                    row.temperature = row.light;
                }
            });

            valueChanged = false;
            almanac.humidity.forEach(value => {
                if (row.temperature >= value.sourceStartPos && row.temperature <= (value.sourceStartPos + value.len - 1)) {
                    const diff = value.destinationStartPos - value.sourceStartPos;
                    row.humidity = row.temperature + diff;
                    valueChanged = true
                }
                if (!valueChanged) {
                    row.humidity = row.temperature;
                }
            });

            valueChanged = false;
            almanac.location.forEach(value => {
                if (row.humidity >= value.sourceStartPos && row.humidity <= (value.sourceStartPos + value.len - 1)) {
                    const diff = value.destinationStartPos - value.sourceStartPos;
                    row.location = row.humidity + diff;
                    valueChanged = true
                }
                if (!valueChanged) {
                    row.location = row.humidity;
                }
            });

            finalVar.push(row);
        }
    }

    // almanac.seeds.forEach((seed, index) => {

    // });

    propertyName = 'location';
    rowWithLowestLocation = finalVar.reduce((minRow, currentRow) => {
        return currentRow[propertyName] < minRow[propertyName] ? currentRow : minRow;
    }, finalVar[0]);
    console.log('Lowest position:', rowWithLowestLocation.location);
    console.timeEnd('p2');
    // console.log(almanac);
} catch (err) {
}