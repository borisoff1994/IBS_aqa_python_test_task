from web.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class ReqresPage(BasePage):
    def __init__(self, browser: WebDriver):
        url = "https://reqres.in/"
        super(ReqresPage, self).__init__(browser, url)

    def click_get_list_users(self):
        self._scroll_to(ReqresPageLocators.GET_LIST_USERS)
        self._click(ReqresPageLocators.GET_LIST_USERS)

    def click_get_single_user(self):
        self._scroll_to(ReqresPageLocators.GET_SINGLE_USER)
        self._click(ReqresPageLocators.GET_SINGLE_USER)

    def click_single_user_not_found(self):
        self._scroll_to(ReqresPageLocators.GET_SINGLE_USER_NOT_FOUND)
        self._click(ReqresPageLocators.GET_SINGLE_USER_NOT_FOUND)

    def click_get_list_resource(self):
        self._scroll_to(ReqresPageLocators.GET_LIST_RESOURCE)
        self._click(ReqresPageLocators.GET_LIST_RESOURCE)

    def click_get_single_resource(self):
        self._scroll_to(ReqresPageLocators.GET_SINGLE_RESOURCE)
        self._click(ReqresPageLocators.GET_SINGLE_RESOURCE)

    def click_get_single_resource_not_found(self):
        self._scroll_to(ReqresPageLocators.GET_SINGLE_USER_NOT_FOUND)
        self._click(ReqresPageLocators.GET_SINGLE_USER_NOT_FOUND)

    def click_post_create(self):
        self._scroll_to(ReqresPageLocators.POST_CREATE)
        self._click(ReqresPageLocators.POST_CREATE)

    def click_put_update(self):
        self._scroll_to(ReqresPageLocators.PUT_UPDATE)
        self._click(ReqresPageLocators.PUT_UPDATE)

    def click_patch_update(self):
        self._scroll_to(ReqresPageLocators.PATCH_UPDATE)
        self._click(ReqresPageLocators.PATCH_UPDATE)

    def click_delete(self):
        self._scroll_to(ReqresPageLocators.DELETE)
        self._click(ReqresPageLocators.DELETE)

    def click_post_register_successful(self):
        self._scroll_to(ReqresPageLocators.POST_REGISTER_SUCCESSFUL)
        self._click(ReqresPageLocators.POST_REGISTER_SUCCESSFUL)

    def click_post_register_unsuccessful(self):
        self._scroll_to(ReqresPageLocators.POST_REGISTER_UNSUCCESSFUL)
        self._click(ReqresPageLocators.POST_REGISTER_UNSUCCESSFUL)

    def click_post_login_successful(self):
        self._scroll_to(ReqresPageLocators.POST_LOGIN_SUCCESSFUL)
        self._click(ReqresPageLocators.POST_LOGIN_SUCCESSFUL)

    def click_post_login_unsuccessful(self):
        self._scroll_to(ReqresPageLocators.POST_LOGIN_UNSUCCESSFUL)
        self._click(ReqresPageLocators.POST_LOGIN_UNSUCCESSFUL)

    def click_get_delayed_response(self):
        self._scroll_to(ReqresPageLocators.GET_DELAYED_RESPONSE)
        self._click(ReqresPageLocators.GET_DELAYED_RESPONSE)

    def get_response_code(self):
        self._scroll_to(ReqresPageLocators.RESPONSE_CODE)
        return self._get_text(ReqresPageLocators.RESPONSE_CODE)

    def get_response_body(self):
        self._scroll_to(ReqresPageLocators.RESPONSE_BODY)
        return self._get_text(ReqresPageLocators.RESPONSE_BODY)


class ReqresPageLocators:
    GET_LIST_USERS = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(1)")
    GET_SINGLE_USER = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(2)")
    GET_SINGLE_USER_NOT_FOUND = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(3)")
    GET_LIST_RESOURCE = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(4)")
    GET_SINGLE_RESOURCE = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(5)")
    GET_RESOURCE_NOT_FOUND = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(6)")
    POST_CREATE = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(7)")
    PUT_UPDATE = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(8)")
    PATCH_UPDATE = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(9)")
    DELETE = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(10)")
    POST_REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(11)")
    POST_REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(12)")
    POST_LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(13)")
    POST_LOGIN_UNSUCCESSFUL = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(14)")
    GET_DELAYED_RESPONSE = (By.CSS_SELECTOR, "div.endpoints ul li:nth-child(15)")
    RESPONSE_CODE = (By.CSS_SELECTOR, "div.output div.response p")
    RESPONSE_BODY = (By.CSS_SELECTOR, "div.output div.response pre")
