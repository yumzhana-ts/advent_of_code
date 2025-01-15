#ifndef LINEN_LAYOUT
#define LINEN_LAYOUT

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <set>
#include <map>

std::vector<std::string> my_super_vector_line(const std::string &file_txt);
void super_vector_print(std::vector<std::string> data);
std::vector<std::string> my_super_vector_delim(const std::string& file_txt, char delimiter);
bool compare_by_length_desc(const std::string& a, const std::string& b);
void sort_towels_by_length_desc(std::vector<std::string>& towels);

#define DEBUG 1
#define RESET_COLOR "\033[0m"
#define BLACK "\033[0;30m"
#define RED "\033[0;31m"
#define GREEN "\033[0;32m"
#define BLUE "\033[0;34m"
#define WHITE "\033[0;37m"
#define BOLD_BLACK "\033[1;30m"
#define BG_WHITE "\033[0;47m"

#endif