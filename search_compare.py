import argparse
# other imports go here
import time
import random

def get_me_random_list(n):
    """Generate list of n elements in random order
    
    :params: n: Number of elements in the list
    :returns: A list with n elements in random order
    """
    a_list = list(range(n))
    random.shuffle(a_list)
    return a_list
    
def sequential_search(a_list,item):
    pos = 0
    found = False
    
    start = time.time()
    
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    end = time.time()
    
    seq_searchtime = end - start
    
    return (found, seq_searchtime)
    
def ordered_sequential_search(a_list,item):
    pos = 0
    found = False
    stop = False
    
    start = time.time()
    
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos + 1

    end = time.time()
    
    ord_searchtime = end - start
    
        return(found, ord_searchtime)   


def binary_search_iterative(a_list,item):
    first = 0
    last = len(a_list) - 1
    found = False
    
    start = time.time()
    
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
        else:
            first = midpoint + 1
    
    end = time.time()        
    
    iter_searchtime = end - start
    
    return(found, iter_searchtime)
    
def binary_search_recursive(a_list,item):
    
    start = time.time()
    
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search(a_list[:midpoint], item)
        else:
            return binary_search(a_list[midpoint + 1:], item)
            
    end = time.time()   
    
    rec_searchtime = end - start
    
    return rec_searchtime

if __name__ == "__main__":
    """Main entry point"""
    list = [500, 1000 , 5000]
    
    start = time.time()
    
    for list in list:
        for x in range(100):
            my_list = get_me_random_list(list)
            sequential_search(list, -1)
    
    end = time.time()
    
    total = end - start
    
    print(f'Total Sequential Search run time: {total:10.7f}s')
    
        start = time.time()
    
    for list in list:
        for x in range(100):
            my_list = get_me_random_list(list)
            ordered_sequential_search(list, -1)
    
    end = time.time()
    
    total = end - start
    
    print(f'Total Ordered Sequential Search run time: {total:10.7f}s')
    
        start = time.time()
    
    for list in list:
        for x in range(100):
            my_list = get_me_random_list(list)
            binary_search_iterative(list, -1)
    
    end = time.time()
    
    total = end - start
    
    print(f'Total Iterative Binary Search run time: {total:10.7f}s')
    
            start = time.time()
    
    for list in list:
        for x in range(100):
            my_list = get_me_random_list(list)
            binary_search_recursive(list, -1)
    
    end = time.time()
    
    total = end - start
    
    print(f'Total Iterative Binary Search run time: {total:10.7f}s')
    
    
