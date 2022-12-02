const fs = require("fs");

fs.readFile("test.txt", (err, data) => {
  if (err) throw err;

  const inputData = data.toString().replace(/\r\n/g, "\n").split("\n");
  const allNums = inputData
    .pop()
    .split(",")
    .map((x) => Number(x));

  console.log(allNums.reduce((a, b) => a + b, 0));
});
