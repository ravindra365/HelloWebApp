from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

class TestNewTest:

    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless")  # optional for EC2
        # Set up service with logging level "trace"
        service = Service(
        executable_path="/usr/local/bin/geckodriver",
        log_path="/tmp/python/geckodriver.log"  # optional log output
        )
        service.log_level = "trace"
        self.driver = webdriver.Firefox(service=service, options=options)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_newTest(self):
        print(">>> Starting test")
        self.driver.set_page_load_timeout(10)
        try:
            self.driver.get("http://51.92.147.60:8081/HelloWebApp/")
            print(">>> Page loaded")
            page_source = self.driver.page_source
            print(">>> Page Source Length:", len(page_source))
            
            h1_elem = self.driver.find_element(By.XPATH, "//h1")
            h1_text = h1_elem.text
            print(">>> Found H1 text:", h1_text)
            assert h1_text == "Welcome to Hello World"
        except Exception as e:
            print(">>> ERROR:", e)
            raise