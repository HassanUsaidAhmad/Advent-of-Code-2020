const fs = require("fs");

function mostFreq(arr) {
    return arr
        .sort(
            (a, b) =>
                arr.filter((v) => v === a).length -
                arr.filter((v) => v === b).length
        )
        .pop();
}

fs.readFile("input.txt", (err, data) => {
    if (err) throw err;

    const inputData = data.toString().replace(/\r\n/g, "\n").split("\n");
    const nums = [];
    const gammaRate = [];

    let char = 0;

    while (char < inputData[0].toString().length) {
        for (let i = 0; i < inputData.length; i++) {
            nums.push(inputData[i].charAt(char));
        }
        gammaRate.push(mostFreq(nums));
        nums.length = 0;
        char++;
    }
    // Gives an array of number
    const gammaRateNum = gammaRate.map((i) => Number(i));
    const revGammaRate = gammaRate.map((i) => 1 - i);
    // Combine the array of numbers into number only
    let a = gammaRateNum.join("");
    let b = revGammaRate.join("");

    console.log(parseInt(a, 2) * parseInt(b, 2));
});
