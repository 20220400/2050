import itertools

class BETNode:
    """Node for binary expression tree"""

    # Don't modify the provided code below - start working at add_left()

    # Some class variables (no need to make a copy of these for every node)
    # access these with e.g. `BETNode.OPERATORS`
    OPERATORS = {'+', '-', '*', '/'}
    CARD_VAL_DICT = {'A':1, '1':1, '2':2, '3':3, '4':4,
                     '5':5, '6':6, '7':7, '8':8, '9':9,
                     '10':10, 'J':11, 'Q':12, 'K':13}

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # These are proficed for you - do not modify. They let you hash BETs (so they can be stored in sets)
    # and compare them (so you can write unittests more easily).
    def __eq__(self, other):
        """Two nodes are equal if their values are equal and their subtrees are (recursively) equal"""
        if other is None: return False
        return self.value == other.value and self.left == other.left and self.right == other.right
    
    def __hash__(self):
        """Hash the whole tree (value + left and right subtrees)"""
        return hash((self.value, self.left, self.right))
    
    # START HERE
    def add_left(self,node):
        '''adds node as the left child'''
        if self.left is not None:
            raise ValueError("child already exists")
        else:
            self.left = node

    def add_right(self, node): 
        '''adds node as the right child'''
        if self.right is not None:
            raise ValueError("child already exists")
        else:
            self.right = node
          
    def evaluate(self): 
        '''Recursively evaluate the subtree rooted at this BETNode.'''

        if self.value in self.OPERATORS:
            
            left = self.left.evaluate()
            right = self.right.evaluate()

            if left in self.OPERATORS:
                left = float(left)
            elif isinstance(left, str):
                left = BETNode.CARD_VAL_DICT[left]

            if right in self.OPERATORS:
                right = float(right)
            elif isinstance(right, str):
                right = BETNode.CARD_VAL_DICT[right]
        
            if self.value == '+':
                return left + right
            elif self.value == '-':
                return left - right
            elif self.value == '*':
                return left * right
            else:
                if right == 0 or left == 0:
                    return 0
                return left / right
        else:
            return self.value
    
    def in_order(self):
        '''Helper function for repr: returns an in-order traversal of binary expression tree  '''
        if self.value in BETNode.OPERATORS:
             yield '('
      
        if self.left is not None: yield from self.left.in_order()  
        yield self.value                                              
        if self.right is not None: yield from self.right.in_order()

        if self.value in BETNode.OPERATORS:
            yield ')'
        
    def __repr__(self):
        '''Displays the expression stored in the BET'''
        str = ""
        str_helper = self.in_order()
        for i in str_helper:
            str += i
        return str
    
def post_to_in(lst):
    '''Helper function for create trees: return the root of a resulting tree'''
    a_stack = list()
    for i in lst:
        a_stack.append(BETNode(i))
        if i in BETNode.OPERATORS:
            node = a_stack.pop()
            node.add_right(a_stack.pop())
            node.add_left(a_stack.pop())
            a_stack.append(node)
    return a_stack.pop()

def create_trees(card): 
    '''Returns a set of every valid tree for a collection of 4 cards'''
    trees = set()
    for card in itertools.permutations(card):
        for operaters in itertools.product(BETNode.OPERATORS, repeat = 3):
        # Shape One: CCXCCXX
            
            cards = list(card)
            expr_one = [cards[0], cards[1], operaters[0], cards[2], cards[3], operaters[1], operaters[2]]
            root_one = post_to_in(expr_one)
            trees.add(root_one)
            
        #   Shape Two: CCXCXCX
            expr_two = [card[0],card[1],operaters[0],card[2],operaters[1],card[3],operaters[2]]
            root_two = post_to_in(expr_two)
            trees.add(root_two)
    
        #   Shape Three: CCCXXCX
            expr_three = [card[0],card[1],card[2],operaters[0],operaters[1],card[3],operaters[2]]
            root_three =  post_to_in(expr_three)
            trees.add(root_three)
            

        #   Shape Four: CCCXCXX
            expr_four = [card[0],card[1],card[2],operaters[0],card[3],operaters[1], operaters[2]]
            root_four = post_to_in(expr_four)
            trees.add(root_four)
            

        #   Shape Five: CCCCXXX
            expr_five = [card[0],card[1],card[2],card[3],operaters[0],operaters[1], operaters[2]]
            root_five = post_to_in(expr_five)
            trees.add(root_five)

    return trees
 
def find_solutions( cards):
    '''Finds solution for the create_trees method'''
    trees = create_trees(cards)
    solutions = set()
    if len(trees) == 0:
        return solutions
    
    for tree in trees:
        result = tree.evaluate()
        if result == 24:
            solutions.add(repr(tree))
    return solutions 


