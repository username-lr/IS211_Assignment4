import argparse
# other imports go here

import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:

            a_list[position] = a_list[position - 1]
            position = position - 1

            a_list[position] = current_value

    end = time.time()

    return end - start


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2

    end = time.time()

    return end - start

def gap_insertion_sort(a_list, start, gap):
	start_time = time.time()
    for i in range(start + gap, len(a_list), gap):
		current_value = a_list[i]
		position = i
		while position >= gap and a_list[position - gap] > current_value:
			a_list[position] = a_list[position - gap]
			position = position - gap
		a_list[position] = current_value

    end = time.time()
    
    return end - start_time
    
def python_sort(a_list):
    
    start = time.time()

    sorted(a_list)

    end = time.time()

    return end - start

if __name__ == "__main__":
    """Main entry point"""
    list = [500, 1000 , 5000]
    
    start = time.time()
    
    for list in list:
        for x in range(100):
            my_list = get_me_random_list(list)
            insertion_sort(list)
            
    end = time.time()
    total_time = end - start
    average_time = total_time / 100
    
    print(f"Average time to sort a list of {list} using Insertion Sort was%10.7f seconds to run, on average" % (average_time))
    
    start = time.time()
    
    for list in list:
        for x in range(100):
            my_list = get_me_random_list(list)
            shell_sort(list)
            
    end = time.time()
    total_time = end - start
    average_time = total_time / 100
    
    print(f"Average time to sort a list of {list} using Shell Sort was%10.7f seconds to run, on average" % (average_time))
    
    start = time.time()
    
    for list in list:
        for x in range(100):
            my_list = get_me_random_list(list)
            python_sort(list)
            
    end = time.time()
    total_time = end - start
    average_time = total_time / 100
    
    print(f"Average time to sort a list of {list} using Python Sort was%10.7f seconds to run, on average" % (average_time))
