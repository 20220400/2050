import unittest
from BET import BETNode, create_trees, find_solutions

class TestBETNode(unittest.TestCase):
    def test_repr(self):
        '''tests the repr function'''
        r"""String representation
               *
              / \
             A   -
                / \
               2   +
                  / \
                 3   4

        """
        root = BETNode('*')
        root.add_left(BETNode('A'))
        root.add_right(BETNode('-'))
        root.right.add_left(BETNode('2'))
        root.right.add_right(BETNode('+'))
        root.right.right.add_left(BETNode('3'))
        root.right.right.add_right(BETNode('4'))
        expected_str = '(A*(2-(3+4)))'
        self.assertEqual(repr(root), expected_str)
       

    # TODO: Add test cases below. Repr is provided for you.
    def test_evaluate_tree1(self): 
      '''test evaluate function (basic tree)'''
      r"""String representation
                +
              /    \
            *       -
          / \       / \
         13  12   11   1
           
        """
      root = BETNode('+')
      root.add_left(BETNode('*'))
      root.add_right(BETNode('-'))
      root.left.add_left(BETNode('Q'))
      root.left.add_right(BETNode('K'))
      root.right.add_left(BETNode('J'))
      root.right.add_right(BETNode('A'))

      expected_result = (12 *13) + (11-1)
      self.assertEqual(root.evaluate(), expected_result)

    def test_evaluate_tree2(self):
        '''Evaluate function: Tests when a node is 0'''
        r"""String representation
                 +
              /     \
            /        -
          / \       / \
         13  12   11   1
           """
        root = BETNode('+')
        root.add_left(BETNode('*'))
        root.add_right(BETNode('-'))
        root.left.add_left(BETNode('Q'))
        root.left.add_right(BETNode(0))  
        root.right.add_left(BETNode('J'))
        root.right.add_right(BETNode('A'))

        r"""String Representation
              +
            /   \
           *    -
        / \    / \
        Q  0  J   A
        
        """

        expected_result = (0) + (11-1)
        self.assertEqual(root.evaluate(), expected_result)

class TestCreateTrees(unittest.TestCase):
    '''test create trees function'''
    def test_hand1(self): 
        '''Test for all unique cases'''
        card = ['A', '2', '3', '4']
        trees = create_trees(card)
        self.assertEqual(len(trees), 7680)
        
    def test_hand2(self):
        '''Test when two cards are duplicates'''
        play = ['A', 'A', '2', '3']
        trees = create_trees(play)
        self.assertEqual(len(trees), 3840)

class TestFindSolutions(unittest.TestCase):
    '''test find solutions function'''
    def test0sols(self): 
        '''Test case for 0 solutions'''
        hand = ['1', '1', '1', '1']
        solutions = find_solutions(hand)
        self.assertEqual(len(solutions), 0)

    def test_A23Q(self): 
        '''Test whether function returns 33'''
        hand = ['A', '2', '3', 'Q']
        solutions = find_solutions(hand)
        self.assertEqual(len(solutions), 33)

unittest.main()