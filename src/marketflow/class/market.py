"""
Fondamental market class
"""

class MarketInformation:
    """
    A class to register market
    """
    def __init__(self, short_name = "", full_name = "",description = "",official_url = ""):
        # These are instance variables
        self.short_name = short_name
        self.full_name = full_name
        self.description = description
        self.official_url = official_url
    
    def show(self):
        print(f"""=== AVAILABLE STOCK MARKETS ===\nID : {1}    
        Shortname : {self.short_name}
        Fullname : {self.full_name}
        Description : {self.description}
        Official url : {self.official_url}
        """)
    

a = MarketInformation("BRVM","BOURSE REGIONALE DES VALEURS MOBILIERES","-","https://www.brvm.org/")
a.show()