class And:
    def __init__(self, *matchers):
        self.matchers = matchers
    
    def matches(self, player):
        for matcher in self.matchers:
            if not matcher.matches(player):
                return False
        
        return True
