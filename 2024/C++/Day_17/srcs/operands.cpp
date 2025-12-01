#include "include.hpp"

long long int combo(long long int number, const std::vector<long long int>registers)
{
	switch(number)
	{
		case 0:
			return(number);
			break;
		case 1:
			return(number);
			break;
		case 2:
			return(number);
			break;
		case 3:
			return(number);
			break;
		case 4: 
			return(registers[0]);
			break;
		case 5:
			return(registers[1]);
			break;
		case 6:
			return(registers[2]);
			break;
		default:
			return(-1);
			break;
	}
}

void cases(long long int number, std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data, std::vector<long long int>& print_list)
{
	switch(number)
	{
		case 0:
			adv(registers, operand, data);
			break;
		case 1:
			bxl(registers, operand, data);
			break;
		case 2:
			bst(registers, operand, data);
			break;
		case 3:
			jnz(registers, operand, data);
			break;
		case 4: 
			bxc(registers, data);
			break;
		case 5:
			out(registers, operand, data, print_list);
			break;
		case 6:
			bdv(registers, operand, data);
			break;
		case 7:
			cdv(registers, operand, data);
			break;
	}
}

long long int input(std::string &type, long long int number, const std::vector<long long int>registers)
{
	if(type == "combo")
	{
		return (combo(number, registers));
	}
    else if(type == "literal" && number >=0 && number <=7)
	{
		return(number);
	}
	else
		return (-1);
}

