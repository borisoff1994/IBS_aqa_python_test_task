import requests


def get_users_list():
    return requests.get("https://reqres.in/api/users?page=2")


def get_single_user(user_id):
    return requests.get(f"https://reqres.in/api/users/{user_id}")


def get_users():
    return requests.get("https://reqres.in/api/users")


def get_users_negative():
    return requests.get("https://reqres.in/api/users?page=0")


def create_user(body):
    return requests.post("https://reqres.in/api/users", data=body)


def update_user_put(body):
    return requests.put("https://reqres.in/api/users/2", data=body)


def update_user_patch(body):
    return requests.patch("https://reqres.in/api/users/2", data=body)


def delete_user(user_id):
    return requests.delete(f"https://reqres.in/api/users/{user_id}")


def register(body):
    return requests.post("https://reqres.in/api/register", data=body)


def login(body):
    return requests.post("https://reqres.in/api/login", data=body)


def delayed():
    return requests.get("https://reqres.in/api/users?page=2")
