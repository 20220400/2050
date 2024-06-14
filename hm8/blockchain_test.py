import unittest
from blockchain import Block , Blockchain, Transaction, Ledger
from hashmap import hashmap
# from blockchain import Blockchain
class Test_Transaction(unittest.TestCase):
    '''Transaction test cases'''
    def test_hash(self):
        TransactionOne = Transaction("Phineas", "Ferb", 100)
        TransactionTwo = Transaction("Phineas", "Ferb", 100)
        TransactionThree = Transaction("Ferb", "Phineas", 100)
        
        self.assertEqual(hash(TransactionOne), hash(TransactionTwo))
        self.assertNotEqual(hash(TransactionOne), hash(TransactionThree))

    def test_Eq(Self):
        TransactionOne = Transaction("Phineas", "Ferb", 100)
        TransactionTwo = Transaction("Phineas", "Ferb", 100)
        TransactionThree = Transaction("Phineas", "Perry", 200)
        Self.assertEqual(TransactionOne, TransactionTwo)
        Self.assertNotEqual(TransactionOne, TransactionThree)

class Test_Block(unittest.TestCase):
    '''Block test cases'''
    def test_prevhash(self): 
        TransactionOne =  Transaction('Phineas','Ferb', 7 )
        prev_hash = 'ghjkl0187'
        block = Block([TransactionOne], prev_hash)

        new_prev_hash = 'fdsa9498'
        block.update_prevhash(new_prev_hash)

        self.assertEqual(block.prev_hash, new_prev_hash)

    def test_hash(self):
        TransactionOne = Transaction("Phineas", "Ferb", 100)
        TransactionTwo = Transaction("Candace", "Ferb", 200)
        block1 = Block([TransactionOne, TransactionTwo], "prev_hash_1")
        block2 = Block([TransactionOne, TransactionTwo], "prev_hash_2")
        self.assertNotEqual(hash(block1), hash(block2))

    def test_add_transaction(self):
       block = Block()

       TransactionOne = Transaction('Phineas','Ferb', 100 )
       TransactionTwo = Transaction('Candace', 'Stacy', 200)
       TransactionThree = Transaction('Doofenshmirtz', 'Perry', 300)

       block.add_transaction(TransactionOne)
       block.add_transaction(TransactionTwo)
       block.add_transaction(TransactionThree)

       self.assertEqual(block.transactions, [TransactionOne, TransactionTwo, TransactionThree])
    
class Test_Ledger(unittest.TestCase):
    '''Ledger test cases'''
    def test_has_funds(self):
        ledger = Ledger()
        personOne = "Doofenshmirtz"
        personTwo = "Perry"
        personThree = "Candace"

        ledger.deposit(personOne, 100)
        ledger.deposit(personTwo, 50)

        self.assertTrue(ledger.has_funds(personOne, 50))
        self.assertFalse(ledger.has_funds(personTwo, 101))
        self.assertFalse(ledger.has_funds(personThree, 10))

    def test_deposit(self):
        ledger = Ledger()
        personOne = "Candace"
        ledger.deposit(personOne,100)
        self.assertEqual(ledger._hashmap.get(personOne),100)

        ledger.deposit(personOne, 50)
        self.assertEqual(ledger._hashmap.get(personOne),150)

        personTwo = "Stacy"
        ledger.deposit(personTwo, 200)
        self.assertEqual(ledger._hashmap.get(personTwo),200)

    def test_Transfer(self):
       # Create a new ledger
        ledger = Ledger()
        personOne = "Candace"
        personTwo = "Stacy"

        ledger.deposit(personOne, 100)
        ledger.transfer(personOne, personTwo, 25)

        # Check that personOne's balance is  75 and personTwo's balance is  25 
        self.assertEqual(ledger._hashmap.get(personOne), 75)
        self.assertEqual(ledger._hashmap.get(personTwo), 25)

class Test_blockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()
        self.blockchain.add_block(Block([Transaction('Phineas', 'Ferb', 10)]))
    
    def test_add_block(self):
        '''tests to see if block is added'''
        # Add a block with a valid transaction
        self.assertTrue(self.blockchain.add_block(Block([Transaction('Ferb', 'Candace', 5)])))
        self.assertEqual(len(self.blockchain._blockchain), 2)

        # Add a block with an invalid transaction (insufficient funds)
        self.assertFalse(self.blockchain.add_block(Block([Transaction('Phineas', 'Candace', 100)])))
        self.assertEqual(len(self.blockchain._blockchain), 2)

    def test_validate_chain(self):
        '''tests to see if validate function method works'''
        # Test that the original chain is valid
        tampered_blocks = self.blockchain.validate_chain()
        self.assertEqual(len(tampered_blocks), 0)

        # Test that tampering with a block is detected
        block_to_tamper = self.blockchain._blockchain[0]
        block_to_tamper.add_transaction(Transaction('Perry', 'Phineas', 10))
        tampered_blocks = self.blockchain.validate_chain()
        self.assertEqual(len(tampered_blocks), 1)

        # Test that adding a block to the end of the chain doesn't affect validity of previous blocks
        self.blockchain.add_block(Block([Transaction('Candace', 'Doofenshmirtz', 15)]))
        tampered_blocks = self.blockchain.validate_chain()
        self.assertEqual(len(tampered_blocks), 1)

class Test_hash_map(unittest.TestCase):
    def test_add(self):
        '''tests add function in hashmap'''
        h = hashmap()
        h.add('Phineas', 100)
        h.add('Ferb', 200)
        self.assertEqual(h.get('Phineas'), 100)
        self.assertEqual(h.get('Ferb'), 200)
        self.assertEqual(h.get('Candace'), 0)

    def test_get(self):
        '''tests get function in hashmap'''
        h = hashmap()
        h.add('Phineas', 100)
        h.add('Ferb', 200)
        self.assertEqual(h.get('Phineas'), 100)
        self.assertEqual(h.get('Ferb'), 200)
        self.assertEqual(h.get('Candace'), 0)

    def test_contains(self):
        '''Tests contains method in hashmap'''
        h = hashmap()
        h.add('Phineas', 100)
        h.add('Ferb', 200)
        self.assertTrue('Phineas' in h)
        self.assertTrue('Ferb' in h)
        self.assertFalse('Candace' in h)

        
if __name__ == '__main__':
    unittest.main()