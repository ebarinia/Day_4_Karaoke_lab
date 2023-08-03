class Person:

    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song 
    
   
    def charge_customer(self, amount):
        self.wallet -= amount 