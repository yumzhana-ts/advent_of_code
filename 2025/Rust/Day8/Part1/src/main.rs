mod helpers;
use std::io;

fn distance_sq(p1: &(i64, i64, i64), p2: &(i64, i64, i64)) -> i64 
{
    let dx = p1.0 - p2.0;
    let dy = p1.1 - p2.1;
    let dz = p1.2 - p2.2;

	dx * dx + dy * dy + dz * dz
}

fn process_chains(pairs: Vec<(i64, usize, usize)>) 
{
    let mut chains: Vec<Vec<usize>> = Vec::new();
    let mut successful_connections = 0;

    for &(_dist, i, j) in pairs.iter() 
	{
        let mut chain_idx_i: Option<usize> = None;
        let mut chain_idx_j: Option<usize> = None;

        for (idx, chain) in chains.iter().enumerate() 
		{
            if chain.contains(&i) 
			{ 
				chain_idx_i = Some(idx); 
			}
            if chain.contains(&j) 
			{ 
				chain_idx_j = Some(idx); 
			}
        }

        match (chain_idx_i, chain_idx_j) 
		{
            (None, None) => {
                chains.push(vec![i, j]);
                successful_connections += 1;
            }

            (Some(idx), None) => {
                chains[idx].push(j);
                successful_connections += 1;
            }
            (None, Some(idx)) => {
                chains[idx].push(i);
                successful_connections += 1;
            }
            (Some(idx_i), Some(idx_j)) => 
			{
                if idx_i != idx_j 
				{
                    let mut target_chain = chains[idx_j].clone();
                    chains[idx_i].append(&mut target_chain);
                    // Вместо remove, просто очистим вторую цепь, чтобы не ломать индексы
                    chains[idx_j].clear(); 
                    successful_connections += 1;
                } 
				else 
				{
                    successful_connections += 1;
                }
            }
        }
        if successful_connections == 1000
		{ 
			break; 
		}
    }
	//println!("{:?}", chains);
	chains.sort_by_key(|ch| ch.len());
	chains.reverse();
	//println!("{:?}", chains);
	let mut sum = chains[0].len(); 
	for v in 1..3 
	{ 
		sum*=chains[v].len(); 
	} 
	println!("sum: {}", sum);
}

fn main() -> io::Result<()> 
{
    let points = helpers::read_coordinates("src/input.txt")?;
	println!("{:?}", points);
	let mut pairs = Vec::new();

    for i in 0..points.len() 
	{
        for j in i+1..points.len() 
		{
            let dist_sq = distance_sq(&points[i], &points[j]);
            pairs.push((dist_sq, i, j));
        }
    }
    pairs.sort_by_key(|k| k.0);
	process_chains(pairs);
	Ok(())
}