import api.api_utils.api_client as api_client
from web.pages.reqres_page import ReqresPage
from data.request_body import RequestBodies


def test_check_list_users__web_and_api(browser):
    # Arrange
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_get_list_users()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.get_users_list()
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_single_user__web_and_api(browser):
    # Arrange
    user_id = 2
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_get_single_user()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.get_single_user(user_id)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_single_user_not_found__web_and_api(browser):
    # Arrange
    user_id = 23
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_single_user_not_found()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.get_single_user(user_id)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_post_create__web_and_api(browser):
    # Arrange
    body = RequestBodies.MORPHEUS_LEADER
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_post_create()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.create_user(body)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_put_update__web_and_api(browser):
    # Arrange
    body = RequestBodies.MORPHEUS_ZION_REZIDENT
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_put_update()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.update_user_put(body)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_patch_update__web_and_api(browser):
    # Arrange
    body = RequestBodies.MORPHEUS_ZION_REZIDENT
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_patch_update()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.update_user_patch(body)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_delete__web_and_api(browser):
    # Arrange
    user_id = 2
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_delete()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.delete_user(user_id)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_post_register_successful__web_and_api(browser):
    # Arrange
    body = RequestBodies.EVE_POSITIVE_REG
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_post_register_successful()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.register(body)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_post_register_unsuccessful__web_and_api(browser):
    # Arrange
    body = RequestBodies.SIDNEY_NEGATIVE_REG
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_post_register_unsuccessful()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.register(body)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_post_login_successful__web_and_api(browser):
    # Arrange
    body = RequestBodies.EVE_POSITIVE_LOGIN
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_post_login_successful()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.login(body)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_post_login_unsuccessful__web_and_api(browser):
    # Arrange
    body = RequestBodies.PETER_NEGATIVE_LOGIN
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_post_login_unsuccessful()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.login(body)
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body


def test_check_get_delayed__web_and_api(browser):
    # Arrange
    page = ReqresPage(browser)
    api = api_client

    # Act
    page.click_get_delayed_response()
    web_response_code = page.get_response_code()
    web_response_body = page.get_response_body()

    api_response = api.delayed()
    api_response_code = api_response.status_code
    api_response_body = api_response.json()

    # Assert
    assert web_response_code == api_response_code
    assert web_response_body == api_response_body
