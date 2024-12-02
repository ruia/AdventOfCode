function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}

let numbers = [
    929142010, 467769747
];

let resultGCD = numbers.reduce(gcd, numbers[0]);

console.log(resultGCD);
