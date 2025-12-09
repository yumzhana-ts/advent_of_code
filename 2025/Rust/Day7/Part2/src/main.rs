mod helpers;
use std::io;

fn print_tree(grid: &Vec<Vec<char>>)
{
	for row in grid 
	{
		println!("{:?}", row);
	}	
}

fn calculate_timelines(grid: &Vec<Vec<char>>) -> u64 
{
    let rows = grid.len();
    let cols = grid[0].len();
    let mut weights = vec![vec![0u64; cols]; rows];

    for y in 0..rows 
	{
        for x in 0..cols 
		{
            if grid[y][x] == 'S' 
			{
                weights[y][x] = 1;
            }
        }
    }

    for y in 0..rows - 1 
	{
        for x in 0..cols 
		{
            let current_weight = weights[y][x];
            if current_weight == 0
			{ 
				continue; 
			}
            let next_y = y + 1;

            if grid[next_y][x] == '^' 
			{
                if x > 0 
				{
					weights[next_y][x - 1] += current_weight; 
				}
                if x + 1 < cols 
				{
					weights[next_y][x + 1] += current_weight;
				}
            } 
			else 
			{
                weights[next_y][x] += current_weight;
            }
        }
    }
    weights[rows - 1].iter().sum()
}

fn main() -> io::Result<()> 
{
    let grid = helpers::read_matrix("src/input.txt")?;
    let total_timelines = calculate_timelines(&grid);
    println!("Total active timelines: {}", total_timelines);
    Ok(())
}