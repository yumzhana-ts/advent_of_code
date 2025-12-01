mod helpers;

fn wrap(pos: i32, delta: i32) -> i32 
{
    (pos + delta + 100) % 100
}

fn rota(pos: i32, delta: i32) -> i32 
{
    let mut count = 0;
    let green = "\x1b[32m";
    let yellow = "\x1b[33m";
    let reset = "\x1b[0m";
    if delta > 0 
    {
        let remaining_delta = delta - (100 - pos);
        println!("{}[Forward] Moving from {} by {}: remaining_delta = {}{}", yellow, pos, delta, remaining_delta, reset);
        if remaining_delta >= 0 
        {
            count = 1 + remaining_delta / 100;
            println!("{}{} times it went through 0 {}", green, count, reset);
        }
    } 
	else if delta < 0 
	{
		let remaining_delta = (-delta) - pos;
		println!("{}[Backward] Moving from {} by {}: remaining_delta = {}{}", yellow, pos, delta, remaining_delta, reset);

        if remaining_delta >= 0 
		{
			let remaining_delta = (-delta) - pos;
			if remaining_delta >= 0 
			{ 
				if pos == 0
				{
					count = remaining_delta / 100;
					println!("{}{} times it went through 0 {}", green, count, reset);
				}
				else
				{
					count = 1 + remaining_delta / 100;
					println!("{}{} times it went through 0 {}", green, count, reset);
				}
				
			}
		}
	}
    count
}



fn main() -> std::io::Result<()> {
    let path = "src/mini_input.txt";
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