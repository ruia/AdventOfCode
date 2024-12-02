use std::fs;

fn main() {
    let file = "01.test.in";
    let data = fs::read(file).expect("Unable to read file");
    // println!("{}", data.len());

    for line in data.iter() {
        println!("{}", line);
    }
}