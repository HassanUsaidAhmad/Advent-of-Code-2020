const fs = require("fs");

fs.readFile("input.txt", (err, data) => {
    if (err) throw err;

    const inputData = data.toString().replace(/\r\n/g, "\n").split("\n");

    let horizontalPosition = 0;
    let aim = 0;
    let depth = 0;
    let sum = 0;

    inputData.map((i) => {
        movement = i.substr(0, i.indexOf(" "));
        spaces = Number(i.substr(i.indexOf(" ") + 1));

        switch (movement) {
            case "forward":
                horizontalPosition += spaces;
                depth = spaces * aim;
                sum += depth;
                break;
            case "up":
                aim -= spaces;
                break;
            case "down":
                aim += spaces;
                break;
        }
    });

    console.log(horizontalPosition * sum);
});
