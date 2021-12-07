const fs = require("fs");

fs.readFile("input.txt", (err, data) => {
    if (err) throw err;

    const inputData = data.toString().replace(/\r\n/g, "\n").split("\n");
    const allNums = inputData
        .pop()
        .split(",")
        .map((x) => Number(x));

    for (let i = 0; i < 80; i++) {
        allNums.forEach((fish, index) => {
            if (fish === 0) {
                allNums[index] = 6;
                allNums.push(8);
            } else allNums[index] = fish - 1;
        });
    }
    console.log(allNums.length);
});
