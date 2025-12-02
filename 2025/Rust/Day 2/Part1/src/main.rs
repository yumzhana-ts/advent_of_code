mod helpers;
use std::io;

fn main() -> io::Result<()> 
{
	//let green = "\x1b[32m";
    //let yellow = "\x1b[33m";
    //let reset = "\x1b[0m";
    let ranges = helpers::read_range("src/mini_input.txt")?;
	let mut sum = 0;
	for (start, end) in ranges 
	{
		//println!("{}Range is: [{}:{}]{}", green, start, end, reset);
		for item in start..=end 
		{
			let string = item.to_string();
			let numbers: Vec<char> = string.chars().collect();

			let mid = numbers.len() / 2;
			let first_half = &numbers[..mid];
			let second_half = &numbers[mid..];
			if first_half == second_half 
			{
				//println!("item {}", item);
				sum+=item;
			}
		}
	}
	println!("sum: {}", sum);
    Ok(())
}