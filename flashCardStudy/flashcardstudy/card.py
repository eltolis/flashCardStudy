from prettytable import PrettyTable

class Card(object):

	def __init__(self, id):
		self.id = id
		content = []

class Helpers(object):

	def adding(self):

		finished = False
		card_count = 1
		cards = [] 

		while finished == False:
			new_card = []
			print "Card: %d" % card_count
			card_id = card_count
			side1 = raw_input("Side one: ")
			side2 = raw_input("Side two: ")
			new_card = [card_id, side1, side2]
			cards.append(new_card)

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

def list_card_contents(files):
	from stack import read_stack_files
	contents = read_stack_files(files)

	table = PrettyTable(["Card ID", "Side 1", "Side 2"])
	table.align["Side1"] = 'l'
	table.align["Side2"] = 'l'

	cards = [stack[2] for stack in contents]

	for card in cards[0]:
		side1 = (card[1][:40] + '...') if len(card[1]) > 40 else card[1]
		side2 = (card[2][:40] + '...') if len(card[2]) > 40 else card[2]
		table.add_row([card[0],side1, side2])

	print "\nStack name: %s" % stack[1]
	print table.get_string(sortby="Card ID")
