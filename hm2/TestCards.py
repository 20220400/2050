from Cards import Card, Deck, Hand
import unittest
import random

'''Test cases with assertion statements specific to the card class'''

''' Tests to see if the init function output values and suits correctly '''
class TestCard(unittest.TestCase):

    def test_init(self):
        ''''''
        c1 =  Card(4, 'spades')
        self.assertEqual(c1.values, 4)
        self.assertEqual(c1.suits, 'spades')

#''' Tests to see if the repr function outputs a card correctly  '''
    def test_repr(self):
        card = Card(13, 'clubs')
        self.assertEqual(repr(card), 'Card(13 of clubs)')

# Test to see if the lt function checks if a card is less than the other card
    def test_lt(self):
        card1 = Card(13, 'clubs')
        card2 = Card(4, 'clubs')
        self.assertLess(card2,card1)

# Test to see if the lt function checks if a card is equal to the other card
    def test_eq(self):
        card1 = Card(13, 'spades')
        card2 = Card(13, 'spades')
        self.assertEqual(card2,card1)


'''Test cases with assertion statements specific to the deck class'''
class TestDeck(unittest.TestCase):
    # tests to see if the value of the deck is equal to the value of th expected val
    def test_init(self):
        c1 = Deck([1,2,3], ['clubs','spades','diamonds'])
        expectedVal = 9
        self.assertEqual(expectedVal,len(c1))

    # test to see if repr returns the proper string function of the deck
    def test__repr__(self):
        c1 = Deck([1], ['clubs'])
        c1 = str(c1)
        expectedVal = 'Deck: [Card(1 of clubs)]'
        self.assertEqual(expectedVal, c1)

   # test to see the length of the values and suits
    def test_len(self):
        list_one = range(1,14)
        list_two = ['clubs', 'diamonds', 'hearts', 'spades']
        self.assertEqual(len(list_one), 13)
        self.assertEqual(len(list_two), 4)

    # test to see if the deck is shuffled by shuffling a deck and seeing if the
    # deck before and after are equal 
    def test_shuffle(self):
        deck = Deck([1,2], ['spades','clubs'])
        deck2 = deck.shuffle()
        self.assertNotEqual(deck,deck2)

    # checks to see if user draws top card by the length
    def test_draw_top(self):
        deck = Deck([1,2], ['spades','clubs'])
        deck_len = len(deck)
        deck.draw_top()
        deck_len2 = len(deck)
        self.assertNotEqual(deck_len,deck_len2)
    
    # checks to see if deck is sorted by shuffling it first then sorting it again 
    def test_sort(self):
        deck = Deck([1,2], ['spades','clubs'])
        #deck = Deck()
        deck.shuffle()
        #shuffled deck
        #repr(deck)
        deck.sort()
        #sorted deck
        print(deck)
        print('Deck: [Card(1 of clubs), Card(2 of clubs), Card(1 of spades), Card(2 of spades)]')
        self.assertEqual(repr(deck),'Deck: [Card(1 of clubs), Card(2 of clubs), Card(1 of spades), Card(2 of spades)]')

'''Test cases with assertion statements specific to the hand class'''
class TestHand(unittest.TestCase):
    # checks to see the init function passes a hand of spades
    def test_init(self):
        h_spades = Hand([Card(value, 'spades') for value in range(5,0,-1)])
        self.assertEqual(len(h_spades.cards), 5)

   # checks to see if user plays a card by creating a Hand then asserting its equality
    def test_play(self):
        h_spades = Hand(Card(8, 'spades'))
        self.assertEqual(h_spades.play(), 'Card(8 of spades')

    # checks to see if the string function of repr in hand is correct and outptus the correct stirng value. 
    def test_repr(self, v = [1,2], s = ['clubs','spades']):
       h_spades = Hand([Card(value, 'spades') for value in range(5,0,-1)])
       h_spades.sort()
       h_spades_test = 'Hand: [Card(1 of spades), Card(2 of spades), Card(3 of spades), Card(4 of spades), Card(5 of spades)'
       self.assertEqual(repr(h_spades), h_spades_test)
if __name__ == '__main__':
    unittest.main()

