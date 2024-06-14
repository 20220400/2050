import random
class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time
    
class Waitlist:
    def __init__(self):
        self.heap = Heap()

    def add_customer(self, item, priority = None):
        '''adds customers to the waiting list'''
        self.heap._entries.append(Entry(item, priority))
        self.heap._upheap(len(self.heap._entries) - 1)

    def peek(self):
        '''peeks and sees the first customer in the waitlist'''
        if len(self.heap._entries) == 0:
            return None
        else:
            return (self.heap._entries[0].name, self.heap._entries[0].time)
        
    def seat_customer(self):
        '''extracts the customer with the highest priority'''
        L = self.heap._entries
        if not L:
            return None
        customer = L[0]
        L[0] = L[-1]
        L.pop()
        if L:
            self.heap._downheap(0)

        return (customer.name, customer.time)

    def print_reservation_list(self):
        '''print reservation list'''
        reservation_lst = []
        L = Waitlist()
        L.heap._entries = self.heap._entries.copy()

        while len(L.heap._entries) > 0:
            max = L.seat_customer()
            reservation_lst.append((max[0],max[1]))
        return reservation_lst
    
    def change_reservation(self, name, new_time):
        '''changes the reservation time for the customer with the given name'''
        for i in range(len(self.heap._entries)):
            if self.heap._entries[i].name == name:
                self.heap._entries[i].time = new_time
                if new_time < self.heap._entries[self.heap._parent(i)].time:
                    self.heap._upheap(i)
                else:
                    self.heap._downheap(i)
                break

class Heap:
    '''A class that contains heap methods and helper functions'''
    def __init__(self):
        self._entries = []
    def _parent(self, i):
        '''returns the parent of the heap(i)'''
        return (i - 1) // 2
    
    def _children(self, i):
        '''returns the children of heap(i)'''
        left = 2 * i + 1
        right = 2 * i + 2
        return range(left, min(len(self._entries), right + 1)) 
    
    def _swap(self, a, b):
        '''swaps list positions from self._entries'''
        L = self._entries
        L[a], L[b] = L[b], L[a]

    def _upheap(self, i):
        '''maintains the min-heap property upwards'''
        L = self._entries
        parent = self._parent(i)
        if 0 <= i < len(L):
            parent = self._parent(i)
            if i > 0 and L[i] < L[parent]:
                self._swap(i, parent)
                self._upheap(parent)

    def _downheap(self, i):
        '''maintains the min-heap property downwards'''
        L = self._entries
        children = self._children(i)
        if children:
            child = min(children, key = lambda x: L[x])
            if L[child] < L[i]:
                    self._swap(i, child)
                    self._downheap(child)

    def _pop(self):
        '''removes and returns the smallest item from the heap'''
        L = self._entries
        last_elem_index = len(L) - 1
        self._swap(0, last_elem_index)
        smallest = L.pop()
        self._downheap(0)
        return smallest