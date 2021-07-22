import coins


class Wallet:
    def __init__(self):
        # super().__init__(self)
        self.money = []
        self.fill_wallet()

    def fill_wallet(self):
        # TODO: """Method will fill wallet's money list with certain amount of each type of coin when called."""
        for index in range(1): # 8
            self.money.append(coins.Quarter())
        for index in range(1): # 10
            self.money.append(coins.Dime())
        for index in range(1): # 20
            self.money.append(coins.Nickel())
        for index in range(1): # 50
            self.money.append(coins.Penny())
