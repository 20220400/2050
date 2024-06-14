# TODO: implement the 4 functions (as always, include docstrings & comments)
def find_zero(L):
    '''Binary search that returns index 0'''
    left = 0
    right = len(L) - 1
    while left <=right:
        median = (left+right)// 2
        if L[median] == 0:
            return median
        elif L[median] > 0:
            right = median - 1
        else:
            left = median + 1
    return median
  
def bubble(L, left, right): 
    '''Function bubble sort --> sorts a list using bubble sort'''
    for i in range(len(L)-1):
        swapped = False
        for  j in range(left, right-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
                swapped = True
                # print(f"List after iteration {i}: {L}")
        if not swapped:
            break

def selection(L, left, right): 
    '''Function insertion sort --> sorts a list using selection sort'''
    n = len(L)
    for i in range(left, right-1):
        min_index = i
        for j in range(i + 1, right):
            if L[j] < L[min_index]:
                min_index = j
        L[i], L[min_index] = L[min_index], L[i]
    

def insertion(L, left, right): 
    '''Function insertion sort --> sorts a list using insertion sort'''
   #get length of list L
    n = len(L)
    for i in range(left + 1, right):
        j = n - i - 1 #starting position and go til end of list
        while j < n - 1 and L[j]>L[j+1]:
            #swap positions 
            L[j], L[j+1] = L[j+1], L[j]
            j+=1

def sort_halfsorted(L, sort):
    '''Efficiently sorts a list comprising a series of negative items, a single 0, and a series of positive items
    
        Input
        -----
            * L:list
                a half sorted list, e.g. [-2, -1, -3, 0, 4, 3, 7, 9, 14]
                                         <---neg--->     <----pos----->

            * sort: func(L:list, left:int, right:int)
                a function that sorts the sublist L[left:right] in-place
                note that we use python convention here: L[left:right] includes left but not right

        Output
        ------
            * None
                this algorithm sorts `L` in-place, so it does not need a return statement

        Examples
        --------
            >>> L = [-1, -2, -3, 0, 3, 2, 1]
            >>> sort_halfsorted(L, insertion)
            >>> print(L)
            [-3, -2, -1, 0, 1, 2, 3]
    '''

    idx_zero = find_zero(L)     # find the 0 index 
    (L, 0, idx_zero)        # sort left half
    sort(L, idx_zero+1, len(L)) # sort right half

    
