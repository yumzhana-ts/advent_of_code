#ifndef ChronospatialComputer
#define ChronospatialComputer

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <stdexcept>
#include <mutex>
#include <pthread.h>
#define NUM_THREADS 10

void cases(long long int number, std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data, std::vector<long long int>& print_list);
long long int combo(long long int number, const std::vector<long long int>registers);
long long int input(std::string &type, long long int number, const std::vector<long long int>registers);
void instruction_pointer(std::vector<long long int>& data);
std::vector<long long int> get_instruction_pointer(long long int pointer);
void adv(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data);
void bdv(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data);
void bxl(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data);
void bst(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data);
void jnz(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data);
void bxc(std::vector<long long int>& registers, std::vector<long long int>& data);
void out(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data, std::vector<long long int>& print_list);
void cdv(std::vector<long long int>& registers, long long int operand, std::vector<long long int>& data);
void super_vector_print(std::vector<long long int> data);
void print_vector(const std::string& name, const std::vector<long long int>& vec);
void debug_log(const std::string& message);



#define DEBUG 0
#define RESET_COLOR "\033[0m"
#define BLACK "\033[0;30m"
#define RED "\033[0;31m"
#define GREEN "\033[0;32m"
#define BLUE "\033[0;34m"
#define WHITE "\033[0;37m"
#define BOLD_BLACK "\033[1;30m"
#define BG_WHITE "\033[0;47m"

#endif