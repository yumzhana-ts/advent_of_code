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


pub fn read_matrix(path: &str) -> io::Result<(Vec<Vec<char>>, Vec<char>)> {
    let file = fs::File::open(path)?;
    let reader = io::BufReader::new(file);

    let mut matrix: Vec<Vec<char>> = Vec::new();
    let mut operations: Vec<char> = Vec::new();

    for line_result in reader.lines() {
        let line = line_result?;

        if line.chars().any(|c| matches!(c, '+' | '*')) {
            // store operations line separately
            for c in line.chars() {
                if matches!(c, '+' | '*') {
                    operations.push(c);
                }
            }
            continue;
        }

        // store numbers line as chars to preserve exact spacing
        matrix.push(line.chars().collect());
    }

    Ok((matrix, operations))
}



