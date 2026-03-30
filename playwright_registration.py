from playwright.sync_api import sync_playwright, expect

def test_successful_registration():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        page.fill('//div[@data-testid="registration-form-email-input"]/div/input', "test@mail.su")
        page.fill('//div[@data-testid="registration-form-username-input"]/div/input', "Zverr001")
        page.fill('//div[@data-testid="registration-form-password-input"]/div/input', "22323234")

        registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
        registration_button.click()

        page.wait_for_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

        dashboard_title = page.get_by_test_id("dashboard-toolbar-title-text")
        expect(dashboard_title).to_be_visible()
