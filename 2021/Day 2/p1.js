const fs = require("fs");

fs.readFile("input.txt", (err, data) => {
    if (err) throw err;

    const inputData = data.toString().replace(/\r\n/g, "\n").split("\n");

    let horizontalPosition = 0;
    let depth = 0;

    inputData.map((i) => {
        movement = i.substr(0, i.indexOf(" "));
        spaces = Number(i.substr(i.indexOf(" ") + 1));

        switch (movement) {
            case "forward":
                horizontalPosition += spaces;
                break;
            case "up":
                depth -= spaces;
                break;
            case "down":
                depth += spaces;
                break;
        }
    });

    console.log(horizontalPosition * depth);
});
