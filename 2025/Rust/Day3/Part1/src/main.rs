mod helpers;
use std::io;
use num_bigint::BigInt;
use num_traits::{Zero};

fn number_to_int(mut number: BigInt) -> Vec<BigInt> 
{
    let mut digits = Vec::new();
    let ten = BigInt::from(10);

    while number > BigInt::zero() 
	{
        let digit = &number % &ten;   // number % 10
        digits.push(digit.clone());
        number /= &ten;               // number / 10
    }

    digits.reverse();
    digits
}


fn cut_the_crap(nums: &[BigInt], start_index: usize) -> BigInt 
{
    let mut max = BigInt::zero();
    for i in start_index + 1..nums.len() 
	{
        if nums[i] > max 
		{
            max = nums[i].clone();
        }
    }
    max
}

fn main() -> io::Result<()> 
{
    let numbers = helpers::read_line("src/mini_input.txt")?;
    let mut sum = BigInt::zero();

    for item in numbers 
	{
        let digits = number_to_int(item.clone());

        let mut first_num = BigInt::zero();
        let mut second_num = BigInt::zero();

        for num in 0..digits.len() - 1 
		{
            if digits[num] > first_num 
			{
                first_num = digits[num].clone();
                second_num = cut_the_crap(&digits, num);
            }
        }

        let voltage = &first_num * 10 + &second_num;
        sum += voltage;
    }

    println!("Voltage sum: {}", sum);
    Ok(())
}
