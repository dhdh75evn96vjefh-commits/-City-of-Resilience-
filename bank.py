class Bank:
    def __init__(self, initial_money):
        self.money = initial_money
        self.loans = []
    def add_money(self, amount):
        self.money += amount
    def subtract_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        return False
    def take_loan(self, amount):
        self.money += amount
        self.loans.append({"rem": amount * 1.2})
    def pay_loans(self):
        paid = 0
        for l in self.loans:
            p = min(l["rem"], self.money * 0.1)
            if self.subtract_money(p):
                l["rem"] -= p
                paid += p
        self.loans = [l for l in self.loans if l["rem"] > 0]
        return paid
