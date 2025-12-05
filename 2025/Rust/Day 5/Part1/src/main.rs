mod helpers;
use std::io;

fn main() -> io::Result<()> 
{
    let (ranges, numbers) = helpers::read_range("src/input.txt")?;
	//println!("{:?}", ranges);
	//println!("{:?}", numbers);
	let mut spoiled = Vec::new();
	for number in numbers
	{
		for (start, end) in &ranges
		{
			if (*start..=*end).contains(&number) 
			{
				if !spoiled.contains(&number) 
				{
					spoiled.push(number);
					//println!("number in spolied: {}", number);
				}				
			}
		}
	}
	println!("sum: {}", spoiled.len());
    Ok(())
}