from Graph import Graph, Queue, Heap
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        '''makes the diagram'''

        f'''
        FRANKLIN-----(500ml)---LISBON
          |  \              /   |
                        
          |    \           /    |

   (75 ml)|    (35ml)   (45ml)  | (85 ml)
                                                  
          |      \       /      |

          |        \   /        |
              
          | 
                    DUBAI       |
                   
          |                     |
         NARNIA              TOKYO
        -----------  55ml   ------------ 
        '''

        self._V = ['NARNIA', 'DUBAI', 'FRANKLIN', 'LISBON', 'TOKYO']
        self.E= {('FRANKLIN', 'NARNIA'): 75, 
                 ('FRANKLIN', 'DUBAI'): 35,
                 ('DUBAI', 'LISBON'): 45,
                 ('LISBON', 'TOKYO'): 85,
                 ('TOKYO', 'NARNIA'): 55,
                 ('FRANKLIN', 'LISBON'): 500

        }
        self.g = Graph(self._V, self.E)

    # TODO: Add unittests for public interface of Graph class (except traversal algs)

    def test_add_vertex(self):
        '''tests the add vertex'''
        self.g.add_vertex(2)
        self.assertEqual(len(self.g), 6)
        self.g.add_vertex('PARIS')
        self.assertIn('PARIS', self.g._V)
        self.assertEqual(len(self.g), 7)

    def test_remove_vertex(self):
        '''test the remove vertex'''
        self.g.remove_vertex("FRANKLIN")
        self.assertEqual(len(self.g), 4)
        self.assertNotIn('FRANKLIN', self.g._V)
        self.assertNotIn('FRANKLIN', self.g._nbrs.keys())

    def test_remove_edge(self):
        '''test the remove edge'''
        self.g.add_edge('FRANKLIN', 'NARNIA', 75)
        self.g.remove_edge('FRANKLIN', 'NARNIA', 75)
        self.assertFalse(('FRANKLIN', 'NARNIA') in self.g.E)
        self.assertFalse(('NARNIA', 'FRANKLIN') in self.g.E)

    def test_add_edge(self):
        """Tests adding an edge to the graph"""
        self.g.add_edge('PANAMA', 'VALLEY', 10)
        self.assertTrue(('PANAMA', 'VALLEY') in self.g.E)
        self.assertTrue(('VALLEY', 'PANAMA') in self.g.E)
        self.assertEqual(self.g.E[('PANAMA', 'VALLEY')], 10)
        self.assertEqual(self.g.E[('VALLEY', 'PANAMA')], 10)
        self.assertTrue('PANAMA' in self.g._nbrs['VALLEY'])
        self.assertTrue('VALLEY' in self.g._nbrs['PANAMA'])
    
    def test_nbrs(self):
        '''test the nbrs function'''
        x = self.g.nbrs('FRANKLIN')
        edges = set()
        edges.add('NARNIA')
        edges.add('LISBON')
        edges.add('DUBAI')
        x_list = set()
        for i in x:
            x_list.add(i)
        self.assertEqual(x_list, edges)
            
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        
        '''makes the diagram'''

        f'''
        FRANKLIN-----(500ml)---LISBON
          |  \              /   |
                        
          |    \           /    |

   (75 ml)|    (35ml)   (45ml)  | (85 ml)
                                                  
          |      \       /      |

          |        \   /        |
              
          | 
                    DUBAI       |
                   
          |                     |
         NARNIA              TOKYO
        -----------  55ml   ------------ 
        '''

        self._V = ['NARNIA', 'DUBAI', 'FRANKLIN', 'LISBON', 'TOKYO']
        self.E= {('FRANKLIN', 'NARNIA'): 75, 
                 ('FRANKLIN', 'DUBAI'): 35,
                 ('DUBAI', 'LISBON'): 45,
                 ('LISBON', 'TOKYO'): 85,
                 ('TOKYO', 'NARNIA'): 55,
                 ('FRANKLIN', 'LISBON'): 500
        }
        self.g = Graph(self._V, self.E)

    # TODO: Which alg do you use here, and why?
    # Alg: BFS
    # Why: This helps to find the minimum amount of stops
    def test_fewest_flights(self):
        """Tests the fewest flights function"""
        #tests that the amounts are correct for shortest distance for Franklin
        expected = {'NARNIA': None, 'FRANKLIN': 'NARNIA', 'DUBAI': 'FRANKLIN', 'LISBON': 'DUBAI', 'TOKYO': 'LISBON'}
        result, flight_amt = self.g.fewest_flights('NARNIA')
        self.assertEqual(flight_amt['NARNIA'], 0)
        self.assertEqual(flight_amt['FRANKLIN'], 1)
        self.assertEqual(flight_amt['DUBAI'], 2)
        self.assertEqual(flight_amt['LISBON'], 2)
        self.assertEqual(flight_amt['TOKYO'], 1)
    
    # TODO: Which alg do you use here, and why?
    # Alg:DYKSTRA
    # Why: In order to find the shortest path for each one. 

    def test_shortest_path(self):
        """Tests the shortests path function"""
        expected_distance = {'NARNIA': 75, 'DUBAI': 35, 'FRANKLIN': 0, 'LISBON': 80, 'TOKYO': 130}
        # Expected previous node in shortest path from FRANKLIN
        expected_prev = {'NARNIA': 'FRANKLIN', 'DUBAI': 'FRANKLIN', 'FRANKLIN': None, 'LISBON': 'FRANKLIN', 'TOKYO': 'LISBON'}

        # Test shortest path from FRANKLIN
        distance, prev = self.g.shortest_path('FRANKLIN')

        self.assertEqual(distance, expected_distance)

    # TODO: Which alg do you use here, and why?
    # Alg:PRIM
    # Why: Tries to find the least amount of edges which can be done through prim

    # def test_minimum_salt(self):
    #     expected_dist = {'NARNIA': 55, 'DUBAI': 35, 'FRANKLIN': 0, 'LISBON': 45, 'TOKYO': 85}
    #     expected_tree = {'NARNIA': ('FRANKLIN', 'NARNIA'), 'DUBAI': ('FRANKLIN', 'DUBAI'), 'FRANKLIN': None, 'LISBON': ('DUBAI', 'LISBON'), 'TOKYO': ('LISBON', 'TOKYO')}
    #     result = self.g.minimum_salt('FRANKLIN')
    #     self.assertEqual(result['dist'], expected_dist)
    #     self.assertEqual(result['tree'], expected_tree)

unittest.main()


