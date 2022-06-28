function solve001() {
    let s = 0;
    for (let i = 1; i < 1000; i++) {
        if (i%3 == 0 || i%5 == 0) {
            s += i;
        }
    }
    return s;
}

function solve002() {
    let fib = [1, 2];
    let l = fib.length
    while (fib[l-1] < 4000000) {
        l = fib.length;
        fib.push(fib[l-1]+fib[l-2]);
    }
    fib.pop();
    s = 0;
    for (let i of fib) {
        if (i%2 == 0) {
            s += i;
        }
    }
    return s;
}

function main(arg) {
    map = {
        "1": solve001,
        "2": solve002
    }

    if (arg in map) {
        console.log(map[arg]().toString());
    } else {
        console.log("NA")
    }
    
}

main(process.argv[2])