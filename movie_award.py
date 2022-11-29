class movie_award:
    @staticmethod
    def tableDefinition():
        return 'movieawards (title, year, award, result)'

    def __init__(self, title, year, award, result):
        self.title = title
        self.year = year
        self.award = award
        self.result = result

    def toValue(self):
        return f'\'{self.title}\', {self.year}, \'{self.award}\', \'{self.result}\''
