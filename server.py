contratti = {
    "Vicolo Corto": {
      "class": None,
      "Prezzo": 150,
      "Rendite": [ 5, 25, 75, 225, 400, 625 ],
      "Costo": 125
    },
    "Vicolo Stretto": {
      "class": None,
      "Prezzo": 150,
      "Rendite": [ 10, 50, 150, 450, 800 ],
      "Costo": 125
    },
    "Bastioni Gran Sasso": {
      "class": None,
      "Prezzo": 250,
      "Rendite": [ 15, 75, 225, 675, 100, 1375 ],
      "Costo": 125
    },
    "Viale Monterosa": {
      "class": None,
      "Prezzo": 250,
      "Rendite": [ 15, 75, 225, 675, 100, 1375 ],
      "Costo": 125
    },
    "Viale Vesuvio": {
      "class": None,
      "Prezzo": 300,
      "Rendite": [ 20, 100, 250, 750, 1125, 1500 ],
      "Costo": 125
    },
    "Via Accademia": {
      "class": None,
      "Prezzo": 350,
      "Rendite": [ 23, 125, 375, 1125, 1550, 1875 ],
      "Costo": 250
    },
    "Corso Ateneo": {
      "class": None,
      "Prezzo": 350,
      "Rendite": [ 23, 125, 375, 1125, 1550, 1875 ],
      "Costo": 250
    },
    "Piazza Università": {
      "class": None,
      "Prezzo": 400,
      "Rendite": [ 30, 150, 450, 1250, 1750, 2250 ],
      "Costo": 250
    },
    "Via Verdi": {
      "class": None,
      "Prezzo": 450,
      "Rendite": [ 35, 175, 500, 1375, 1875, 2375 ],
      "Costo": 250
    },
    "Corso Raffaello": {
      "class": None,
      "Prezzo": 450,
      "Rendite": [ 35, 175, 500, 1375, 1875, 2375 ],
      "Costo": 250
    },
    "Piazza Dante": {
      "class": None,
      "Prezzo": 500,
      "Rendite": [ 40, 200, 550, 1500, 2000, 2500 ],
      "Costo": 250
    },
    "Via Marco Polo": {
      "class": None,
      "Prezzo": 550,
      "Rendite": [ 45, 225, 625, 1750, 2200, 2625 ],
      "Costo": 375
    },
    "Corso Magellano": {
      "class": None,
      "Prezzo": 550,
      "Rendite": [ 45, 225, 625, 1750, 2200, 2625 ],
      "Costo": 375
    },
    "Largo Colombo": {
      "class": None,
      "Prezzo": 600,
      "Rendite": [ 50, 250, 750, 1875, 2250, 2750 ],
      "Costo": 375
    },
    "Viale Costantino": {
      "class": None,
      "Prezzo": 650,
      "Rendite": [ 55, 275, 825, 2000, 2500, 3000 ],
      "Costo": 375
    },
    "Viale Traiano": {
      "class": None,
      "Prezzo": 650,
      "Rendite": [ 55, 275, 825, 2000, 2500, 3000 ],
      "Costo": 375
    },
    "Piazza Giulio Cesare": {
      "class": None,
      "Prezzo": 700,
      "Rendite": [ 60, 300, 900, 2125, 2625, 3125 ],
      "Costo": 375
    },
    "Via Roma": {
      "class": None,
      "Prezzo": 750,
      "Rendite": [ 65, 325, 1000, 2250, 2750, 3250 ],
      "Costo": 500
    },
    "Corso Impero": {
      "class": None,
      "Prezzo": 750,
      "Rendite": [ 65, 325, 1000, 2250, 2750, 3250 ],
      "Costo": 500
    },
    "Largo Augusto": {
      "class": None,
      "Prezzo": 800,
      "Rendite": [ 70, 375, 1125, 2500, 3000, 3500 ],
      "Costo": 500
    },
    "Viale dei Giardini": {
      "class": None,
      "Prezzo": 875,
      "Rendite": [ 90, 500, 1250, 2750, 3250, 3750 ],
      "Costo": 500
    },
    "Parco della Vittoria": {
      "class": None,
      "Prezzo": 1000,
      "Rendite": [ 125, 500, 1500, 3500, 4250, 5000 ],
      "Costo": 500
    }
  }

class player:
	def __init__(self, n):
		self.name = n
		self.money = 200
	def bid(self, current):
		if current>self.money:
			print("{} does not have enough money".format(self.name))
			return 0
		self.offer = int(input("{}, place your offer (currently {}): ".format(self.name, current)))
		while self.offer <= current and self.offer != 0:
			self.offer = int(input("{}, you have to bid more than {}: ".format(self.name, current)))
		if self.offer >= self.money:
			print("Not enough money")
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
	def __init__(self, name, price, revenues, cost, houses=0, owner=None):
		self.name = name
		self.owner = owner
		self.houses_num = houses
		self.revenues = revenues[:]
		self.price = price
		self.cost = cost
	def auction(self, passing):
		print("Auctioning for {}".format(self.name))
		if passing.bid(self.price) == self.price:
				passing.pay(self.price)
				self.owner = passing
				print("{} is now the owner of {}".format(self.owner.name, self.name))
		else:
			self.bidders = players[:]
			self.current = self.price/2
			if self.current%5 != 0:
				self.current = 5*(self.current//5)+5
			self.orig = self.current
			while len(self.bidders) > 1:
				for e in self.bidders:
					self.offer = e.bid(self.current)
					if self.offer > self.current:
						self.current = self.offer
					else:
						self.bidders.remove(e)
						print("{} removed from auction".format(e.name))
			if self.orig == self.current:
				self.offer = self.bidders[0].bid(self.current)
				if self.offer > self.current:
					self.bidders[0].pay(self.current)
					self.owner = self.bidders[0]
					print("{} bought {}".format(self.bidders[0].name, self.name))
				else:
					print("The contract remains unsold")
			else:
				self.bidders[0].pay(self.current)
				self.owner = self.bidders[0]
				print("{} bought {}".format(self.bidders[0].name, self.name))
	def onPass(self, passing):
		print ("{} stepped on {}".format(passing.name, self.name))
		if not self.owner:
			self.auction(passing)
		elif passing == self.owner:
			print("{} is the owner of {}, he's not gonna pay".format(passing.name, self.name))
		else:
			#cost da calcolare in base alle case
			print("{} is not the owner of {}, he's gonna pay".format(passing.name, self.name))
			self.payed = passing.pay(self.revenues[self.houses_num])
			if self.payed == self.revenues[self.houses_num]:
				self.owner.receive(self.fee)
			elif self.payed == 0:
				print("{} doesn't have enough money".format(passing.name))

# First step is to create an instance for every property owned by the Bank
# Then every player will get his money and contracts
init = ["Ciccio", "Banca", "Zietto"]
players = []
for e in init:
	players.append(player(e))
for e in contratti:
	contratti[e]["class"] = property(e, contratti[e]["Prezzo"], contratti[e]["Rendite"], contratti[e]["Costo"])