class Movie:
    def __init__(self,movieName,rating):
        self.movieName=movieName
        self.rating=rating
m=Movie("Alpha",8.7)
print(m.movieName)
print(m.rating)