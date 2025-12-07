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


pub fn read_matrix(path: &str) -> io::Result<(Vec<Vec<u32>>, Vec<char>)> {
    let file = fs::File::open(path)?;
    let reader = io::BufReader::new(file);

    let mut matrix = Vec::new();
    let mut operations = Vec::new();

    for line_result in reader.lines() 
    {
        let line = line_result?;
        let trimmed = line.trim();

        if let Some(op) = trimmed.chars().next() 
        {
            if matches!(op, '+' | '-' | '*' | '/')
            {
                let ops: Vec<char> = trimmed.split_whitespace().map(|s| s.chars().next().expect("Failed to parse operation")).collect();
                operations.extend(ops);
                continue;                
            }
        }
        let row: Vec<u32> = trimmed.split_whitespace().map(|s| s.parse::<u32>().expect("Failed to parse number")).collect();
        matrix.push(row);
    }

    Ok((matrix, operations))
}



