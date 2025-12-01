mod helpers;

fn wrap(pos: i32, delta: i32) -> i32 
{
    (pos + delta + 100) % 100

}

fn main() -> std::io::Result<()>
{
	let path = "src/input.txt";
	let moves = helpers::read_moves(path)?;
	let mut position = 50;
	let mut rotation = 0;
	for(dir, num) in &moves 
	{
		println!("{} {}", dir, num);
		if *dir == 'R'
		{
			position = wrap(position, *num);
			println!("Right rotation: {}", position); 
		}
		else
		{
			position = wrap(position, -*num);
			println!("Left rotation: {}", position);
		}
		if position == 0
		{
			rotation+=1;
		}
	}
	println!("Rotations: {}", rotation);
	Ok(())
}