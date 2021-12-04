class Model():

    def __init__(self):
        self.preposition = ""
        self.data = []
    
    def get_data(self, string):
        self.array = []

        #FILTERS:

        # 1. Prepositions
        for charac in string:
            self.array.append(charac)
            if charac == "p":
                self.preposition = self.preposition + "p "
            elif charac == "q":
                self.preposition = self.preposition + "q "
            elif charac == "r":
                self.preposition = self.preposition + "r "
            elif charac == "s":
                self.preposition = self.preposition + "s "
            elif charac == "~":
                self.preposition = self.preposition + "not "
            elif charac == "˄":
                self.preposition = self.preposition + "and "
            elif charac == "v":
                self.preposition = self.preposition + "or "
            elif charac == "→":
                self.preposition = self.preposition + "implies "
            elif charac == "↔":
                self.preposition = self.preposition + "= "
            elif charac == "+":
                self.preposition = self.preposition + "characor "
            elif charac == "(":
                self.preposition = self.preposition + "("
            elif charac == ")":
                self.preposition = self.preposition + ")"

        #2. Identifiers
        
        self.ids = filter(lambda id:
            id == 'p' or
            id == 'q' or
            id == 'r'or
            id == 's',
            self.array)

        self.data.append(list(self.ids))
        self.data.append(self.preposition)

        self.preposition = ""
        self.ids = None

        return self.data