class hashmap():
    def __init__(self):
        self._dict = dict()

    def add(self, user, balance):
        '''update user amount'''
        self._dict[user] = balance
        
    def get(self,user):
        #get account balance
        '''Case where user in dict and not in dict'''
        if user in self._dict:
             return self._dict[user]
        else:
             return 0

    def __contains__(self,user):
        '''checks if user exists or not'''
        return True if user in self._dict else False
  