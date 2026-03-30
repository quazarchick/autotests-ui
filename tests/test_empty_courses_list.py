import pytest
from playwright.sync_api import expect


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    chromium_page_with_state.wait_for_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_title = chromium_page_with_state.locator('//div/h6[@data-testid="courses-list-toolbar-title-text"]')
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    empty_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_icon).to_be_visible()

    empty_view_title_text = chromium_page_with_state.locator('//h6[@data-testid="courses-list-empty-view-title-text"]')
    expect(empty_view_title_text).to_be_visible()
    expect(empty_view_title_text).to_have_text("There is no results")

    empty_view_description_text = chromium_page_with_state.locator(
        '//p[@data-testid="courses-list-empty-view-description-text"]')
    expect(empty_view_description_text).to_be_visible()
    expect(empty_view_description_text).to_have_text("Results from the load test pipeline will be displayed here")
