from .user_finder import UserFinder
from src.utils.generate_word import generate_word
from src.infra.db.tests.users_repository import UsersRepositorySpy

def test_find():
    first_name = generate_word()

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributes["first_name"] == first_name

    assert response["type"] == "Users"
    assert response["count"] == len(response["attributes"])
    assert response["attributes"]