print("Hello\n")

class player:
	def __init__(self, n):
		self.name = n
		self.money = 200
	def bid(self, name, current):
		self.offer = int(input("{}, would you buy {} for {}? ".format(self.name, name, current+1)))
		if self.offer >= self.money or self.offer <= current:
			print("Not enough money. You are excluded from the auction")
			return 0
		else:
			return self.offer
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
	# We will need name, owner=bank, cost, house fee and hotel fee, cost
	def __init__(self, name, owner=None):
		self.name = name
		self.owner = owner
		self.houses = 0
		self.hotels = 0
		self.fee = 50
		self.cost = 50
	def onPass(self, passing):
		print ("{} stepped on {}".format(passing.name, self.name))
		if not self.owner:
			if passing.bid(self.name, self.cost-1) == self.cost:
				passing.pay(self.cost)
				self.owner = passing
				print("{} is now the owner of {}".format(self.owner.name, self.name))
			else:
				self.bidders = players
				self.current = self.cost/2
				while len(self.bidders) > 1:
					for e in self.bidders:
						self.offer = e.bid(self.name, self.current-1)
						if self.offer > self.current:
							self.current = self.offer
						else:
							self.bidders.remove(e)
				self.bidders[0].pay(self.current)
				self.owner = self.bidders[0]
		elif passing == self.owner:
			print("{} is the owner of {}, he's not gonna pay".format(passing.name, self.name))
		else:
			#cost da calcolare in base alle case
			print("{} is not the owner of {}, he's gonna pay".format(passing.name, self.name))
			self.payed = passing.pay(self.fee)
			if self.payed == self.fee:
				self.owner.receive(self.fee)
			elif self.payed == 0:
				print("{} doesn't have enough money".format(passing.name))

# First step is to create an instance for every property owned by the Bank
# Then every player will get his money and contracts
init = ["Ciccio", "Banca", "Zietto"]
players = []
for e in init:
	players.append(player(e))
vicolo = property("Vicolo stretto")
print("Inizializzate le tre classi\n")
vicolo.onPass(players[0])