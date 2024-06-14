
class Graph:
    def __init__(self, V=(), E=()):
        """Initialized the edge cases as well as the"""
        self._V = set()
        self.E = dict()
        self._nbrs = {}
        for v in V: self.add_vertex(v)
        for e in E: self.add_edge(*e, E[e]) 

    def __len__(self):
        '''returns the len of the Vertices'''
        return len(self._V)

    def add_vertex(self, v):
        """Adds a vertex"""
        self._V.add(v)
        self._nbrs[v] = set()

    def remove_vertex(self, v):
        """Removes a vertex"""
        self._V.remove(v)
        self._nbrs[v] = set()
        del self._nbrs[v]

    def add_edge(self, u, v, wt):
        """ADDs and edge"""
        if u not in self._V:
            self._V.add(u)
            self._nbrs[u] = set()
        if v not in self._V:
            self._V.add(v)
            self._nbrs[v] = set()
        self.E[(u, v)] = wt
        self.E[(v, u)] = wt
        self._nbrs[u].add(v)
        self._nbrs[v].add(u)
        
    def remove_edge(self, u, v, wt):
        """removes and edge"""
        del self.E[(u, v)]
        del self.E[(v, u)]
        self._nbrs[u].remove(v)
        self._nbrs[v].remove(u)

    def nbrs(self, v):
        """Displays a neighbors of vertices"""
        return iter(self._nbrs[v])
    
    def __iter__(self):
        '''iterates the vertex'''
        return iter(self._V)

    def fewest_flights(self, city):
        '''bfs: finds how to get from city to any other city in the graph with the fewest number of flights'''
        
        tree = {}
        tovisit = Queue()
        tovisit.enqueue((None, city))
        flight_amt = {}
        flight_amt[city] = 0
        while not tovisit.is_empty():
            item = tovisit.dequeue()
            if item is None:
                continue
            a, b = item
            if b not in tree:
                tree[b] = a
                if a is not None:
                    flight_amt[b] = flight_amt[a] + 1

                for n in self.nbrs(b):
                    tovisit.enqueue((b,n))
        return tree, flight_amt
                    
    def shortest_path(self, city):
        '''Dykstra: - finds how to get from city to any other city in the graph with the fewest number of miles travelled'''
        
        distance = {u: float('inf') for u in self._V}
        distance[city] = 0
        prev = {u: None for u in self._V}

        heap = Heap()
        heap._entries.append((0, city))

        while heap._entries:
            d, u = heap._pop()
            if distance[u] < d:
                continue

            for w in self.nbrs(u):
                alt_dist = distance[u] + self.E[(u, w)]
                if alt_dist < distance[w]:
                    distance[w] = alt_dist
                    prev[w] = u
                    heap._entries.append((alt_dist, w))
                    heap._upheap(len(heap._entries) - 1)

        return distance, prev

    def minimum_salt(self,city):
        '''Uses Prim: connects city to o every other city in the graph with the fewest total number of miles '''
        v = city
        tree = {}
        dist = {u: float('inf') for u in self._V}
        dist[v] = 0
        tovisit = Heap()
        tovisit.insert((None,v), 0)
        while len(tovisit) > 0:
            a, b = tovisit.removemin()
            if b not in tree:
                tree[b] = a
                for n in self._nbrs[b]:
                    for i in n:
                        tovisit.insert((b,n), i)
            if len(tree) == len(self._V):
                break

        for i in tree:
            if tree[i] is not None:
                dist[i] = self.E[(i, tree[i])]
        result = {'dist': dist, 'tree': tree}
        return result
    
class Queue:
    def __init__(self):
        self._head = 0
        self._L = []

    def enqueue(self, item):
        return self._L.append(item)

    def dequeue(self):
        if not self._L:
            return None
        item = self._L[self._head]
        self._head +=1
        if self._head > len(self._L)//2:
            self._L = self._L[self._head:]
            self._head = 0
        return item
    
    def is_empty(self):
        return self._head == len(self._L)
    
class Entry:
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

    def removemin(self):
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._downheap

    def __lt__(self, other):
        return self.priority < other.priority

class Heap:
    '''A class that contains heap methods and helper functions'''
    def __init__(self):
        self._entries = []
        
    def insert(self, item, priority):
        self._entries.append(Entry(item, priority))
        self._upheap(len(self._entries)-1)

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
    
    def removemin(self):
        L = self._entries
        item = L[0].item
        L[0] = L[-1]
        L.pop()
        self._downheap
        return item
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self) > 0:
            return self.removemin()
        else:
            raise StopIteration
        
    def __len__(self):
        return len(self._entries)
    
    

