fn main() {
    let a:i8 = 1;
    let b:i8 = 2;
    let mut total:i8 = sum(a,b);
    println!("a = {}, b = {}, a+b = {}", a, b, total);
    total = -100;
    println!("New total = {}", total);
}

fn sum(x:i8, y:i8) -> i8{
    x + y
}