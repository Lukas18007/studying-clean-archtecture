from src.domain.models.users import Users
from src.utils.generate_word import generate_word
from typing import List
import random


class UsersRepositorySpy:

    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age
        return

    def select_user(self, first_name: str) -> List[Users]:
        user_list = []
        qnt_users = random.randint(1,10)

        self.select_user_attributes["first_name"] = first_name

        for i in range(1,qnt_users):
            user_list.append(
                Users(
                    random.randint(1, 100), 
                    first_name, 
                    generate_word(), 
                    random.randint(1, 99)
                )
            )
        
        return user_list