class Atm(object):
    def __init__(self, cardNumber, pinNumber, bankName):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.bankName = bankName

    def CashWithdrawl(self):
        print('Cash withdrawl success!')

    def CashDeposit(self):
        print('Cash deposit success!')
