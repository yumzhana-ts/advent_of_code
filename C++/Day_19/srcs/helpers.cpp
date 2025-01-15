#include "include.hpp"

//function for reading and saving line to vector
std::vector<std::string> my_super_vector_line(const std::string& file_txt)
{
	std::ifstream file(file_txt);
	if(!file.is_open())
	{
		std::cerr << "Error: Could not open the file." << std::endl;

	}
	std::string line;
	std::vector <std::string> data ;
	while(std::getline(file,line))
	{
		data.push_back(line);
	}
	file.close();
	return(data);
}

//function for reading and saving line to vector
std::vector<std::string> my_super_vector_delim(const std::string& file_txt, char delimiter) 
{
    std::ifstream file(file_txt);
    if (!file.is_open()) 
	{
        std::cerr << "Error: Could not open the file." << std::endl;
    }
    std::string line;
    std::vector<std::string> data;
    while (std::getline(file, line)) 
	{
        std::stringstream ss(line);
        std::string item;
        while (std::getline(ss, item, delimiter)) 
		{
            data.push_back(item);
        }
    }
    file.close();
    return data;
}

//vector printing out 
void super_vector_print(std::vector<std::string> data)
{
	for(size_t i = 0; i < data.size(); i++)
	{
		std::cout << data[i] << std::endl;
	}
}

bool compare_by_length_desc(const std::string& a, const std::string& b) 
{
    return a.length() > b.length();
}

// Function to sort the vector by length in descending order
void sort_towels_by_length_desc(std::vector<std::string>& towels) 
{
    std::sort(towels.begin(), towels.end(), compare_by_length_desc);
}