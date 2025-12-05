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

pub fn read_range(path: &str) -> io::Result<Vec<(u64, u64)>> 
{
    let file = fs::File::open(path)?;
    let reader = io::BufReader::new(file);
    let mut ranges = Vec::new();
    for line_result in reader.lines() 
    {
        let line = line_result?;
        let trimmed = line.trim();
        if trimmed.is_empty() 
        {
            continue;
        }
        let parts: Vec<&str> = trimmed.split('-').collect();
        if parts.len() != 2 
        {
            break
        }
        let first: u64 = parts[0].parse().expect("Failed to parse the first number");
        let second: u64 = parts[1].parse().expect("Failed to parse the second number");
        ranges.push((first, second));
    }

    Ok(ranges)
}

