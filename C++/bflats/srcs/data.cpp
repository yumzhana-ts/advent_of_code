#include "Node.class.hpp"

void save_keypads(s_data *data)
{
    char temp_numeric[4][3] = {
        {'7', '8', '9'},
        {'4', '5', '6'},
        {'1', '2', '3'},
        {'.', '0', 'A'}
    };

    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 3; j++)
            data->numeric_keypad[i][j] = temp_numeric[i][j];

    char temp_directional[2][3] = {
        {'.', '^', 'A'},
        {'<', 'v', '>'}
    };

    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 3; j++)
            data->directional_keypad[i][j] = temp_directional[i][j];
}

void print_2d_array(const char array[][3], int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            std::cout << array[i][j] << " ";
        }
        std::cout << std::endl; // Move to the next line after each row
    }
}