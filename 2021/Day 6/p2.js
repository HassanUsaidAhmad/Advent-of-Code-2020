const fs = require("fs");

fs.readFile("input.txt", (err, data) => {
    if (err) throw err;

    const inputData = data.toString().replace(/\r\n/g, "\n").split("\n");
    const allNums = inputData
        .pop()
        .split(",")
        .map((x) => Number(x));

    const allFish = Array(9).fill(0);

    for (const fish of allNums) {
        allFish[fish]++;
    }

    for (let i = 0; i < 256; i++) {
        const currentFish = allFish.shift();
        allFish.push(currentFish);
        allFish[6] += currentFish;
    }

    console.log(allFish.reduce((a, b) => a + b, 0));
});
