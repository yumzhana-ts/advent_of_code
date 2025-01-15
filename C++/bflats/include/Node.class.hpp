/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Node.class.hpp                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ytsyrend <ytsyrend@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/07/05 18:24:01 by ytsyrend          #+#    #+#             */
/*   Updated: 2025/01/06 14:07:33 by ytsyrend         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef NODE_CLASS_H
#define NODE_CLASS_H

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <set>
#include <map>

class Node;
struct t_neighbors;

class Node 
{
private:
    int id;
    std::pair<int, int> coordinates;
    std::vector<t_neighbors> neighbors;
    bool visited;
public:
    Node(std::pair<int, int> coordinates);
    ~Node(void);

    int get_id(void) const { return this->id; }
    void add_neighbor(Node* neighborNode, const std::string& dir);
    const std::vector<t_neighbors>& get_neighbors() const {return neighbors;}
    void set_coordinates(int y, int x) {coordinates = std::make_pair(y, x);}
    std::pair<int, int> get_coordinates(void) const {return coordinates;}

    void check_neighbors(int max_y, int max_x, const char keypad[][3]);
    bool operator==(const Node& other) const; 
};

std::ostream &operator<<(std::ostream & o, Node const &rhs);
Node find_start(const char array[][3], char start, int max_x, int max_y);
Node find_end(const char array[][3], char end, int max_x, int max_y);

typedef struct t_neighbors {
    Node* neighbor;
    std::string direction;
    
    bool operator==(const t_neighbors& other) const {
        std::pair<int, int> this_coords = neighbor->get_coordinates();
        std::pair<int, int> other_coords = other.neighbor->get_coordinates();
        return this_coords == other_coords;
    }
} s_neighbors;

typedef struct t_data
{
    char numeric_keypad[4][3];
    char directional_keypad[2][3];
    std::vector<s_neighbors>queue;
    std::vector<s_neighbors>visited;
}s_data;

void save_keypads(s_data *data);
void pathfinder(s_data *data, Node &start, Node &end, int max_x, int max_y, const char array[][3]);
void print_2d_array(const char array[][3], int rows, int cols);
void print_debug(const std::string &text);
void print_vector(const std::vector<std::string> &vec);
void print_neighbors(const std::vector<s_neighbors>& neighbors);

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