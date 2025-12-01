/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.cpp                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ytsyrend <ytsyrend@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/07/05 18:41:01 by ytsyrend          #+#    #+#             */
/*   Updated: 2025/01/06 00:46:05 by ytsyrend         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "Node.class.hpp"


int main() 
{
    s_data data;
    save_keypads(&data);
    //print_2d_array(data.directional_keypad, 2, 3);
    Node start = find_start(data.numeric_keypad, 'A', 3, 4);
    Node end = find_end(data.numeric_keypad, '7', 3, 4);
    std::cout << start << end;
    pathfinder(&data, start, end, 3, 4, data.numeric_keypad);
    return (0);
}