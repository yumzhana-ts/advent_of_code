/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   Node.class.cpp                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ytsyrend <ytsyrend@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/07/05 18:24:16 by ytsyrend          #+#    #+#             */
/*   Updated: 2025/01/05 23:17:17 by ytsyrend         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "Node.class.hpp"

/****************************************************/
/*                    Constructor                   */
/****************************************************/
int id_n = 0;

Node::Node(std::pair<int, int> coordinates_n) : coordinates(coordinates_n)
{
    id = id_n;
    id_n++;
    if (DEBUG)
    {
        std::cout << GREEN << "[Node] Constructor with id and coordinates called" << RESET_COLOR << std::endl;
    }
}

/****************************************************/
/*                    Destructor.                   */
/****************************************************/

Node::~Node(void)
{
    if (DEBUG)
    {
        std::cout << GREEN << "[Node] Destructor called" << RESET_COLOR << std::endl;
    }
}

/****************************************************
 *                 Memeber Functions                *
 ****************************************************/

std::ostream &operator<<(std::ostream &o, Node const &rhs)
{
    o << "[ID " << rhs.get_id() << "] {" << rhs.get_coordinates().first << ":" << rhs.get_coordinates().second << "}";
    return o;
}

void Node::add_neighbor(Node *neighborNode, const std::string &dir)
{
    s_neighbors neighbor;
    neighbor.neighbor = neighborNode;
    neighbor.direction = dir;
    this->neighbors.push_back(neighbor);
    std::cout << RED << "[DEBUG] Added neighbor " << *neighbor.neighbor << ") in direction " << neighbor.direction << ".\n" << RESET_COLOR;
    print_neighbors(this->neighbors);
}

bool check_range(int y, int x, int max_x, int max_y, const char keypad[][3])
{
    return (x >= 0 && x < max_x) && (y >= 0 && y < max_y) && keypad[y][x] != '.';
}

void Node::check_neighbors(int max_y, int max_x, const char keypad[][3])
{
    int y = this->coordinates.first;
    int x = this->coordinates.second;

    std::cout << "Checking neighbors for Node at (" << y << ", " << x << ")\n";

    int directions[4][2] =
        {
            {0, 1},
            {0, -1},
            {-1, 0},
            {1, 0}};
    const char *dir_chars[4] = {">", "<", "^", "v"};

    for (int i = 0; i < 4; ++i)
    {
        int new_y = y + directions[i][0];
        int new_x = x + directions[i][1];
        std::cout << "Checking direction " << dir_chars[i] << ": New coordinates (" << new_y << ", " << new_x << ")\n";
        if (check_range(new_y, new_x, max_x, max_y, keypad))
        {
            std::cout << "Coordinates (" << new_y << ", " << new_x << ") are valid and within range.\n";
            coordinates = std::make_pair(new_y, new_x);
            Node* neighbor = new Node(coordinates);
            Node::add_neighbor(neighbor, dir_chars[i]);
        }
    }

    std::cout << "Finished checking neighbors for Node at (" << y << ", " << x << ").\n";
}

bool Node::operator==(const Node &other) const
{
    return (this->coordinates.first == other.coordinates.first) && (this->coordinates.second == other.coordinates.second);
}

Node find_start(const char array[][3], char start, int max_x, int max_y)
{
    for (int i = 0; i < max_y; i++)
    {
        for (int j = 0; j < max_x; j++)
        {
            if (array[i][j] == start)
            {
                std::pair<int, int> coordinates = std::make_pair(i, j);
                Node start_node(coordinates);
                return start_node;
            }
        }
    }
    return Node(std::make_pair(-1, -1));
}

Node find_end(const char array[][3], char end, int max_x, int max_y)
{
    for (int i = 0; i < max_y; i++)
    {
        for (int j = 0; j < max_x; j++)
        {
            if (array[i][j] == end)
            {
                std::pair<int, int> coordinates = std::make_pair(i, j);
                Node end(coordinates);
                return (end);
            }
        }
    }
    return Node(std::make_pair(-1, -1));
}
