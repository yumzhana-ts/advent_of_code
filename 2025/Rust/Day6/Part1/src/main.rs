mod helpers;
use std::io;

fn main() -> io::Result<()> 
{
    let (matrix, operations) = helpers::read_matrix("src/input.txt")?;
	//println!("{:?}", (matrix, operations));
	let mut total = 0; 
	for y in 0..matrix.len().saturating_sub(matrix.len() - 1)
	{
		for x in 0..matrix[y].len() 
		{
			let mut sum: i64 = matrix[y][x] as i64;
			for i in 1..matrix.len() {
				let case = operations[x];
				let value = matrix[y + i][x] as i64;
				match case {
					'*' => sum *= value,
					'+' => sum += value,
					'/' => sum /= value,
					'-' => sum -= value,
					_ => todo!(),
				}
			}
			total += sum;
		}
	}
	println!("sum: {}", total);
	Ok(())
}