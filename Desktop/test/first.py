
#1

# filename = "air.txt"


# with open(filename) as file:
# 	text = file.read()
# text = text.replace("\n", "")
# text = "".join(text)
# text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace(" ", "")
# words = list(text.lower())


# words_dict = dict()
# for word in words:
#     if word in words_dict:
#         words_dict[word] = words_dict[word] + 1
#     else:
#         words_dict[word] = 1

# print(words_dict)
# finale = words_dict.values()
# max_letters = max(finale)
# finalll = {k:v for k,v in words_dict.items() if v == max_letters}
# for k,v in finalll.items():
# 	print(f"Max letters is\nletter: {k}\nnumber: {v}")





#2
# class CoffeeMachine:
# 	def __init__(self, milk,coffee,sugar):
# 		self.milk = milk
# 		self.coffee = coffee
# 		self.sugar = sugar

# 	def make_coffee(self,milk,coffee,sugar):
# 			if milk > self.milk and coffee > self.coffee and sugar > self.sugar:
# 				res = milk - self.milk
# 				res2 = coffee - self.coffee
# 				res3 = sugar - self.sugar
# 				print(f"There is not enough everything\nmilk-{res}\ncoffee-{res2}\nsugar-{res3}")


# 			elif milk > self.milk and coffee > self.coffee and sugar < self.sugar:
# 				res = milk - self.milk
# 				res2 = coffee - self.coffee
# 				print(f"There is not enough milk-{res} and coffee-{res2}")

# 			elif milk > self.milk and coffee < self.coffee and sugar > self.sugar:
# 				res = milk - self.milk
# 				res2 = coffee - self.coffee
# 				print(f"There is not enough milk-{res} and sugar-{res2}")

# 			elif milk < self.milk and coffee > self.coffee and sugar > self.sugar:
# 				res = sugar - self.sugar
# 				res2 = coffee - self.coffee
# 				print(f"There is not enough coffee-{coffee} and sugar-{sugar}")

# 			elif milk > self.milk and coffee < self.coffee and sugar < self.sugar:
# 				res = milk - self.milk
# 				print(f"There is not enough milk-{res}")

# 			elif milk < self.milk and coffee > self.coffee and sugar < self.sugar:
# 				res = coffee - self.coffee
# 				print(f"There is not enough coffee-{res}")

# 			elif milk < self.milk and coffee < self.coffee and sugar > self.sugar:
# 				res = sugar - self.sugar	
# 				print(f"There is not enough sugar-{res}")

# 			elif milk < self.milk and coffee < self.coffee and sugar < self.sugar:
# 				self.__substract_milk(milk)
# 				self.__substract_coffee(coffee)
# 				self.__subtsract_sugar(sugar)
# 				print(f"Coffee is done\nmilk-{self.milk}\ncoffee-{self.coffee}\nsugar{self.sugar}")

# 	def __substract_milk(self,milk):
# 		self.milk -= milk	
# 	def __substract_coffee(self,coffee):
# 		self.coffee -= coffee

# 	def __subtsract_sugar(self,sugar):
# 		self.sugar -= sugar


# def main():
# 	coffemachine = CoffeeMachine(1000,1000,1000)
# 	coffemachine.make_coffee(123,132,400)
# if __name__ == "__main__":
# 	main()



