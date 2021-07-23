import user_interface
from customer import Customer
from soda_machine import SodaMachine
from backpack import Backpack


class Simulation:
    def __init__(self):
        # tbh i dont yet know why this is empty
        pass

    #@staticmethod # ? STATIC OR NOT - I MAY NEVER KNOW :(
    def run_simulation(self):
        """The central method called in main.py."""
        backpack = Backpack()
        customer = Customer()
        soda_machine = SodaMachine()
        will_proceed = True
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == 1:
                soda_machine.begin_transaction(customer)
            elif user_option == 2:
                customer.check_coins_in_wallet()
            elif user_option == 3:
                customer.check_backpack(backpack, backpack.purchased_cans)
            else:
                will_proceed = False
        
                
