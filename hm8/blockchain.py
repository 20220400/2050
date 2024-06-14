from hashmap import hashmap
class Transaction():
    '''class that contains the transaction of users'''
    def __init__(self, from_user, to_user, amount):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount    
    
    def __hash__(self):
        '''returns the hash of the sender and recipient as well as the amount given'''
        return hash(tuple((self.from_user, self.to_user, self.amount)))

    def __eq__(self, other):
        '''checks whether the two hashes are equal or not'''
        if self.__hash__() == other.__hash__():
            return True
        else:
            return False

    def __repr__(self):
        '''returns a string representation of the user amount and recipient'''
        return str(self.from_user) + " transferred " + str(self.amount) + " $ to " + str(self.to_user)
    
class Block():
    '''Class that contains the collection of transaction objects'''
    def __init__(self, transactions=None, prev_hash = None):
        if transactions == None: 
            self.transactions = list()
        else:
            self.transactions = transactions
        self.prev_hash = prev_hash
    
    def update_prevhash(self, ph):
        '''contains the hash of the previous block'''
        self.prev_hash = ph
    
    def __hash__(self):
        '''returns the hash of the transactions and previous hash'''
        return hash((tuple(self.transactions), self.prev_hash))

    def add_transaction(self, transaction):
        '''a method for adding a single transaction to the block'''
        self.transactions.append(transaction)

    def __repr__(self):
        '''returns string representation of the transaction list and previous hash'''
        string = ''
        for i in self.transactions:
            string += str(i)
        return str('Transaction list:', string , 'prev_hash: ', self.prev_hash) 
    
class Ledger():
    '''class that contains the instance of Hashmaps ADT so it can be used to keep track of user balances'''
    def __init__(self):
        self._hashmap = hashmap()

    def has_funds(self, user, amount):
        '''checks to see if user has enough funds to transfer'''
        if user not in self._hashmap:
            return False
        balance = self._hashmap.get(user)
        return balance >= amount

    def deposit(self, user, amount):
        '''adds the amount of HuskyCoin to the given user'''
        balance = self._hashmap.get(user)
        new_balance = balance + amount
        self._hashmap.add(user, new_balance)

    def transfer(self, from_user, to_user, amount):
        '''subtracts an amount of huskycoin from the given user'''
        from_amt = self._hashmap.get(from_user)
        to_amt = self._hashmap.get(to_user)

        new_from_amt = from_amt - amount
        new_to_amt = to_amt + amount

        self._hashmap.add(from_user, new_from_amt)
        self._hashmap.add(to_user, new_to_amt)

    def __repr__(self):
        '''returns string representation of the hashmap dict'''
        string = ''
        for key in self.hashmap.keys():
            amount = self._hashmap[key] 
            string += str(key)+ " "+ str(amount)
        return string

class Blockchain():
    '''Contains the chain of blocks.'''
    #########################
    # Do not use these three values in any code that you write. 
    _ROOT_BC_USER = "ROOT"            # Name of root user account.  
    _BLOCK_REWARD = 1000              # Amoung of HuskyCoin given as a reward for mining a block
    _TOTAL_AVAILABLE_TOKENS = 999999  # Total balance of HuskyCoin that the ROOT user receives in block0
    #########################

    def __init__(self):
        self._blockchain = list()     # Use the Python List for the chain of blocks
        self._bc_ledger = Ledger()    # The ledger of HuskyCoin balances
        # Create the initial block0 of the blockchain, also called the "genesis block"
        self._create_genesis_block()

    # This method is complete. No additional code needed.
    def _create_genesis_block(self):
        '''Creates the initial block in the chain.
        This is NOT how a blockchain usually works, but it is a simple way to give the
        Root user HuskyCoin that can be subsequently given to other users'''
        trans0 = Transaction(self._ROOT_BC_USER, self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)
        block0 = Block([trans0])
        self._blockchain.append(block0)
        self._bc_ledger.deposit(self._ROOT_BC_USER, self._TOTAL_AVAILABLE_TOKENS)

    # This method is complete. No additional code needed.
    def distribute_mining_reward(self, user):
        '''
        You need to give HuskyCoin to some of your users before you can transfer HuskyCoing
        between users. Use this method to give your users an initial balance of HuskyCoin.
        (In the Bitcoin network, users compete to solve a meaningless mathmatical puzzle.
        Solving the puzzle takes a tremendious amount of copmputing power and consuming a lot
        of energy. The first node to solve the puzzle is given a certain amount of Bitcoin.)
        In this assigment, you do not need to understand "mining." Just use this method to 
        provide initial balances to one or more users.'''
        trans = Transaction(self._ROOT_BC_USER, user, self._BLOCK_REWARD)
        block = Block([trans])
        self.add_block(block)

    # TODO - add the rest of the code for the class here

    def __repr__(self):
        '''returns string representation of the blockchain and ledger'''
        return "Blockchain('" + str(self._blockchain) + "', '" + str(self._bc_ledger) + "')"
    
    def add_block(self, block):
        '''Adds a block to the blockchain'''
        prev_hash = hash(self._blockchain[-1])
        
        block.update_prevhash(prev_hash)

        map = dict()
        for transaction in block:
            if transaction.from_user in map:
                map[transaction.from_user] += transaction.amount
            else:
                map[transaction.from_user] = transaction.amount
        
        for user, amount in map.items():
            if not self._bc_ledger.has_funds(user, amount):
                return False
            
        self._blockchain.append(block)

        for transaction in block.transaction:
            self._bc_ledger.transfer(transaction.from_user, transaction.amount)
            self._bc_ledger.deposit(transaction.to_user, transaction.amount)

        return True

    def validate_chain(self):
        '''Checks to see if blocks have been tampered with'''
        tampererd_chain = []

        if self._blockchain[0] != None:
            tampererd_chain.append(self._blockchain)

        for i in (1, len(self._blockchain)):
            current_block = self._blockchain[i]
            prev_block = self._blockchain[i-1]

            if hash(prev_block) != current_block.prev_hash: # hash(prev_block)
                tampererd_chain.append(prev_block)

        return tampererd_chain
            