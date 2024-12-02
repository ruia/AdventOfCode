const fs = require('node:fs');

const files = [
  {name: 'test', filename: '01.test.in'},
  {name: 'input', filename: '01.in'},
];

files.forEach((file) => {
  console.log(`Reading file: ${file.name}`);
  fs.readFile(file.filename, 'utf8', (err, data) => {
    let list1 = [];
    let list2 = [];
    const input = data.split('\n');
    input.forEach((line) => {
      // console.log(line);
      const tmp = line.split('   ');
      list1.push(tmp[0]);
      list2.push(tmp[1]);
    });
    list1.sort();
    list2.sort();

    // console.log(list1);
    // console.log(list2);
    let sum = 0;
    for (let i = 0; i < list1.length; i++) {
      const distance = Math.abs(list1[i] - list2[i]);
      sum += distance;
    }
    console.log('Part 1 result',sum);
    //   console.log(data);
    sum = 0;
    for (let i = 0; i < list1.length; i++) {
      const sim = list1[i] * list2.filter((item) => item === list1[i]).length;
      sum += sim;
    }
    console.log('Part 2 result',sum);
  });
});