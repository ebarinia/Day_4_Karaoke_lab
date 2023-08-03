class Room:

    def __init__(self, name, max_capacity):
        self.name = name
        self.max_capacity = max_capacity
        self.room = []
        self.songs = []
        self.till = 0
    
    def add_person(self, person):
        if len(self.room) < self.max_capacity:
            self.room.append(person)

    def remove_person(self, person):
        self.room.remove(person)

    def add_song(self, song):
        self.room.append(song)

    def add_till(self, amount):
        self.till += amount

    def charge_customer(self, customer, amount):
        customer.charge_customer(amount)
        self.add_till(amount)

    def add_playlist(self, song):
        self.songs.append(song)

    def favourite_song(self, name):
        for song in self.songs:
            if song.title == name:
                return "Woooo!"
                