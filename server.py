print("Hello\n")

class player:
	def __init__(self, n):
		self.name = n
		self.money = 3000
	def pay(self, amount):
		if self.money-amount >= 0:
			self.money-=amount
			print("{} payed {}. Now he's got {}€".format(self.name, amount, self.money))
			return amount
		else:
			return 0
	def receive(self, amount):
		self.money+=amount
		print("{} received {}€, now he's got {}€".format(self.name, amount, self.money))
class property:
	# We will need name, owner=bank, amount, house cost and fee and hotel cost and fee
	def __init__(self, name, owner):
		self.name = name
		self.owner = owner
		self.houses = 0
		self.hotels = 0
		self.amount = 50
	def onPass(self, passing):
		print ("{} stepped on {}".format(passing.name, self.name))
		if passing.name != self.owner.name:
			#amount da calcolare in base alle case
			print("{} is not the owner of {}, he's gonna pay".format(passing.name, self.name))
			if passing.pay(self.amount) == self.amount:
				self.owner.receive(self.amount)
		else:
			print("{} is the owner of {}, he's not gonna pay".format(passing.name, self.name))

ciccio = player("ciccio")
bank = player("bank")
vicolo = property("Vicolo stretto", bank)
print("Inizializzate le tre classi\n")
vicolo.onPass(ciccio)