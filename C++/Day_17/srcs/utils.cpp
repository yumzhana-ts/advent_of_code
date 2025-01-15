#include "include.hpp"

void print_debug(const std::string &text)
{
    if(DEBUG)
        std::cout << RED "[DEBUG]" << text << RESET_COLOR << std::endl;
}

void super_vector_print(std::vector<long long int> data)
{
	for(size_t i = 0; i < data.size(); i++)
	{
		std::cout << data[i] << std::endl;
	}
}

void debug_log(const std::string& message) 
{
    long long int debug = 0;
    if (debug)
        std::cerr << "[DEBUG]: " << message << std::endl;
}

void print_vector(const std::string& name, const std::vector<long long int>& vec)
{
    std::cerr << "[DEBUG] " << name << ": ";
    for (size_t v = 0; v < vec.size();v++) {
        std::cerr << vec[v] << " ";
    }
    std::cerr << std::endl;
}

