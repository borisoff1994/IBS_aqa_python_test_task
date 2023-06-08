import pytest
from api.api_utils import api_client as api_method
from data.api_response_bodies import ApiResponseBodies
from data.request_body import RequestBodies


def test_get_users_list():
    # Act
    response = api_method.get_users_list()

    # Assert
    assert response.status_code == 200
    assert response.json() == ApiResponseBodies.GET_RESOURCE


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_get_single_user(user_id):
    # Act
    response = api_method.get_single_user(user_id)

    # Assert
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id


@pytest.mark.parametrize("user_id", [23, "qwerty", "???"])
def test_get_user_negative(user_id):
    # Act
    response = api_method.get_single_user(user_id)

    # Assert
    assert response.status_code == 404


def test_get_users():
    # Act
    response = api_method.get_users()

    # Assert
    assert response.status_code == 200
    assert response.json() == ApiResponseBodies.GET_USERS


def test_get_users_negative():
    # Act
    response = api_method.get_users_negative()

    # Assert
    assert response.status_code == 400


def test_create_user():
    # Arrange
    body = RequestBodies.MORPHEUS_LEADER

    # Act
    response = api_method.create_user(body)

    # Assert
    assert response.status_code == 201
    assert response.json()["name"] == body["name"]
    assert response.json()["job"] == body["job"]
    assert len(response.json()["id"]) > 0
    assert len(response.json()["createdAt"]) > 0


def test_create_user_negative():
    # Arrange
    body = RequestBodies.JOHN_NEGATIVE_CREATE

    # Act
    response = api_method.create_user(body)

    # Assert
    assert response.status_code == 400


def test_update_user():
    # Arrange
    body = RequestBodies.MORPHEUS_ZION_REZIDENT

    # Act
    response = api_method.update_user_put(body)

    # Assert
    assert response.status_code == 200
    assert response.json()["job"] == body["job"]
    assert len(response.json()["updatedAt"]) > 0


@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_delete_user(user_id):
    # Act
    response = api_method.delete_user(user_id)

    # Assert
    assert response.status_code == 204


def test_register():
    # Arrange
    body = RequestBodies.EVE_POSITIVE_REG

    # Act
    response = api_method.register(body)

    # Assert
    assert response.status_code == 200
    assert response.json()["id"] > 0
    assert len(response.json()["token"]) > 0


def test_register_negative():
    # Arrange
    body = RequestBodies.SIDNEY_NEGATIVE_REG

    # Act
    response = api_method.register(body)

    # Assert
    assert response.status_code == 400
    assert response.json() == ApiResponseBodies.ERROR_MESSAGE_MISSING_PASSWORD


def test_login():
    # Arrange
    body = RequestBodies.EVE_POSITIVE_LOGIN

    # Act
    response = api_method.login(body)

    # Assert
    assert response.status_code == 200
    assert len(response.json()["token"]) > 0


def test_login_negative():
    # Arrange
    body = RequestBodies.PETER_NEGATIVE_LOGIN

    # Act
    response = api_method.login(body)

    # Assert
    assert response.status_code == 400
    assert response.json() == ApiResponseBodies.ERROR_MESSAGE_MISSING_PASSWORD
