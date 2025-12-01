mod helpers;

fn wrap(pos: i32, delta: i32) -> i32 
{
    (pos + delta + 100) % 100
}

fn rota(pos: i32, delta: i32) -> i32 
{
    let mut count = 0;
    if delta > 0 
    {
        for x in pos+1 ..= pos+delta 
        {
            if x % 100 == 0 
            {
                count += 1;
            }
        }
    } 
    else 
    {
        for x in (pos+delta .. pos).rev() 
        {
            if x % 100 == 0 
            {
                count += 1;
            }
        }
    }
    count
}

fn main() -> std::io::Result<()> {
    let path = "src/input.txt";
    let moves = helpers::read_moves(path)?;
    let mut position = 50;
    let mut total_rotation = 0;

    for (dir, num) in &moves 
	{
        let rotation = if *dir == 'R' 
		{
            let r = rota(position, *num);
            position = wrap(position, *num);
            r
        } 
		else 
		{
            let r = rota(position, -*num);
            position = wrap(position, -*num);
            r
        };
        total_rotation += rotation;
    }
    println!("Total rotations: {}", total_rotation);
    Ok(())
}