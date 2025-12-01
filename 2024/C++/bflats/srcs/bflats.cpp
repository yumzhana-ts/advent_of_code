#include "Node.class.hpp"

void push_to_queue(std::vector<s_neighbors> &destination, const std::vector<s_neighbors> &source)
{
	for (size_t i = 0; i < source.size(); ++i)
	{
		destination.push_back(source[i]);
	}
}

bool compare_neighbors(const s_neighbors &a, const s_neighbors &b) {
    return a.neighbor->get_coordinates().first == b.neighbor->get_coordinates().first && a.neighbor->get_coordinates().second == b.neighbor->get_coordinates().second;
}

bool search_in_vector(const std::vector<s_neighbors> &neighborsList, const s_neighbors &item)
{
    for (std::vector<s_neighbors>::const_iterator it = neighborsList.begin(); it != neighborsList.end(); ++it)
    {
        if (compare_neighbors(*it, item))
        {
            return true;
        }
    }
    return false;
}

void process_start(s_data *data, Node &start)
{
    t_neighbors s;
    s.direction = "None";
    s.neighbor = &start;
    data->queue.push_back(s);
    print_debug(" Processed starting node");
}

void pathfinder(s_data *data, Node &start, Node &end, int max_x, int max_y, const char keypad[][3])
{
    process_start(data, start);
    print_neighbors(data->queue);

    while (!data->queue.empty())
    {
        // Retrieve the current node
        t_neighbors current = data->queue.front();
        data->queue.erase(data->queue.begin());
        print_debug(" Processing node");
        std::cout  << std::endl;

        // If already visited, skip
        if (search_in_vector(data->visited, current))
        {
            print_debug("Visited node encountered");
            continue;
        }

        // Mark the current node as visited
        data->visited.push_back(current);

        // Check if we reached the end
        if (*current.neighbor == end)
        {
            std::cout << "End is here\n";
            return;
        }

        // Check neighbors
        current.neighbor->check_neighbors(max_y, max_x, keypad);
        print_neighbors(current.neighbor->get_neighbors());

        // Add unvisited neighbors to the queue
        const std::vector<s_neighbors> &neighbors = current.neighbor->get_neighbors();
        for (std::vector<s_neighbors>::const_iterator it = neighbors.begin(); it != neighbors.end(); ++it)
        {
            if (!search_in_vector(data->visited, *it))
            {
                data->queue.push_back(*it);
            }
        }

        print_neighbors(data->queue);
    }

    // If we exhaust the queue and don't find the end
    std::cout << "Queue is empty. Pathfinding complete.\n";
}

