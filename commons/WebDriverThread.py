from selenium import webdriver

class WebDriverThread:

    def __init__(self):
        self.driver=webdriver
    
    def get_driver(self):
        return self.driver
    
    def quit_driver(self):
        
        if self.driver:
            self.driver.quit()