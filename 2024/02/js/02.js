const fs = require('node:fs');

const base = process.cwd() + '/2024/02/';
const files = [
  { name: 'test', filename: base + 'test.in' },
  { name: 'input', filename: base + 'data.in' },
];

for (let fileIndex = 0; fileIndex < files.length; fileIndex++) {
  const file = files[fileIndex];
  console.log(`Reading file: ${file.name}`);

  let reports = [];
  let safeCount = 0;
  let safeCountExtra = 0;

  const data = fs.readFileSync(file.filename, 'utf8'); // Synchronous reading
  const input = data.split('\n');
  reports = input.map((line) => line.split(' ').map((num) => parseInt(num)));

  for (let reportIndex = 0; reportIndex < reports.length; reportIndex++) {
    const report = reports[reportIndex];
    if (checkOrder(report) === 'safe') {
      safeCount++;
    } else {
      for (let i = 0; i < report.length; i++) {
        const tmpReport = [...report];
        tmpReport.splice(i, 1);
        if (checkOrder(tmpReport) === 'safe') {
          safeCountExtra++;
          break;
        }
      }
    }

  }
  console.log('Part one safeCount:', safeCount);
  console.log('Part two safeCount:', safeCountExtra + safeCount);
}


function checkOrder(array) {
  // console.log(array);
  if (array.length < 2) return 'Array too short to determine order';

  let isIncreasing = true;
  let isDecreasing = true;

  for (let i = 1; i < array.length; i++) {
    if (array[i] > array[i - 1]) {
      isDecreasing = false;
    } else if (array[i] < array[i - 1]) {
      isIncreasing = false;
    } else {
      return 'unsafe';
    }
    const diff = Math.abs(array[i] - array[i - 1]);
    // console.log(diff);
    if (diff < 1 || diff > 3) {
      return 'unsafe';
    }
    // console.log({isDecreasing:isDecreasing,isIncreasing:isIncreasing, i:array[i]});
  }

  if (isIncreasing) return 'safe';
  if (isDecreasing) return 'safe';
  return 'unsafe';
}