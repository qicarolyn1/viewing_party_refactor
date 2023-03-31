import pytest
from viewing_party.person import Person
from viewing_party.movie import Movie

def test_create_person():
    # Arrange / Act
    kendall = Person("Kendall", ["Nancy"], [])

    # Assert
    assert isinstance(kendall, Person)

def test_person_name_is_set_correctly():
    # Arrange / Act
    nancy = Person("Nancy", ["Kendall"], [])
    danica = Person("Danica", ["Ping"], [])

    # Assert
    assert nancy.name == "Nancy"
    assert danica.name == "Danica"

def test_person_friends_list_is_set_correctly():
    # Arrange / Act
    ana = Person("Ana", ["Ariel"], [])

    # Assert
    assert ana.friends == ["Ariel"]

def test_friend_added_to_person():
    # Arrange
    laura = Person("Laura", ["Sage"], [])

    # Act
    laura.add_friend("Elizabeth")

    # Assert
    assert laura.friends == ["Sage", "Elizabeth"]

def test_no_duplicate_friends_added():
    # Arrange
    moyo = Person("Moyo", ["Sarah"], [])

    # Act
    moyo.add_friend("Sarah")

    # Assert
    assert moyo.friends == ["Sarah"]

def test_add_movie_to_watchlist():
    # Arrange
    moyo = Person("Moyo", ["Sarah"], [])
    harry_potter = Movie("Harry Potter", "fiction", 5)

    #Act
    moyo.add_watchlist(harry_potter)

    #Assert
    moyo.watchlist == [harry_potter]

def test_add_movie_to_watchlist_duplicate():
    # Arrange
    harry_potter = Movie("Harry Potter", "fiction", 5)
    moyo = Person("Moyo", ["Sarah"], [harry_potter])

    #Act
    moyo.add_watchlist(harry_potter)

    #Assert
    moyo.watchlist == [harry_potter]

def test_watch_a_movie_adds_movie_to_watched():
    # Arrange
    harry_potter = Movie("Harry Potter", "fiction", 5)
    moyo = Person("Moyo", ["Sarah"], [harry_potter])

    #Act
    moyo.watch_a_movie(harry_potter)

    #Assert
    moyo.watchlist == []
    moyo.watched == [harry_potter]

def test_watch_a_movie_adds_movie_was_not_in_watchlist():
    # Arrange
    harry_potter = Movie("Harry Potter", "fiction", 5)
    lords_of_rings = Movie("Lord of The Rings", "fantasy", 5)
    moyo = Person("Moyo", ["Sarah"], [lords_of_rings])

    #Act
    moyo.watch_a_movie(harry_potter)

    #Assert
    moyo.watchlist == [lords_of_rings]
    moyo.watched == [harry_potter]

def test_watch_a_movie_adds_movie_duplicate_in_watched():
    # Arrange
    harry_potter = Movie("Harry Potter", "fiction", 5)
    lords_of_rings = Movie("Lord of The Rings", "fantasy", 5)
    moyo = Person("Moyo", ["Sarah"], [lords_of_rings, harry_potter])

    #Act
    moyo.watch_a_movie(harry_potter)
    moyo.watch_a_movie(harry_potter)

    #Assert
    moyo.watchlist == [lords_of_rings]
    moyo.watched == [harry_potter]