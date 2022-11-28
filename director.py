class director:
    @staticmethod
    def tableDefinition():
        return 'directors (director, yearofbirth)'

    def __init__(self, name, yearofbirth):
        self.name = name
        self.yearofbirth = yearofbirth

    def toValue(self):
        return f'\'{self.name}\', {self.yearofbirth}'
