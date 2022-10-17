fn main() {
    let mut input_line = String::new();
    std::io::stdin()
    .read_line(&mut input_line)
    .expect("Failed to read line");

    let x: i32 = input_line.trim().parse().expect("Input not an integer");

    for _ in 1..x {
        println!("Hello world!");
    }
}
