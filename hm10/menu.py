from waitlist import Waitlist
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def validate_hour(self,hour):
        '''validate the hour input'''
        if not isinstance(hour, int) or hour < 00 or hour > 23:
            return False
        return True
    
    def validate_min(self,minute):
        '''validate the minute'''
        if not isinstance(minute, int) or minute < 00 or minute > 59:
            return False
        return True
    
    def validate_length(self, time):
        '''validates the length of time'''
        if len(time) != 5:
            return False
        return True
    
    def validate_time(self, time):
        '''checks if time input is correct'''
        while True:
            try:
                L = time.split(':')
                hour, minute = int(L[0]), int(L[1])
                if not self.validate_hour(hour) or not self.validate_min(minute) or not self.validate_length(time):
                    return False
                else:
                    return time
                
            except ValueError:
                print('Invalid format: Enter Again ')
                time = input()
                continue

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:
            
            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                #TODO """Add a customer to the waitlist"""
                name = input("Input Name:")
                time = input('Input time as HH:MM: ')
                newtime = self.validate_time(time)

                while newtime == False:
                    time = input("Invalid, New Input: ")
                    newtime = self.validate_time(time)

                self.waitlist.add_customer(name,newtime)

            elif choice == "2":
                #TODO"""Seat the next customer"""
                print(self.waitlist.seat_customer())
                
            elif choice == "3":
                #TODO"""Change the time of a customer's reservation"""
                name = input("Input Name:")
                time = input('Input new time as HH:MM: ')
                newtime = self.validate_time(time)
                while newtime == False:
                    time = input("Invalid, New Input: ")
                    newtime = self.validate_time(time)

                self.waitlist.change_reservation(name, newtime)
            
            elif choice == "4":
                #TODO"""Peek at the next customer"""
                next_customer = self.waitlist.peek()
                # a = next_customer
                # self.validate_time(a)
                if next_customer is None:
                    print("Empty waitlist")
                else:
                    print("Next customer6:", next_customer)

            elif choice == "5":
                #TODO"""Print the waitlist"""
                print(self.waitlist.print_reservation_list())
                
            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")
    
s = Menu()
s.run()

