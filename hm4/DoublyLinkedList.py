# Do not modify this class
class Node:
    'Node object to be used in DoublyLinkedList'

    def __init__(self, item, _next=None, _prev=None):
        'initializes new node objects'
        self.item = item
        self._next = _next
        self._prev = _prev

    def __repr__(self):
        'String representation of Node'
        return f"Node({self.item})"


class DoublyLinkedList:
    def __init__(self, items=None):
        'Construct a new DLL object'
        self._head = None
        self._tail = None
        self._len = 0
        self._nodes = dict()    # dictionary of item:node pairs

        # initialize list w/ items if specified
        if items is not None:
            for item in items:
                self.add_last(item)

    def __len__(self):
        'returns number of nodes in DLL'
        return self._len

    # TODO: Modify the 4 methods below to keep `self._nodes` up-to-date
    def add_first(self, item):
        'adds item to front of dll'
        # add new node as head
        self._head = Node(item, _next=self._head, _prev=None)
        self._len += 1
        # Dictionary
        self._nodes[item] = self._head
        # if that was the first node
        if len(self) == 1:
            self._tail = self._head

        # otherwise, redirect old heads ._tail pointer
        else:
            self._head._next._prev = self._head

    def add_last(self, item):
        'adds item to end of dll'
        # add new node as head
        self._tail = Node(item, _next=None, _prev=self._tail)
        self._len += 1

        # Dictionary
        self._nodes[self._tail.item] = self._tail
        # if that was the first node
        if len(self) == 1:
            self._head = self._tail

        # otherwise, redirect old heads ._tail pointer
        else:
            self._tail._prev._next = self._tail

    def remove_first(self):
        'removes and returns first item'
        if len(self) == 0:
            raise RuntimeError("cannot remove from empty dll")

        # dictionary
        del self._nodes[self._head.item]

        # extract item for later
        item = self._head.item
        self._nodes[item] = item

        # move up head pointer
        self._head = self._head._next
        self._len -= 1

        # was that the last node?
        if len(self) == 0:
            self._tail = None
        else:
            self._head._prev = None
        return item

    def remove_last(self):
        'removes and returns last item'
        if len(self) == 0:
            raise RuntimeError("cannot remove from empty dll")

        # dictionary
        del self._nodes[self._tail.item]

        # extract item for later
        item = self._tail.item

        # move up tail pointer
        self._tail = self._tail._prev
        self._len -= 1

        # was that the last node?
        if len(self) == 0:
            self._head = None

        else:
            self._tail._next = None

        return item

    '''Function that returns true or false if item is within dictionary (ie: self._nodes)'''

    def __contains__(self, item):
        return True if item in self._nodes else False

    '''Outputs the neighers (bef:aft) of a specific item in index'''
    def neighbors(self, item):
        if self._nodes[item] == self._head:
            return (None, self._head._next.item)
        if self._nodes[item] == self._tail:
            return (self._tail._prev.item, None)
        else:
            bef = self._nodes[item]._prev.item
            aft = self._nodes[item]._next.item
            return (bef, aft)


    '''Removes the node from the list (changes the location arrow of prev and next)'''
    def remove_node(self, item):
        
        if self._nodes[item]._prev is not None:
            self._nodes[item]._prev._next = self._nodes[item]._next
        
        if self._nodes[item]._next is not None:
            self._nodes[item]._next._prev = self._nodes[item]._prev


        if self._nodes[item]._prev is None:
            self._head = self._nodes[item]._next
            self._head._prev = None
        if self._nodes[item]._next is None:
            self._tail = self._nodes[item]._prev
            self._tail._next = None
        if item not in self._nodes == None:
            raise RuntimeError()

        del self._nodes[item]
        return item
