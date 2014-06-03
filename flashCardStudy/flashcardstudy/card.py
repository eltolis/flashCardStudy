class Card(object):

	def __init__(self, id):
		self.id = id
		content = []

class Helpers(object):

	def adding(self):

		finished = False
		card_count = 1
		cards = [] 
		#cards = {}

		while finished == False:
			new_card = []
			#new_card = {}
			print "Card: %d" % card_count
			card_id = card_count
			side1 = raw_input("Side one: ")
			side2 = raw_input("Side two: ")
			new_card = [card_id, side1, side2]
			cards.append(new_card)
			#new_card[card_id] = [side1, side2]
			#cards.update(new_card)

			finished_prompt = raw_input("Press RETURN to add another card, type F to finish.")

			if finished_prompt.lower() == 'f':
				finished == True
				return cards 
			else:
				card_count += 1

requests = Helpers()

def add_card():
	cards = requests.adding()
	return cards
