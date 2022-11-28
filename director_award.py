class director_award:
    @staticmethod
    def tableDefinition():
        return 'directorawards (director, year, award, result)'

    def __init__(self, director, year, award, result):
        self.director = director
        self.year = year
        self.award = award
        self.result = result

    def toValue(self):
        return f'\'{self.director.name}\', {self.year}, \'{self.award}\', \'{self.result}\''
