from math import log2

def linear_scan(L):
    '''Linearly scans which sorting list to use'''
    num = len(L)
    check = True

    for i in range(1, num):
        if L[i] < L[i - 1]:
            check = False
    if check:
        return 'already sorted'
    elif num <= 5:
        return 'insertion_sort'
    elif all(L[i] >= L[i + 1] for i in range(num - 1)):
        return 'reverse_sort'
    else: 
        return 'quicksort'
            
def reverse_list(L):
    '''Reverses the order of the list'''
    i, j = 0, len(L) - 1 

    while i < j:
        L[i], L[j] = L[j], L[i]
        i +=1
        j -= 1
    return L

def insertionsort(L): 
    '''Function insertion sort --> sorts a list using insertion sort'''
    num = len(L)
    left = 0
    right = len(L)
    for i in range(left + 1, right):
        j = num - i - 1 #starting position and go till end of list
        while j < num - 1 and L[j]>L[j+1]:
            #swap positions 
            L[j], L[j+1] = L[j+1], L[j]
            j+=1
    return L

#helper function for quicksort
def partition(L, i, j):
    '''function that finds the partition position'''
    pivot = j - 1
    j = pivot -1
    while i < j :
        while L[i] < L[pivot]:
            i = i + 1
        while i<j and L[j] >= L[pivot]:
            j = j - 1
        if i < j:
            L[i], L[j] = L[j], L[i]
    if L[i]>= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    return pivot

def quicksort(L, left = 0, right = None, count = 0):
    '''Sorts the list using a recursive function (partition) (uses quicksort) '''
    if right is None:
        right = len(L) - 1

    if right - left  <= 16:
        return insertionsort(L)

    # the depth case
    if count >= log2(len(L))+1:
        return mergesort(L)
    
    # Base Case
    if right - left <= 1: return None

    #Div
    pivot = partition(L, left, right)

    #Conquer
    quicksort(L, left, pivot, count + 1)
    quicksort(L, pivot+1, right, count + 1)

    return L

# helper function for merge sort
def merge(A,B,L):
    '''merges the two sublists into one sorted list'''
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            L[i+ j] = A[i]
            i = i + 1
        else:
            L[i+j] = B[j]
            j = j+ 1
    
    L[i + j:] = A[i:] + B[j:]

def mergesort(L):
    '''Sorts a list using mergesort (splits into two and calls merge(helper function) to sort) '''
    if len(L) <= 16:
        return insertionsort(L)

    mid = len(L) // 2
    A = L[:mid]
    B = L[mid:]

    a = mergesort(A)
    b = mergesort(B)
    merge(a,b,L)

    return L

def magic_sort(L):
    '''Outputs which sort method is used for a list'''
    instance_method = set()
    result = linear_scan(L)

    if result == 'already sorted':
        return instance_method
    
    if result == 'insertion_sort':
        insertionsort(L)
        instance_method.add('insertion_sort')
        
    elif result == 'reverse_sort':
        reverse_list(L)
        
        instance_method.add('reverse_sort')

    elif result == 'quicksort':
        quicksort(L)
        instance_method.add('quicksort')

    return instance_method