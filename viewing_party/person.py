class Person:
    def __init__(self, name, friends, watchlist):
        self.name = name
        self.friends = friends
        self.watchlist = watchlist
        self.watched = []
    
    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)

    def add_watchlist(self, movie):
        if movie not in self.watchlist:
            self.watchlist.append(movie)

    def watch_a_movie(self, movie):
        if movie not in self.watched:
            self.watched.append(movie)
        if movie in self.watchlist:
            self.watchlist.remove(movie)
