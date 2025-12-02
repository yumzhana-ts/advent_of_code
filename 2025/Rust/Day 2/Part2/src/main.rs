mod helpers;
use std::io;

/*
let first_third = &numbers[..third];
let second_third = &numbers[third..2*third];
let third_third = &numbers[2*third..];
k*slice 2k * slice;*/

fn funny_slicing(item: Vec<char>) -> bool 
{
    let length = item.len();
    let mid = length / 2;

    for slice in 1..=mid
    {
        if length % slice != 0 {
            continue;
        }

        let count = length / slice;
        let mut duplicates = true;
        let first_slice = &item[0..slice];

		//println!("Slice to compare {:?}", first_slice);
        for k in 0..count
        {
            let start = k * slice;
            let end = start + slice;
            let slice_to_compare = &item[start..end];

            if slice_to_compare != first_slice 
			{
                duplicates = false;
                break;
            }
        }

        if duplicates 
		{
            //println!("All slices are equal!");
            return true;
        }
    }

    false
}

fn main() -> io::Result<()> 
{
	//let green = "\x1b[32m";
    //let yellow = "\x1b[33m";
    //let reset = "\x1b[0m";
    let ranges = helpers::read_range("src/input.txt")?;
	let mut sum = 0;
	for (start, end) in ranges 
	{
		//println!("{}Range is: [{}:{}]{}", green, start, end, reset);
		for item in start..=end 
		{
			let string = item.to_string();
			let numbers: Vec<char> = string.chars().collect();
			if funny_slicing(numbers) == true
			{
				//println!("item {}", item);
				sum+=item;
			}
		}
	}
	println!("sum: {}", sum);
    Ok(())
}