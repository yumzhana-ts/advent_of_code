#include "include.hpp"

int count_possible = 0;

bool can_form(const std::string& target, const std::vector<std::string>& towels, std::map<std::string, bool>& memo) 
{
    if (memo.find(target) != memo.end()) 
        return memo[target];
    if (target.empty()) 
        return true;
    for (std::vector<std::string>::const_iterator it = towels.begin(); it != towels.end(); ++it) 
    {
        const std::string& towel = *it;
        if (target.substr(0, towel.length()) == towel) 
        {
            std::string remaining = target.substr(towel.length());
            if (can_form(remaining, towels, memo)) 
            {
                memo[target] = true;
                return true;
            }
        }
    }
    memo[target] = false;
    return false;
}

bool towel_find(const std::vector<std::string>& towels, const std::string& target) 
{
    std::map<std::string, bool> memo; // Для мемоизации
    return can_form(target, towels, memo);
}

int main()
{
	std::cout << GREEN << "Let the party begin" << RESET_COLOR << std::endl;
	std::vector <std::string> designs;
	designs = my_super_vector_line("big_data/desired_design.txt");
	super_vector_print(designs);

	std::vector <std::string> towels;
	towels = my_super_vector_delim("big_data/towel_patterns.txt", ' ');
	super_vector_print(towels);
    for (size_t i = 0; i < designs.size(); i++) 
	{
        if (towel_find(towels, designs[i])) 
		{
			std::cout << designs[i] << std::endl; 
            count_possible++;
        }
    }
    std::cout << "Number of possible designs: " << count_possible << std::endl;
    return 0;
}
