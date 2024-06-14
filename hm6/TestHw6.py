import unittest
from hw6 import find_zero, sort_halfsorted, bubble, selection, insertion
from TestHelpers import generate_halfsorted, is_sorted

# TODO: implement tests for sort_halfsorted

class Test_SortHalfSorted(unittest.TestCase):
   '''test to see if bubblesort works with half sort'''
   def test_halfsorted_bubble(self): 
     for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 51):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

                        L_copy = L.copy()
                        bubble(L, 0, idx_zero)
                        L_copy.sort()

                        self.assertListEqual(L,L_copy)
                        bubble(L, 0, idx_zero+1, len(L))
                        self.assertTrue(is_sorted(L))

                        sort_halfsorted(L, bubble)
                        print(sort_halfsorted(L, bubble))
                        self.assertTrue(is_sorted(L))

   def test_halfsorted_selection(self): 
      '''test to see if bubblesort works with half sort'''
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 51):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

                        L_copy = L.copy()
                        selection(L, 0, idx_zero)
                        L_copy.sort()

                        self.assertListEqual(L,L_copy)
                        selection(L, 0, idx_zero+1, len(L))
                        self.assertTrue(is_sorted(L))

                        sort_halfsorted(L, selection)
                        self.assertTrue(is_sorted(L))


   def test_halfsorted_insertion(self): 
      '''test to see if bubblesort works with half sort'''

      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 51):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

                        L_copy = L.copy()
                        insertion(L, 0, idx_zero)
                        L_copy.sort()

                        self.assertListEqual(L,L_copy)
                        insertion(L, 0, idx_zero+1, len(L))
                        self.assertTrue(is_sorted(L))

                        sort_halfsorted(L, insertion)
                        self.assertTrue(is_sorted(L))

# Test provided for you
class Test_FindZero(unittest.TestCase):
   def test1_allLengthsAllIndices(self):
      '''Tests find_zero for every possible index, for lists from 1 to 100 items

         Lists
         -----
            '-' and '+' denote negative and positive ingeters, respectively
                                 idx_zero
            n = 1                
               L = [0]           0

            n = 2
               L = [0, +]        0
               L = [-, 0]        1

            n = 3                
               L = [0, +, +]     0
               L = [-, 0, +]     1  
               L = [-, -, 0]     2

            n = 4
               L = [0, +, +, +]  0
               L = [-, 0, +, +]  1
               L = [-, -, 0, +]  2
               L = [-, -, -, 0]  3
            ...
            n = 100
               L = [0, ..., +]   0
               ...
               L = [-, ..., 0]   99
      '''

      # note the use of `subTest`. These all count as 1 unittest if they pass,
      # but all that fail will be displayed independently
      for pattern in ['random', 'reverse', 'sorted']:
         with self.subTest(pattern=pattern):
            for n in range(1, 50):
               with self.subTest(n=n):
                  for i in range(n):
                     with self.subTest(i=i):
                        L, idx_zero = generate_halfsorted(n, idx_zero=i, pattern=pattern)
                        self.assertEqual(find_zero(L), idx_zero)

unittest.main()

