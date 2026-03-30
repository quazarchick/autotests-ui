import pytest  # Импортируем pytest
from playwright.sync_api import Playwright, Page, \
    expect  # Имопртируем класс страницы, будем использовать его для аннотации типов
from pytest_playwright.pytest_playwright import new_context


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def chromium_page(playwright: Playwright) -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Запускаем браузер
    browser = playwright.chromium.launch(headless=False)

    # Передаем страницу для использования в тесте
    yield browser.new_page()

    # Закрываем браузер после выполнения тестов
    browser.close()


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    email_input = page.locator('//div[@data-testid="registration-form-email-input"]/div/input')
    username_input = page.locator('//div[@data-testid="registration-form-username-input"]/div/input')
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]/div/input')
    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    expect(registration_button).to_be_disabled()

    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")

    registration_button.click()

    page.wait_for_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture(scope="function")
def chromium_page_with_state(playwright: Playwright, initialize_browser_state) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    page = context.new_page()
    return page
