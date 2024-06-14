from hw3 import find_pairs_naive, find_pairs_optimized
import unittest

# Test cases for the naive function
class test_naive_True(unittest.TestCase):
    def test_naive(self):
        '''Test for empty list and for target 0'''
        list = []
        target = 0
        expected = find_pairs_naive(list,target)
        self.assertEqual(expected,[])

        '''Test for target 0'''
        list = [1,2,3,4]
        target = 0
        expected  = find_pairs_naive(list,target)
        self.assertEqual(expected,[])

        '''Test Expected Empty list'''
        listTwo =  [1, 2, 3, 4, 5] 
        targetTwo = 11
        expected_Empty_List = find_pairs_naive(listTwo,targetTwo)
        self.assertEqual(expected_Empty_List,[])

        '''Test Expected duplicate test'''
        listThree =  [1, 2, 3, 4, 5] 
        targetThree = 4
        expected_duplicate_test = find_pairs_naive(listThree,targetThree)
        self.assertEqual(expected_duplicate_test,[[1, 3]])



# Test cases for the optimized function 
class test_optimized_true(unittest.TestCase):
    def test_optimized(self):
        '''Test for empty list and for target 0'''
        list = []
        target = 0
        expected = find_pairs_optimized(list,target)
        self.assertEqual(expected,set())

        '''Test empty set'''
        list = []
        target = 1
        expected_empty_set = find_pairs_optimized(list,target)
        self.assertEqual(expected_empty_set,set())

        '''Test for target 0'''
        list = [1,2,3,4]
        target = 0
        expected_empty_set = find_pairs_optimized(list,target)
        self.assertEqual(expected_empty_set,set())

        '''Expected Empty set since value cannot be found'''
        listTwo =  [1, 2, 3, 4, 5] 
        targetTwo = 11
        expected_empty_set = find_pairs_optimized(listTwo,targetTwo)
        self.assertEqual(expected_empty_set,set())

        '''Expected duplicate test'''
        listThree =  [1, 2, 3, 4, 5] 
        targetThree = 4
        expected_duplicate_test = find_pairs_optimized(listThree,targetThree)
        self.assertEqual(expected_duplicate_test,{(1, 3)})

if __name__ == '__main__':
    unittest.main()

        