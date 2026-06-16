import pytest
from selenium.common.exceptions import TimeoutException, WebDriverException
# We hook into the report generation phase
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        # Check the exception that caused the crash
        exception_info = str(call.excinfo.value)
        failure_category = "Unknown Bug"
        if isinstance(call.excinfo.value, TimeoutException):
            failure_category = "Infrastructure Timeout / Flaky Network"
        elif isinstance(call.excinfo.value, AssertionError):
            failure_category = "Product Bug / Logic Failure"
        elif isinstance(call.excinfo.value, WebDriverException):
            failure_category = "Selenium Grid / Browser Crash"
        # Attach this category to the report object
        report.failure_category = failure_category
        print(f"\n[Analytics] Test {item.name} failed due to: {failure_category}")