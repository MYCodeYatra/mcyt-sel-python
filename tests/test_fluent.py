def test_fluent_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.enter_username("admin")
    login_page.enter_password("pass")
    # click_login() returns a DashboardPage object!
    dashboard_page = login_page.click_login()
    # We instantly have access to dashboard methods without initializing it!
    dashboard_page.click_logout()