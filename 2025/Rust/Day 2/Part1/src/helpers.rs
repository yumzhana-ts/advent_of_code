use std::fs;
use std::io;
use std::io::BufRead;

#[allow(dead_code)]
pub fn read_file(path: &str) -> io::Result<String>
{
	fs::read_to_string(path)
}

#[allow(dead_code)]
pub fn print_file(path: &str) -> io::Result<()>
{
	let content = read_file(path)?;
	println!("{}", content);
	Ok(())
}

#[allow(dead_code)]
pub fn read_moves(path: &str) -> io::Result<Vec<(char,i32)>>
{
	let file = fs::File::open(path)?;
	let reader = io::BufReader::new(file);

	let mut moves = Vec::new();

	for line in reader.lines()
	{
		let line = line?;
		let dir = line.chars().next().expect("Empty line");
		let num: i32 = line[1..].parse().expect("Unable to convert to int");
		moves.push((dir, num));
	}
	Ok(moves)
}

pub fn read_range(path: &str) -> io::Result<Vec<(i64, i64)>> 
{
    // Open the file
    let file = fs::File::open(path)?;
    let reader = io::BufReader::new(file);

    // Vector to store pairs of numbers
    let mut ranges = Vec::new();

    // Go through each line in the file
    for line_result in reader.lines() {
        // Get the line or return an error
        let line = line_result?;
        // Remove whitespace from the start and end
        let trimmed = line.trim();

        // Skip empty lines
        if trimmed.is_empty() {
            continue;
        }

        // Split the line by the '-' character
        let parts: Vec<&str> = trimmed.split('-').collect();

        // Check that there are exactly two numbers
        if parts.len() != 2 {
            panic!("Invalid line format: {}", trimmed);
        }

        // Parse the numbers from strings
        let first: i64 = parts[0].parse().expect("Failed to parse the first number");
        let second: i64 = parts[1].parse().expect("Failed to parse the second number");

        // Store the pair in the vector
        ranges.push((first, second));
    }

    Ok(ranges)
}

