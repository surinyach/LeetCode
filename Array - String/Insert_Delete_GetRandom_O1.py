class RandomizedSet(object):

    def __init__(self):
        self.val_index = {}
        self.values = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.val_index:
            return False
        else:
            self.values.append(val)
            self.val_index[val] = len(self.values) - 1
            return True
            
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.val_index:
            return False
        else:
            position = self.val_index.pop(val)
            last_val = self.values.pop()
            if position != len(self.values):
                self.values[position] = last_val
                self.val_index[last_val] = position
            return True
    
    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()