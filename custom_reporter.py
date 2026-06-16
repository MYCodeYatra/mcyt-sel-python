import requests
class CustomChatReporter:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url
        self.passed = 0
        self.failed = 0
        self.failed_tests = []
    # 1. Listen for individual test results
    def pytest_runtest_logreport(self, report):
        # We only care about the actual execution phase (not setup/teardown)
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1
                self.failed_tests.append(report.nodeid)
    # 2. Listen for the end of the entire test suite
    def pytest_sessionfinish(self, session, exitstatus):
        total = self.passed + self.failed
        # Calculate the success rate
        pass_rate = (self.passed / total * 100) if total > 0 else 0
        # Format our custom message
        message = f"🚀 **Nightly UI Automation Completed!** 🚀\n"
        message += f"Total Executed: {total}\n"
        message += f"✅ Passed: {self.passed}\n"
        message += f"❌ Failed: {self.failed}\n"
        message += f"📊 Pass Rate: {pass_rate:.1f}%\n"
        if self.failed > 0:
            message += "\n**Failing Tests:**\n"
            for test in self.failed_tests[:5]: # Show max 5 to avoid spam
                message += f"- {test}\n"
        # 3. Send the HTTP Request to the Chat Webhook!
        payload = {"text": message}
        print(f"\n[CustomReporter] Sending metrics to Webhook...")
        try:
            requests.post(self.webhook_url, json=payload)
            print("[CustomReporter] Success!")
        except Exception as e:
            print(f"[CustomReporter] Failed to send message: {e}")