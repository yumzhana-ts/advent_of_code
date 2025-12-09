mod helpers;
use std::io;

fn print_tree(grid: &Vec<Vec<char>>)
{
	for row in grid 
	{
		println!("{:?}", row);
	}	
}

fn collect_sticks(mut grid: Vec<Vec<char>>,mut sticks: Vec<(usize, usize)>) -> Vec<Vec<char>> 
{
    let mut i = 0;
    while i < sticks.len() 
	{
        let (y, x) = sticks[i];
        let next_y = y + 1;
        if next_y < grid.len() && grid[next_y][x] == '.' 
		{
            grid[next_y][x] = '|';
            sticks.push((next_y, x));
        }
		else if next_y < grid.len() && grid[next_y][x] == '^' 
		{
			let rhs = x + 1;
			let lhs = x - 1;
			grid[next_y][x] = '#';
			if rhs < grid[0].len() && x > 0
			{
				grid[next_y][rhs] = '|';
				sticks.push((next_y, rhs));
				grid[next_y][lhs] = '|';
				sticks.push((next_y, lhs));
			}
		}
        i += 1;
    }
    grid
}

fn draw_tree(mut grid: Vec<Vec<char>>) -> Vec<Vec<char>>
{
	let mut sticks  = Vec::new();
	for y in 0..grid.len() 
	{
		for x in 0..grid[y].len()
		{
			if grid[y][x] == 'S'
			{
				grid[y+1][x] = '|';
				sticks.push((y+1, x));
			}
		}
	}
	let new_grid = collect_sticks(grid.clone(), sticks);
	new_grid
}


fn main() -> io::Result<()> 
{
    let mut grid = helpers::read_matrix("src/mini_input.txt")?;
	grid = draw_tree(grid);
	print_tree(&grid);
	let mut beam_splitting = 0;
	for line in grid
	{
		for case in line
		{
			if case == '#'
			{
				beam_splitting+=1;
				
			}
		}
	}
	println!("beam splitting: {}", beam_splitting);
	Ok(())
}