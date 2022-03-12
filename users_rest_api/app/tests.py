import unittest
import requests
from os import getenv
from random import choice
from string import ascii_letters


def generate_random_string(size: int):
    return ''.join(choice(ascii_letters) for _ in range(size))


class FunctionalTests(unittest.TestCase):
    # API base URL
    BASE = f"http://127.0.0.1:{getenv('PORT', 5000)}/users"

    def add_random_user(self):
        user = {
            "firstname": generate_random_string(10),
            "lastname": generate_random_string(10),
            "age": 8
        }
        return user, requests.post(self.BASE, user)

    def test_user_add(self):
        user, resp = self.add_random_user()
        self.assertEqual(201, resp.status_code)
        # check that result is not corrupted
        resp = resp.json()
        # save and delete extra key
        id = resp["id"]
        del resp["id"]
        self.assertEqual(user, resp)

    def test_user_modified(self):
        user, resp = self.add_random_user()
        user["age"] = 11
        users_before = len(requests.get(self.BASE).json())

        # send modification request
        resp = requests.put(f'{self.BASE}/{resp.json()["id"]}', user)
        self.assertEqual(201, resp.status_code)
        user["id"] = resp.json()["id"]
        self.assertEqual(user, resp.json())

        # check that no extra users were added
        users_after = len(requests.get(self.BASE).json())
        self.assertEqual(users_before, users_after)

    def test_user_deleted(self):
        user, resp = self.add_random_user()
        id = resp.json()["id"]
        users_before = len(requests.get(self.BASE).json())

        resp = requests.delete(f'{self.BASE}/{id}')

        users_after = len(requests.get(self.BASE).json())
        self.assertLess(users_after, users_before)

        resp = requests.get(f'{self.BASE}/{id}')
        self.assertEqual(404, resp.status_code)


if __name__ == '__main__':
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()
