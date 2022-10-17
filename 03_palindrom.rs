fn main() {    
    let mut input_line = String::new();
    std::io::stdin()
    .read_line(&mut input_line)
    .expect("Failed to read line");

    let reverse = &input_line.to_lowercase().trim().chars().rev().collect::<String>();
    println!("{}", input_line.to_lowercase().trim() == reverse);
}
