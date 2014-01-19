
class Chain(object):
    def __init__(self):
        self.totals = [0] * 256 # Records the total occurences of a character.
        self.chain = [] # Contains occurences of each transition.
        for i in range(0,256):
            self.chain.append([0] * 256)

    def add_transition(self, from_char, to_char):
        self.chain[ord(from_char)][ord(to_char)] += 1
        self.totals[ord(from_char)] += 1

    def get_transition(self, from_char, to_char):
        ''' Returns the probability of a character from_char
        transitioning to the character to_char.'''
        occurences = self.chain[ord(from_char)][ord(to_char)]
        total_from = self.totals[ord(from_char)]
        if total_from:
            return occurences / ( 1.0 * total_from)
        else:
            return 0.0;

    
    def record_string(self, data):
        # The last byte doesn't transition to anywhere else.
        # So we only iterate to len - 1
        for i in range(len(data) - 1): 
            self.add_transition(data[i], data[i+1])
        
    def compare(self, data):
        total = 0.0
        for i in range(len(data) - 1):
            total += self.get_transition(data[0], data[1])

        return total / len(data)
        
