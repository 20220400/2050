import random
class Deck:
    def __init__(self, values = range (1,14), suits = ['clubs', 'diamonds', 'hearts', 'spades']):
        self.values = sorted(values)
        self.suits = sorted(suits)
        self.card_list = [Card(v, s) for v in self.values for s in self.suits]

    '''Returns the length of the deck'''
    def __len__(self):
        return len(self.card_list)

    '''Returns the sorted version of the deck'''
    def sort(self):
        s = self.card_list
        s.sort()
        print(s)
        
        #self.card_list = sorted(s)
      
    '''Returns the string of the card list'''
    def __repr__(self):
        # return f"Deck: {self.card_list}"
        return 'Deck: ' + str(self.card_list)

    '''Returns the shuffled version of the deck '''
    def shuffle(self):
        random.shuffle(self.card_list)

    ''' Returns the last card from the deck and removes the card'''
    def draw_top(self):
        # raise a runtime error if someone tries to draw from an empty deck 
        if len(self.card_list) == 0:
            raise RuntimeError('No cards in deck')
        else:
            return self.card_list.pop(-1)

class Hand(Deck):
    def __init__(self, card_list = []):
        self.card_list == card_list 

    '''Returns the string of the card list hand'''    
    def __repr__(self):
        return f"Hand: {self.card_list}"

    '''removes a card from the card list, runs a runtime error
    if not possible (not cards in deck)'''
    def play(self, play_card):
        # raise RuntimeError("cants draw from empty deck ")
        if play_card in self.card_list:
            # Remove the play_card from deck 
            self.card_list.remove(play_card)
            return play_card
        else:
            raise RuntimeError('Attempt to play Card {} that is not in Hand')


class Card:
    def __init__(self, values, suits):
        self.values = values
        self.suits = suits
    
    '''Return string value and string suit of a card'''
    def __repr__(self):
        return f"Card({self.values} of {self.suits})"
        #return "Card(" + str(self.values) + " of " + self.suits + ")"

    '''Checks to see if the both the values and suits are less than other values'''
    def __lt__(self, other):
        # raise an error if not 2 cards
        # less than
        if not isinstance(self,Card) or not isinstance(other, Card):
            raise TypeError('Incorrect input, please try again')
        elif self.suits == other.suits:
            return self.values < other.values
        else:
            return self.suits < other.suits 

    '''Checks to see if values and suits are equal to each other'''
    def __eq__(self, other):
        if not isinstance(self,Card) or not isinstance(other, Card):
            raise TypeError('Incorrect input, please try again')
        else:
            return self.values == other.values and self.suits == other.suits