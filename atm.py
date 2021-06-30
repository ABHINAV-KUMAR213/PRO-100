class Atm(object):

    def __init__(self,card_number,pin_number):
         self.card_number = card_number
         self.pin_number = pin_number

    def CashWithdrawl(self,cash_withdraw):
        print("You have successfully withdrawed RS",cash_withdraw)

    def BalanceEnquiry(self,balance_enquiry):
        print("You balance : ",balance_enquiry)


Abhinav = Atm("3908","3112")
print(Abhinav.card_number)
print(Abhinav.pin_number)
Abhinav.CashWithdrawl(500)
Abhinav.BalanceEnquiry(50000)
