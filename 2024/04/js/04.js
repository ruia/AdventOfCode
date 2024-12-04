const fs = require('node:fs');

const base = process.cwd() + '/2024/04/';
const files = [
  { name: 'test', filename: base + 'test.in' },
  // { name: 'input', filename: base + 'data.in' },
];

for (let fileIndex = 0; fileIndex < files.length; fileIndex++) {
  const file = files[fileIndex];
  console.log(`Reading file: ${file.name}`);

  let data = fs.readFileSync(file.filename, 'utf8'); // Synchronous reading
  const grid = data.split('\n').map(row => row.split(''));

  console.log('Part 1 results:', countWordOccurrences(grid, 'XMAS'));
  console.log('Part 2 results:', countXShapeMAS(grid));


}

// POWERED BY CHATGPT -.-'
function countWordOccurrences(grid, word) {
  const rows = grid.length;
  const cols = grid[0].length;
  const directions = [
      [0, 1],   // Right
      [0, -1],  // Left
      [1, 0],   // Down
      [-1, 0],  // Up
      [1, 1],   // Down-Right
      [1, -1],  // Down-Left
      [-1, 1],  // Up-Right
      [-1, -1]  // Up-Left
  ];

  let count = 0; // To store the total count of occurrences

  // Helper function to check word in a specific direction
  function checkDirection(x, y, dx, dy) {
      for (let i = 0; i < word.length; i++) {
          const newX = x + i * dx;
          const newY = y + i * dy;
          if (
              newX < 0 || newX >= rows ||
              newY < 0 || newY >= cols ||
              grid[newX][newY] !== word[i]
          ) {
              return false;
          }
      }
      return true;
  }

  // Search the grid
  for (let x = 0; x < rows; x++) {
      for (let y = 0; y < cols; y++) {
          if (grid[x][y] === word[0]) { // First letter matches
              for (const [dx, dy] of directions) {
                  if (checkDirection(x, y, dx, dy)) {
                      count++; // Increment count for each match
                  }
              }
          }
      }
  }

  return count; // Return the total count of occurrences
}


// POWERED BY JE! :P
// redo function to count X-shape word
// find all mas in the grid with an x
// like m . s
//      . a .
//      m . s

// mas could be in any direction like mas or sam or both sam sam in x shape

function countXShapeMAS(grid) {
  const word = 'MAS';
  const rows = grid.length;
  const cols = grid[0].length;

  let count = 0;

  // find all a's in the grid
  // we should ignore the first row and column because we can't have a full x-mas in the first row or column
  // hence the x,y  = 1
  for (let x = 1; x < rows; x++) {
    for (let y = 1; y < cols; y++) {
      if (grid[x][y] === word[1]) {
        console.log('found a at', x, y);
        if (
          (x-1 >= 0 && y-1 >= 0 && grid[x-1][y-1] === word[0] && // top left
          x+1 < rows && y+1 < cols && grid[x+1][y+1] === word[2]) || // bottom right
          (x-1 >= 0 && y-1 >= 0 && grid[x-1][y-1] === word[2] && // top left (reversed)
          x+1 < rows && y+1 < cols && grid[x+1][y+1] === word[0]) || // bottom right (reversed)
          (x-1 >= 0 && y+1 < cols && grid[x-1][y+1] === word[2] && // top right
          x+1 < rows && y-1 >= 0 && grid[x+1][y-1] === word[0]) || // bottom left
          (x-1 >= 0 && y+1 < cols && grid[x-1][y+1] === word[0] && // top right (reversed)
          x+1 < rows && y-1 >= 0 && grid[x+1][y-1] === word[2]) // bottom left (reversed)
        ) {
          // console.log('found x-mas with a at', x, y);
          count++;
        }
        // if (
        //   x-1 >= 0 && y-1 >= 0 && grid[x-1][y-1] === word[0] && // top left
        //   x+1 < rows && y+1 < cols && grid[x+1][y+1] === word[2] && // bottom right
        //   x-1 >= 0 && y+1 < cols && grid[x-1][y+1] === word[2] && // top right
        //   x+1 < rows && y-1 >= 0 && grid[x+1][y-1] === word[0] // bottom left
        // ) {
        //   console.log('found x-mas with a at', x, y);
        //   count++;
        // }


      }
    }
  }


  return count;
}
