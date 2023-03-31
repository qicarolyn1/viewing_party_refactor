import pytest
from viewing_party.movie import Movie

def test_check_attributes():
    # Arrange / Act
    harry_potter = Movie("Harry Potter", "fiction", 5)

    # Assert
    assert harry_potter.name == "Harry Potter"
    assert harry_potter.genre == "fiction"
    assert harry_potter.rating == 5

def test_create_movie():
    # Arrange / Act
    harry_potter = Movie("Harry Potter", "fiction", 5)

    # Assert
    assert isinstance(harry_potter, Movie)