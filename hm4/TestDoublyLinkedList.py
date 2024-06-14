from DoublyLinkedList import DoublyLinkedList as DLL
import unittest

# Basic tests are provided for you, but you need to implement the last 3 unittests
class testDLL(unittest.TestCase):
    def test_addfirst_removefirst(self):
        'adds items to front, then removes from front'
        dll = DLL()
        n = 100

        for j in range(5):  # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_first()

    def test_addlast_removelast(self):
        'adds items to end, then removes from end'
        dll = DLL()
        n = 100

        for j in range(5):  # repeat a few times to make sure removing last item doesn't break anything
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), n-1-i)

            with self.assertRaises(RuntimeError):
                dll.remove_last()

    def test_add_remove_mix(self):
        'various add/remove patterns'
        dll = DLL()
        n = 100

        # addfirst/removelast
        # repeat a few times to make sure removing final node doesn't break anything
        for j in range(5):
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_first(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_last(), i)

        # addlast/removefirst
        # repeat a few times to make sure removing final node doesn't break anything
        for j in range(5):
            for i in range(n):
                self.assertEqual(len(dll), i)
                dll.add_last(i)

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                self.assertEqual(dll.remove_first(), i)

        # mix of first/last
        # repeat a few times to make sure removing final node doesn't break anything
        for j in range(5):
            for i in range(n):
                self.assertEqual(len(dll), i)
                if i % 2:
                    dll.add_last(i)  # odd numbers - add last
                else:
                    dll.add_first(i)  # even numbers - add first

            for i in range(n):
                self.assertEqual(len(dll), n-i)
                if i % 2:
                    # odd numbers: remove last
                    self.assertEqual(dll.remove_last(), n-i)
                else:
                    # even numbers: remove first
                    self.assertEqual(dll.remove_first(), n-2-i)

    # TODO: Add docstrings to and implement the unittests below
    '''Tests if Dll contains numbers within a list'''

    def test_contains(self):
        dll = DLL(range(9))
        emptydll = DLL()
        self.assertEqual(10 in dll, False)
        self.assertEqual(5 in dll, True)
        dll.remove_last()
        dll.remove_first()
        dll.add_first(12)
        self.assertEqual(12 in dll, True)
        self.assertEqual(8 in dll, False)
        self.assertEqual(5 in emptydll, False)

    '''Tests to see if function neighbors has the correct output'''
    def test_neighbors(self):
        dll = DLL(range(5))
        dll_two = DLL(range(2))
        emptydll = DLL()

        self.assertEquals(dll.neighbors(2), (1, 3))
        self.assertNotEquals(emptydll.neighbors, (1, 3))
        self.assertEquals(dll.neighbors(0),(None,1))
        self.assertEquals(dll.neighbors(5),(4,None))
        # Check more cases
        # check to see if none of either side

    def test_remove_item(self):
        dll = DLL(range(4))
        emptydll = DLL()
        dll_two = DLL(range(2))
        self.assertEquals(dll.remove_node(2),2)
        self.assertEquals(dll.neighbors(1),(0, 3))
        self.assertNotEquals(emptydll.remove_node(0), 0)

unittest.main()
