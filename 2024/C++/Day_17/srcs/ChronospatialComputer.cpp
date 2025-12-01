#include "include.hpp"

std::vector<long long int> process_data(std::vector<long long int> registers) 
{
	long long int arr[] = {2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 0, 5, 5, 3, 0};
	//long long int arr[] = {0,3,5,4,3,0};
    std::vector<long long int> data(arr, arr + sizeof(arr) / sizeof(arr[0]));

    std::vector<long long int> print_list;
    while (true) 
	{
		if (data.empty())
            break;	
        long long int operation = data[0];
        long long int operand = data[1];
		cases(operation, registers, operand, data, print_list);	
    }
    return print_list;
}

void* thread_func(void* arg) {
    long long int start = *(long long int*)arg;
    long long int end = start + 100000000;
    
    for (long long int i = start; i < end; ++i) {
        long long int arr[] = {i, 0, 0};
        std::vector<long long int> reg(arr, arr + sizeof(arr) / sizeof(arr[0]));
        std::vector<long long int> result = process_data(reg);
        
        //long long int arrt[] = {0,3,5,4,3,0};
		long long int arrt[] = {2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 0, 5, 5, 3, 0};
        std::vector<long long int> res(arrt, arrt + sizeof(arrt) / sizeof(arrt[0]));
        
        if (result == res) {
            std::cout << "match found: " << i << std::endl;
            pthread_exit(NULL);
        }
    }
    std::cout << "no match found: " << std::endl;
    pthread_exit(NULL);
}

int main() 
{
	long long int thr = 10;
	pthread_t threads[thr];
	long long int start_indices[] = {0, 100000000, 200000000, 300000000, 400000000, 500000000, 600000000, 700000000, 800000000, 900000000, 1000000000};
    //long long int start_indices[] = {2200000000};
	
	for (long long int i = 0; i < thr; ++i) {
		printf("Creating thread %lld with start_index: %lld\n", i, start_indices[i]);
		pthread_create(&threads[i], NULL, thread_func, &start_indices[i]);
	}
	for (long long int i = 0; i < thr; ++i) {
		pthread_join(threads[i], NULL);
		printf("Thread %lld joined.\n", i);
	}
    return 0;
}
