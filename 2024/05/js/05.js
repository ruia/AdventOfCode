const fs = require('node:fs');

const base = process.cwd() + '/2024/05/';
const files = [
  { name: 'test', filename: base + 'test.in' },
  { name: 'input', filename: base + 'data.in' },
];

for (let fileIndex = 0; fileIndex < files.length; fileIndex++) {
  const file = files[fileIndex];
  console.log(`Reading file: ${file.name}`);

  let fileData= fs.readFileSync(file.filename, 'utf8'); // Synchronous reading
  const [rulesData, pagesData] = fileData.trim().split('\n\n').map((data) => data.split('\n'));

  let middleSum = 0;
  pagesData.forEach((pages) => {
    pages = pages.split(',');

    let rules = [];

    rulesData.forEach((rule) => {
      rule = rule.split('|');
      if (pages.includes(rule[0]) && pages.includes(rule[1])) {
        rules.push(rule);
      }
    });

    let correctOrder = true;

    for (let i = 0; i < rules.length; i++) {
      // console.log(rules[i]);
      const firstIndex = pages.indexOf(rules[i][0]);
      const secondIndex = pages.indexOf(rules[i][1]);

      if (firstIndex > secondIndex) {
        correctOrder = false;
        break;
      }
    }

    if (correctOrder) {
      // console.log('Correct order');
      const middle = pages[Math.floor(pages.length / 2)];
      middleSum += parseInt(middle);
      // console.log('middle', pages[Math.floor(pages.length / 2)]);
    }


    // console.log(pages);
    // console.log(rules)
  });

  console.log('Result part 1', middleSum);
  // console.log('Part 1 results:', countWordOccurrences(grid, 'XMAS'));
  // console.log('Part 2 results:', countXShapeMAS(grid));
  // // console.log('Part 2 results2:', countMASInDiagonalPattern(grid))
}