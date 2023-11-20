class Country:
    """Super Class"""
    
    name = '국가명'
    population = '인구'
    capital = '수도'
    
    class Korea(Country) :
        """Sub Class"""
        
    def __init__(self, name, population, cpaital):
        self.name = name
        self.population = population
        self.capital = capital
        
        def show (self):
            print(
            """
            국가의 이름은 {} 입니다.
            국가의 인구는 {} 입니다.
            국가의 수도는 {} 입니다. 
            """.format(self.name, self.population, self.capital)
            """
            )