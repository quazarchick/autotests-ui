import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list():
    with sync_playwright() as playwright:
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

        new_context = browser.new_context(storage_state="browser-state.json")
        new_page = new_context.new_page()

        new_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        new_page.wait_for_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        courses_title = new_page.locator('//div/h6[@data-testid="courses-list-toolbar-title-text"]')
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        empty_icon = new_page.get_by_test_id("courses-list-empty-view-icon")
        expect(empty_icon).to_be_visible()

        empty_view_title_text = new_page.locator('//h6[@data-testid="courses-list-empty-view-title-text"]')
        expect(empty_view_title_text).to_be_visible()
        expect(empty_view_title_text).to_have_text("There is no results")

        empty_view_description_text = new_page.locator('//p[@data-testid="courses-list-empty-view-description-text"]')
        expect(empty_view_description_text).to_be_visible()
        expect(empty_view_description_text).to_have_text("Results from the load test pipeline will be displayed here")
