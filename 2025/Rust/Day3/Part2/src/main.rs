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
        let digit = &number % &ten;
        digits.push(digit.clone());
        number /= &ten;
    }

    digits.reverse();
    digits
}

fn in_chunks(digits: &[BigInt], start: usize, end: usize, result: &mut BigInt)
{
    if start >= digits.len() 
    {
        return;
    }
    let mut max = BigInt::zero();
    let mut max_index = start;

    for i in start..end
    {
        if digits[i] > max 
        {
            max = digits[i].clone();
            max_index = i;
        }
    }
    *result = &*result * 10u32 + &digits[max_index];

    let next_start = max_index + 1;
    let next_end = end + 1;
    if next_end > digits.len()
    {
        return;
    }
    in_chunks(digits, next_start, next_end, result);
}

fn main() -> io::Result<()> 
{
    let numbers = helpers::read_line("src/input.txt")?;
    let mut sum = BigInt::zero();

    for item in numbers 
	{
        let digits = number_to_int(item.clone());
        let mut result = BigInt::zero();
        in_chunks(&digits, 0, digits.len() - 11, &mut result);
        sum += result;
    }
    println!("Voltage sum: {}", sum);
    Ok(())
}
