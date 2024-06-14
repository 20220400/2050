import unittest
from waitlist import Waitlist

class test_waitlist(unittest.TestCase):
    
    def test_add_customer(self):
        '''test add_customer function'''
        waitlist = Waitlist()
        waitlist.add_customer("Bloom", 3)
        self.assertEqual(waitlist.heap._entries[0].name, 'Bloom')
        self.assertEqual(waitlist.heap._entries[0].time, 3)
        
    def test_peek(self):
        '''test add_peek function'''
        waitlist = Waitlist()
        self.assertIsNone(waitlist.peek())
        waitlist.add_customer("Stella", "10:45")
        waitlist.add_customer("Bloom", "11:45")
        waitlist.add_customer("Techna", "12:45")

        #check output
        self.assertEqual(waitlist.peek(), ("Stella", "10:45"))

        #Removes a customer and check again
        waitlist.seat_customer()
        self.assertEqual(waitlist.peek(),("Bloom", "11:45"))

        waitlist.seat_customer()
        waitlist.seat_customer()
        self.assertIsNone(waitlist.peek())
    
    def test_seat_customer(self):
        '''test seat_customer function'''
        waitlist = Waitlist()

          # add some customers to the waitlist
        waitlist.add_customer("Stella", "09:45")
        waitlist.add_customer("Techna", "10:15")
        waitlist.add_customer("Flora", "09:55")
        waitlist.add_customer("Aisha", "09:55")

        # call seat_customer 
        customer, time = waitlist.seat_customer()
        self.assertEqual(customer, "Stella")
        self.assertEqual(time, "09:45")

        # add more customers 
        waitlist.add_customer("Bloom", "09:15")
        waitlist.add_customer("Musa", "10:45")
        customer, time = waitlist.seat_customer()
        self.assertEqual(customer, "Bloom")
        self.assertEqual(time, "09:15")

        # Test customer with the same time
        waitlist.add_customer("Luna", "10:00")
        customer, time = waitlist.seat_customer()
        self.assertEqual(customer, 'Aisha')
        self.assertEqual(time, '09:55')

    def test_print_reservation_list(self):
        '''Test the print_reservation list function'''
        
    # Initialize waitlist with some reservations
        waitlist = Waitlist()
        waitlist.add_customer('Stella', '10:00')
        waitlist.add_customer('Musa', '11:00')
        waitlist.add_customer('Bloom', '12:00')
        waitlist.add_customer('Techna', '09:00')

        # Test printing reservation list
        expected_output = [('Techna', '09:00'), ('Stella', '10:00'), ('Musa', '11:00'), ('Bloom', '12:00')]
        self.assertEqual(waitlist.print_reservation_list(), expected_output)

        # Test after Reservation change
        waitlist.change_reservation('Musa', '08:30')
        expected_output = [('Musa', '08:30'),('Techna', '09:00'),('Stella', '10:00'), ('Bloom', '12:00')]
        self.assertEqual(waitlist.print_reservation_list(), expected_output)

        # Test after seat customer
        waitlist.seat_customer()
        expected_output = [('Techna', '09:00'),('Stella', '10:00'), ('Bloom', '12:00')]
        self.assertEqual(waitlist.print_reservation_list(), expected_output)

    def test_change_reservation(self):
        '''Test the change_reservation function'''

        # Initialize waitlist with some reservations
        waitlist = Waitlist()
        waitlist.add_customer('Stella', '10:00')
        waitlist.add_customer('Musa', '11:00')
        waitlist.add_customer('Bloom', '12:00')

        # Change reservation for existing customer
        waitlist.change_reservation('Musa', '10:30')
        expected_output = [('Stella', '10:00'), ('Musa', '10:30'), ('Bloom', '12:00')]
        self.assertEqual(waitlist.print_reservation_list(), expected_output)

        # Change reservation to an earlier time
        waitlist.change_reservation('Bloom', '11:00')
        expected_output = [('Stella', '10:00'), ('Musa', '10:30'), ('Bloom', '11:00')]
        self.assertEqual(waitlist.print_reservation_list(), expected_output)

        # Change reservation to a later time
        waitlist.change_reservation('Stella', '12:30')
        expected_output = [('Musa', '10:30'), ('Bloom', '11:00'), ('Stella', '12:30')]
        self.assertEqual(waitlist.print_reservation_list(), expected_output)
        
if __name__ == '__main__':
    unittest.main()
