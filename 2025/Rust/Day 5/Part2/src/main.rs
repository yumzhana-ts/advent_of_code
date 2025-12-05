mod helpers;

fn main() -> std::io::Result<()> {
    let mut ranges = helpers::read_range("src/input.txt")?;
    ranges.sort_by_key(|r| r.0);
    //println!("Before: {:?}", ranges);
	let mut sum = 0;
    let mut i = ranges.len();
    while i > 1 {
        i -= 1;
        let mut changed = true;
        while changed 
		{
            changed = false;
            let (curr_start, curr_end) = ranges[i];
            let (prev_start, prev_end) = ranges[i - 1];

            if curr_start >= prev_start && curr_end <= prev_end 
			{
                //println!("Removing (inside): {:?}", ranges[i]);
                ranges.remove(i);
                changed = false;
            }
			else if curr_start <= prev_end 
			{
                //println!("Merging {:?} into {:?}", ranges[i - 1], ranges[i]);
                ranges[i].0 = prev_start;
                ranges[i].1 = curr_end.max(prev_end);
                ranges.remove(i - 1);
                changed = true;
            }
        }
    }

	for range in ranges {
		sum += range.1 - range.0 + 1; // оставляем +1 для включительно
	}
    println!("Sum: {}", sum);
    Ok(())
}


