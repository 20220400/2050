import time

def find_pairs_naive(lst, num):
    ''' This function uses two for loops to add to a list whether combinations of numbers from the two indexes adds to the num value'''
    sum_list = []
    for i in range(len(lst)- 1): # n
        for k in range(i + 1, len(lst)): # n
            if lst[i] + lst[k] == num: #2
                sum_list.append([lst[i],lst[k]]) #1
    return sum_list    # 1
    
# The lines that have the 'n' within the comments are more the the 'n' within the optimized function which means they add more time for the function to run
# The for loops essentially add more time. 

def find_pairs_optimized(lst,num):
    '''This function uses one for loop and a if statement conditions to optimize the running time'''
    pairs = set()
    lstTwo = set(lst)
    for i in lst: #n
        if (num - i) in lstTwo: #2
            if (num - i, i) not in pairs: #2
                if (num - i) != i: #2
                    pairs.add((i, num - i)) #1
    return pairs  # 1

 # Since there is one less for loop within the optimized function it decreased the time taken for the function to run
 # Since the if statements are run on constant time it does not run linearly 

def measure_min_time(f, args):
    """Unpacks the tuple for args and returns the min"""
    min_time = float('inf')
    for i in range(10):
        start = time.time()
        f(*args)
        end = time.time()
        execution = end - start
        if (execution < min_time):
            min_time = end - start
    return min_time
   

if __name__ == '__main__':
    target_num = 4
    lst =  [1,2,3,4,5] 
    x = find_pairs_optimized(lst,target_num)
    i = find_pairs_naive(lst,target_num)
    print(x)
    print(i)
    lst2 = [10, 50, 100, 150,200,300,500,1000,1500,2000,2500,3000,3500,4000] # for table

    '''Prints out table for measuring running time'''

    print('n'+ '\t'*5 + 'naive' + '\t'*5 +'optimized')
    print('****************************************************************************************************************************')

    '''For loop for printing out the comparison between naive and optimized function'''
    for i in lst2:
        k = [j for j  in range(i)]
        t1 = measure_min_time(find_pairs_naive, (k,target_num)) 
        t2 = measure_min_time(find_pairs_optimized, (k,target_num))
        i_list = i
        naive = round(t1,5)
        optimized = round(t2,5)
        print(str(i) +'\t'*5 + f'{naive:.4f}' + '\t'*5 + f'{optimized:.8f}')

    print('****************************************************************************************************************************')
  
