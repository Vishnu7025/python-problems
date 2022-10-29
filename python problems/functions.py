# def sample(*name):
#     print("hello world",*name)

# sample("vishnu","manu")


class sampleclass:
    def hello(self):
        print("hello")

x=sampleclass()
x.hello()


# class Account:
#     def __init__(self,account_number,account_balance) :
#         self.account_number = account_number
#         self.account_balance =  account_balance

#     def withdraw(self,amount):
#         if self.account_balance - amount > 0 :
#             self.account_balance = self.account_balance - amount
#         else:
#             print("Withdrawal failed")

#     def deposit(self,deposit):
#         self.deposit=deposit

#     def display(self):
#         print("your {} balance {}".format(self.account_number,self.account_balance))

# account_one = Account('A23jfj',5000)
# account_two = Account('Sjdsdsf',500)
# account_two.withdraw(600)


# base = int(input("Enter a num : "))
# exponent = int(input("Enter expo : "))
# result = 1
# while exponent != 0:
#     result *= base
#     exponent-=1

# print("Anwer {}".format(result))