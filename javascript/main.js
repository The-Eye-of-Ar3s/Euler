function prime_factorize(n) {
    r = [];
    p = 2;
    while (n >= p*p) {
        if (n%p == 0) {
            r.push(p);
            n = Math.floor(n/p);
        } else {
            p+=1;
        }
    }
    r.push(n);
    return r;
}

function is_palindrome(n) {
    return n.toString() == n.toString().split("").reverse().join("");
}

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

function solve003() {
    pf = prime_factorize(600851475143);
    return pf[pf.length-1]
}

function solve004() {
    let m = 0;
    let ml = 0;
    for (let i = 999; i > 100; i-=1) {
        for (let j = i; j > 100; j-=1) {
            ml = i*j;
            if (is_palindrome(ml) && ml > m) {
                m = ml;
            }
        }
    }
    return m;
}

function main(arg) {
    map = {
        "1": solve001,
        "2": solve002,
        "3": solve003,
        "4": solve004,
    }

    if (arg in map) {
        console.log(map[arg]().toString());
    } else {
        console.log("NA")
    }
    
}

main(process.argv[2])