mod helpers;
use std::io;

fn super_num(num: i64, add: i64) -> i64 
{
    num * 10 + add
}

fn char_to_i64(c: char) -> Option<i64> 
{
    c.to_digit(10).map(|d| d as i64)
}

fn process_count(vector: Vec<i64>, operations: &Vec<char>) -> i64
{
	let mut total = 0; 
	let mut sum = vector[0];
	let mut sign: isize = 0;
	let mut i = 1;
	while i < vector.len() 
	{
		if vector[i] == 0 
		{
			sign += 1;
			total+=sum;
			if i < vector.len() 
			{
				sum = vector[i+1];
			}
			i += 2;
			continue;
		}
		let case = operations[sign as usize];
		match case 
		{
			'*' => sum *= vector[i],
			'+' => sum += vector[i],
			_ => unreachable!(),
		}
		if i == vector.len() -1 
		{
			total+=sum;
		}
		i += 1;
	}
	return total;
}

fn main() -> io::Result<()> 
{
    let (matrix, operations) = helpers::read_matrix("src/mini_input.txt")?;
	let mut vector = Vec::new();
	for x in 0..matrix[0].len() 
	{
		let mut sum = 0;
		for y in 0..matrix.len() 
		{
			if let Some(digit) = char_to_i64(matrix[y][x]) 
			{
				sum = super_num(sum, digit);
			}
		}
		vector.push(sum);
	}
	println!("result: {}", process_count(vector, &operations));
	Ok(())
}