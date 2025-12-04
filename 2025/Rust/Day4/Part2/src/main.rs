mod helpers;
use std::io;

/*
let up = (y - 1, x);
let down = (y + 1, x);
let right = (y, x + 1);
let left = (y, x - 1);
let up_right = (y - 1, x + 1);
let up_left = (y - 1, x - 1);
let down_right = (y + 1, x + 1);
let down_left = (y + 1, x - 1);
*/

fn validate_positions(positions: &Vec<(isize, isize)>, warehouse: &Vec<Vec<char>>) -> bool 
{
    let mut count_papers = 0; 
    for &(y, x) in positions 
	{
        if y >= 0 && (y as usize) < warehouse.len() && x >= 0 && (x as usize) < warehouse[y as usize].len()
		{
            if warehouse[y as usize][x as usize] == '@' 
			{
                count_papers += 1;
            }
        }
    }
    count_papers < 4
}

fn warehouse_cleanup(warehouse: &mut Vec<Vec<char>>, result: &mut i32)
{
    let mut sum = 0;
	for y in 0..warehouse.len()
	{
		for x in 0..warehouse[y].len()
		{
			if warehouse[y][x] == '@'
			{
				let y_pos = y as isize;
				let x_pos = x as isize;
				let positions = vec![(y_pos - 1, x_pos), (y_pos + 1, x_pos), (y_pos, x_pos + 1), (y_pos, x_pos - 1), (y_pos - 1, x_pos + 1), (y_pos - 1, x_pos - 1), (y_pos + 1, x_pos + 1), (y_pos + 1, x_pos - 1)];
				if validate_positions(&positions, &warehouse)
				{
					sum+=1;
                    warehouse[y_pos as usize][x_pos as usize] = '.';
				}
			}
		}
	}
    *result+=sum;
    if sum > 0
    {
        warehouse_cleanup(warehouse, result);
    }
}


fn main() -> io::Result<()> 
{
    let mut warehouse = helpers::read_cases("src/input.txt")?;
	let mut result = 0;
    warehouse_cleanup(&mut warehouse, &mut result);
	println!("Total rolls of paper: {}", result);
    Ok(())
}