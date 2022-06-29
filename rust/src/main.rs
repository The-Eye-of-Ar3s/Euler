use std::env;

fn prime_factorize(mut n: usize) -> Vec<usize> {
    let mut r = Vec::new();
    let mut p = 2;
    while n >= p*p {
        if n%p == 0 {
            r.push(p);
            n /= p;
        } else {
            p += 1;
        }
    }
    r.push(n);
    return r;
}

fn is_palindrome(n: usize) -> bool {
    let f = n.to_string();
    return f == f.chars().rev().collect::<String>();
}

fn solve001() -> usize {
    let mut s = 0;
    for i in 1..1000 {
        if i%3 == 0 || i%5 == 0 {
            s+=i;
        }
    }
    return s;
}

fn solve002() -> usize {
    let mut fib = vec![1, 2];
    while fib.last().unwrap() < &4000000 {
        fib.push(fib[fib.len()-1] + fib[fib.len()-2]);
    }
    fib.pop();
    let mut s = 0;
    for i in fib {
        if i%2 == 0 {
            s+=i;
        }
    }
    return s;
}

fn solve003() -> usize {
    return prime_factorize(600851475143).last().unwrap().clone();
}

fn solve004() -> usize {
    let mut ml;
    let mut m = 0;
    for i in (100..999).rev() {
        for j in (100..i).rev() {
            ml = i*j;
            if is_palindrome(ml) && ml > m {
                m = ml;
            }
        }
    }
    return m;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let problem = args[1].clone();
    match problem.as_str(){
        "1" => {
            println!("{}", solve001());
        }
        "2" => {
            println!("{}", solve002());
        }
        "3" => {
            println!("{}", solve003());
        }
        "4" => {
            println!("{}", solve004());
        }
        _ => {
            println!("NA");
        }
    }
}
