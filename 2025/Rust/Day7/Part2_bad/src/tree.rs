use std::collections::HashSet;
use crate::node::Node;

pub fn print_tree(grid: &Vec<Vec<char>>) 
{
    for row in grid 
	{
        println!("{:?}", row);
    }
}

pub fn unique_sticks(sticks: &Vec<(usize, usize)>) -> Vec<(usize, usize)> 
{
    let mut seen = HashSet::new();
    sticks.iter().filter(|coord| seen.insert(**coord)).cloned().collect()
}

pub fn sticks_to_nodes(sticks: &Vec<(usize, usize)>) -> Vec<Node> 
{
    sticks.iter().map(|&(y, x)| Node::new(x, y)).collect()
}

pub fn collect_sticks(mut grid: Vec<Vec<char>>, mut sticks: Vec<(usize, usize)>) -> (Vec<Node>, Vec<Vec<char>>) 
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
            if rhs < grid[0].len() && x > 0 
            {
                // Помечаем новые пути в сетке, чтобы add_parents увидел их
                grid[next_y][rhs] = '|';
                grid[next_y][lhs] = '|';
                
                sticks.push((next_y, rhs));
                sticks.push((next_y, lhs));
            }
        }
        i += 1;
    }

    print_tree(&grid);
    let unique = unique_sticks(&sticks);
    let nodes = sticks_to_nodes(&unique);
    
    // Возвращаем кортеж (tuple)
    (nodes, grid) 
}

pub fn draw_tree(mut grid: Vec<Vec<char>>) -> (Vec<Node>, Vec<Vec<char>>) 
{
    let mut sticks = Vec::new();
    for y in 0..grid.len() {
        for x in 0..grid[y].len() 
		{
            if grid[y][x] == 'S' 
			{
                grid[y][x] = '|';
                grid[y + 1][x] = '|';
                sticks.push((y + 1, x));
            }
        }
    }
    let (mut nodes, grid) = collect_sticks(grid.clone(), sticks.clone());
    (nodes, grid)
}
