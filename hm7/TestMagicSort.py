import unittest
import random
from math import log2
from MagicSort import linear_scan, reverse_list, insertionsort, quicksort, mergesort,  magic_sort

class Test_linear_scan(unittest.TestCase):
    '''Linearscan test cases'''
    def test_linear(self): 
        #tests if function returns: already sorted
        listOne = [1, 2, 3, 4, 5]
        self.assertEqual(linear_scan(listOne),'already sorted')

        #tests if function returns: insertion sort
        listTwo = [5,4,3,2,1]
        self.assertEqual(linear_scan(listTwo),'insertion_sort')

        #tests if function returns: reverse sort
        listThree = [6, 5, 4, 3, 2, 1]
        self.assertEqual(linear_scan(listThree),'reverse_sort')

        #tests if function returns: quicksort1
        listFour = [1,3,2,4,5,9,8,7,6]
        self.assertEqual(linear_scan(listFour),'quicksort')

class Test_reverse_list(unittest.TestCase):
    '''reverse list test cases'''
    def test_reverse(self):
        #Reg list  (high to low)
        listOne = [6, 5, 4, 3, 2, 1]
        self.assertEqual(reverse_list(listOne),[1, 2, 3, 4, 5, 6])

        #Reg list (low to high)
        listTwo = [1, 2, 3, 4, 5, 6]
        self.assertEqual(reverse_list(listTwo),[6, 5, 4, 3, 2, 1])

        #list with missing numbers
        listThree = [7, 6, 5, 4, 2, 1]
        self.assertEqual(reverse_list(listThree),[1, 2, 4, 5, 6, 7])

        #List with neg integers
        listFour = [6, 5, 4, 3, 2, 1, 0, -1]
        self.assertEqual(reverse_list(listFour),[-1,0,1, 2, 3, 4, 5, 6])

        #not reversed
        listFive = [3, 2, 6, 4, 4, 1, 5]
        self.assertNotEqual(reverse_list(listFive),[1, 2, 3, 4, 4, 5, 6])

class Test_insertionsort(unittest.TestCase):
    '''Insertion sort test cases'''
    def test_insertion(self):
        #Reg list 
        listOne = [3, 2, 6, 4, 1, 5]
        self.assertEqual(insertionsort(listOne),[1, 2, 3, 4, 5, 6])

        #List with neg integers
        listTwo = [0, -1, 4, 3, 2, 5, 1]
        self.assertEqual(insertionsort(listTwo),[-1, 0, 1, 2, 3, 4, 5])

        #list with missing numbers
        listThree = [0, -1, 4, 3, 5, 1]
        self.assertEqual(insertionsort(listThree),[-1, 0, 1, 3, 4, 5])

        #list with duplicates
        listFour = [3, 2, 6, 4, 4, 1, 5]
        self.assertEqual(insertionsort(listFour),[1, 2, 3, 4, 4, 5, 6])
        
        #already sorted
        listFive = [1, 2, 3, 4, 5, 6]
        self.assertEqual(insertionsort(listFive),[1, 2, 3, 4, 5, 6])
 
class Test_quicksort(unittest.TestCase):
    '''quicksort test cases'''
    def test_depth_limit_quick_sort(self):
        # Test to see if the depth within quicksort functions/ Makes sure it goes to mergesort
        rand_list = [random.randint(9, 10000) for i in range(1000)]
        expected_sorted_list = sorted(rand_list)

        depth_threshold = 5
        result = quicksort(rand_list)

        self.assertEqual(result, expected_sorted_list)
        
        self.assertGreaterEqual(log2(len(rand_list))+1,  depth_threshold)

    def test_quicksort(self):
        #Reg list over 16
        listOne = [6, 5, 3, 2, 1, 4, 16, 13, 10, 11, 9, 18, 7, 12, 8, 15, 14, 17]
        self.assertEqual(quicksort(listOne),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

        #List with neg integers
        listTwo = [6, 5, 3, 2, 1, 4, 16, 13, 10, 11, 9, 18, 7,12, 8, 15, 14, 17, -1, -3, 0]
        self.assertEqual(quicksort(listTwo),[-3,-1,0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

        #List with duplicates
        listThree = [6, 5, 3, 2, 1, 4, 16, 13, 10, 11, 9, 18, 7,12, 8, 15, 14, 17, -1, -3, 0, 7]
        self.assertEqual(quicksort(listThree),[-3,-1,0,1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

        #already sorted
        listFour = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.assertEqual(quicksort(listFour),[1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

        #List with missing integers
        listFive = [6, 5, 3, 2, 4, 16, 13, 10, 11, 9, 18, 7,12, 8, 15, 14, 17, -1, -3, 0]
        self.assertEqual(quicksort(listFive),[-3,-1,0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

class Test_mergesort(unittest.TestCase): 
    '''merge sort test cases'''
    def test_mergesort(self):
        #Reg list over 16
        listOne = [6, 5, 3, 2, 1, 4, 16, 13, 10, 11, 9, 18, 7,12, 8, 15, 14, 17]
        self.assertEqual(mergesort(listOne),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

        #List with neg integers
        listTwo = [6, 5, 3, 2, 1, 4, 16, 13, 10, 11, 9, 18, 7,12, 8, 15, 14, 17, -1, -3, 0]
        self.assertEqual(mergesort(listTwo),[-3,-1,0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

        #List with duplicates
        listThree = [6, 5, 3, 2, 1, 4, 16, 13, 10, 11, 9, 18, 7,12, 8, 15, 14, 17, -1, -3, 0, 7]
        self.assertEqual(mergesort(listThree),[-3,-1,0,1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

        #already sorted
        listFour = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.assertEqual(mergesort(listFour),[1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

        #List with missing integers
        listFive = [6, 5, 3, 2, 4, 16, 13, 10, 11, 9, 18, 7,12, 8, 15, 14, 17, -1, -3, 0]
        self.assertEqual(mergesort(listFive),[-3,-1,0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18])

class Test_magicsort(unittest.TestCase): 
    '''Tests what sort function would work best for what list'''
    def test_magicsort(self):
        # Outputs and empty set
        listOne = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        self.assertEqual(magic_sort(listOne),set())

        # Outputs the reverse sort
        listTwo = [6, 5, 4, 3, 2, 1]
        self.assertEqual(magic_sort(listTwo),{'reverse_sort'})

        # Outputs the insertion sort
        listThree = [5, 4, 3, 2, 1]
        self.assertEqual(magic_sort(listThree),{'insertion_sort'})

        # Outputs the quicksort
        listFour = [1, 2, 3, 4, 5, 6, 7, 9, 8]
        self.assertEqual(magic_sort(listFour), {'quicksort'})
        
if __name__ == '__main__':
    unittest.main()