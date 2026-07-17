class ATM:
    def __init__(self):
        self.bank="SBI"
        self.__pin=7534
    
    def get_pin(self):
        return self.__pin
    
    def verify_pin(self,pin):
        if pin==self.__pin:
            print("Access Granted")
        else:
            print("Access Denied")
    
    def set_changePin(self,old_pin,new_pin):
        if old_pin==self.__pin:

            if len(str(new_pin))==4:
                self.__pin=new_pin
                print("Your pin is updated")
            else:
                print("Pin should contain only 4 digits")

        else:
            print("Incorrect PIN")

atm=ATM()

print('\n')
atm.verify_pin(7534)
atm.set_changePin(7534,2353)

print('\n')

atm.verify_pin(4325)
atm.set_changePin(2353,77777)

print('\n')

atm.verify_pin(4325)
atm.set_changePin(7845,7777)