#include "include.hpp"
#include <iostream>


void instruction_pointer(std::vector<long long int>& data) 
{
    if (data.size() == 2) {
        data.clear();
    } else if (data.size() >= 2) {
        data.erase(data.begin(), data.begin() + 2);
    }
}

std::unordered_map<long long int, std::vector<long long int> > instruction_cache;
std::mutex cache_mutex;

// Function to get instruction pointer, now with caching and thread safety
std::vector<long long int> get_instruction_pointer(long long int pointer) {
    {
        std::lock_guard<std::mutex> lock(cache_mutex);
        if (instruction_cache.find(pointer) != instruction_cache.end()) {
            return instruction_cache[pointer];
        }
    }

    long long int arr[] = {2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 0, 5, 5, 3, 0};
	//long long int arr[] = {0,3,5,4,3,0};
    std::vector<long long int> data(arr, arr + sizeof(arr) / sizeof(arr[0]));

    try {
        size_t new_pointer = pointer;

        if (new_pointer * 2 > data.size()) {
            throw std::out_of_range("Instruction pointer is out of range.");
        }

        std::vector<long long int> new_data(data.begin() + new_pointer * 2, data.end());
        {
            std::lock_guard<std::mutex> lock(cache_mutex);
            instruction_cache[pointer] = new_data;
        }
        return new_data;
    } catch (const std::out_of_range& e) {
        throw;
    }
}

void adv(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data) 
{
    long long int numerator = registers[0];
    std::string str = "combo";
    long long int exponential = input(str, operand, registers);
    long long int denominator = static_cast<long long int>(std::pow(2, exponential));
    double result = static_cast<double>(numerator) / denominator;
    registers[0] = static_cast<long long int>(result);
    instruction_pointer(data);
}

void bxl(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data) 
{
    long long int number = registers[1];
    std::string str = "literal";
    long long int result = number ^ input(str, operand, registers);
    registers[1] = result;
    instruction_pointer(data);
}

void bst(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data) 
{
	std::string str = "combo";
    long long int number = input(str, operand, registers);
    long long int result = number % 8;
    registers[1] = result;
    instruction_pointer(data);
}

void jnz(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data) 
{
	long long int number = registers[0];
    std::string str = "literal";
    if (number == 0)
        instruction_pointer(data);
    else {
        data = get_instruction_pointer(input(str, operand, registers));
    }
}

void bxc(std::vector<long long int>& registers, std::vector<long long int>& data) 
{
    long long int num_1 = registers[1];
    long long int num_2 = registers[2];
    long long int result = num_1 ^ num_2;
    registers[1] = result;
    instruction_pointer(data);
}

void out(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data, std::vector<long long int>& print_list) 
{
    std::string str = "combo";
    long long int number = input(str, operand, registers);
    long long int modulo = number % 8;
    print_list.push_back(modulo);
    instruction_pointer(data);
}

void bdv(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data) 
{
    long long int numerator = registers[0];
    std::string str = "combo";
    long long int exponential = input(str, operand, registers);
    long long int denominator = static_cast<long long int>(std::pow(2, exponential));
    double result = static_cast<double>(numerator) / denominator;
    registers[1] = static_cast<long long int>(result);
	instruction_pointer(data);
}

void cdv(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data) {
    long long int numerator = registers[0];
    std::string str = "combo";
    long long int exponential = input(str, operand, registers);
    long long int denominator = static_cast<long long int>(std::pow(2, exponential));
    double result = static_cast<double>(numerator) / denominator;
    registers[2] = static_cast<long long int>(result);
	instruction_pointer(data);
}