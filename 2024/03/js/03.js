const fs = require('node:fs');

const base = process.cwd() + '/2024/03/';
const files = [
  { name: 'test', filename: base + 'test.in' },
  { name: 'input', filename: base + 'data.in' },
];

for (let fileIndex = 0; fileIndex < files.length; fileIndex++) {
  const file = files[fileIndex];
  console.log(`Reading file: ${file.name}`);

  let data = fs.readFileSync(file.filename, 'utf8'); // Synchronous reading

  let regex = /mul\(\d{1,3},\s*\d{1,3}\)/g;
  let operations = data.match(regex);
  let multiplicationsResults = operations.map((operation) => {
    operation = operation.replace('mul(', '');
    operation = operation.replace(')', '');
    operation = operation.split(',');
    return operation[0] * operation[1];
  });
  console.log('Part 1 results:', multiplicationsResults.reduce((accumulator, currentValue) => accumulator + currentValue, 0));

  if (file.name === 'test') {
    data = `xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))`;
  }

  regex = /(mul\(\d{1,3},\s*\d{1,3}\)|do\(\)|don't\(\))/g;
  operations = data.match(regex);

  multiplicationsResults = [];
  let multiplicationsEnabled = true;
  for (const oper of operations) {
    if (oper === 'do()') {
      multiplicationsEnabled = true;
    } else if (oper === `don't()`) {
      multiplicationsEnabled = false;
    } else if (multiplicationsEnabled) {
      let operation = oper.replace('mul(', '');
      operation = operation.replace(')', '');
      operation = operation.split(',');
      multiplicationsResults.push(operation[0] * operation[1]);
    }
  }
  console.log('Part 2 results:', multiplicationsResults.reduce((accumulator, currentValue) => accumulator + currentValue, 0));
}