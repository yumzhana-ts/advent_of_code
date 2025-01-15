#include "Node.class.hpp"

void print_debug(const std::string &text)
{
    if (DEBUG)
        std::cout << RED "[DEBUG]" << text << RESET_COLOR << std::endl;
}

void print_vector(const std::vector<std::string> &vec)
{
    for (size_t i = 0; i < vec.size(); ++i) // Explicit index-based iteration
    {
        std::cout << vec[i] << std::endl;
    }
}

void super_vector_print(std::vector<long long int> data)
{
    for (size_t i = 0; i < data.size(); i++)
    {
        std::cout << data[i] << std::endl;
    }
}

void debug_log(const std::string &message)
{
    long long int debug = 0;
    if (debug)
        std::cerr << "[DEBUG]: " << message << std::endl;
}

void print_neighbors(const std::vector<s_neighbors>& neighbors) 
{
    for (std::vector<s_neighbors>::const_iterator it = neighbors.begin(); it != neighbors.end(); ++it) 
    {
        std::cout << RED << "[DEBUG] Vector info: " << "Neighbor Node ID: " << (*it->neighbor) << ", Direction: " << it->direction << RESET_COLOR << std::endl;
    }
}