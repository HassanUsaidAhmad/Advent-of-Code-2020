const fs = require("fs");

function mostFreq(arr) {
    const zeroNum = [];
    const oneNum = [];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "0") {
            zeroNum.push(arr[i]);
        } else if (arr[i] === "1") {
            oneNum.push(arr[i]);
        }
    }

    if (zeroNum.length === oneNum.length) {
        return "1";
    } else {
        return arr
            .sort(
                (a, b) =>
                    arr.filter((v) => v === a).length -
                    arr.filter((v) => v === b).length
            )
            .pop();
    }
}

function leastFreq(arr) {
    const zeroNum = [];
    const oneNum = [];

    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === "0") {
            zeroNum.push(arr[i]);
        } else if (arr[i] === "1") {
            oneNum.push(arr[i]);
        }
    }
    if (zeroNum.length === oneNum.length) {
        return "0";
    } else {
        return arr
            .sort(
                (a, b) =>
                    arr.filter((v) => v === b).length -
                    arr.filter((v) => v === a).length
            )
            .pop();
    }
}

fs.readFile("input.txt", (err, data) => {
    if (err) throw err;

    const inputData = data.toString().replace(/\r\n/g, "\n").split("\n");

    // inputData copy
    let ORating = [];
    for (let i of inputData) {
        ORating.push(i);
    }
    const CRating = [];
    for (let i of inputData) {
        CRating.push(i);
    }

    // nums is empty to store bits of first numbers
    let nums = [];
    const nums1 = [];
    // char for going over from start to end of the number
    let char = 0;
    let char1 = 0;

    while (char < ORating[0].toString().length) {
        for (let i = 0; i < ORating.length; i++) {
            nums.push(ORating[i].charAt(char));
        }
        let mostfreq = mostFreq(nums);
        const filterNums = ORating.filter(
            (num) => num.charAt(char) === mostfreq
        );
        ORating.length = 0;
        nums.length = 0;
        for (let i of filterNums) {
            ORating.push(i);
        }
        char++;
        if (ORating.length === 1) break;
    }

    while (char1 < CRating[0].toString().length) {
        for (let i = 0; i < CRating.length; i++) {
            nums1.push(CRating[i].charAt(char1));
        }
        let leastfreq = leastFreq(nums1);
        const filterNums1 = CRating.filter(
            (num) => num.charAt(char1) === leastfreq
        );
        CRating.length = 0;
        nums1.length = 0;
        for (let i of filterNums1) {
            CRating.push(i);
        }
        char1++;
        if (CRating.length === 1) break;
    }

    console.log(parseInt(ORating[0], 2) * parseInt(CRating[0], 2));
});
