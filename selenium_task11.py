#common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
#action chains
from selenium.webdriver import ActionChains
#exceptions
from selenium.common.exceptions import NoSuchElementException

class Droppable:
    #initiate class Droppable to take it url
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.action = ActionChains(self.driver)

    # function to open the webpage and maximize it
    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.wait(3)

    # function to wait
    def wait(self, secs):
        sleep(secs)

    #function to quit
    def quit(self):
        self.driver.quit()

    # function to perform drag and drop
    def dragDrop(self):
        try:
            self.boot()
            #create drag_element variable to look for the id "draggable"
            drag_element = self.driver.find_element(By.ID,"draggable")
            # create drop_element variable to look for the id "droppable"
            drop_element = self.driver.find_element(By.ID,"droppable")
            #perform the move function
            self.action.drag_and_drop(drag_element, drop_element).perform()
            self.wait(5)

            # look for the text in the droppable element and check if the text has changed to Dropped
            text = self.driver.find_element(By.ID,"droppable").text
            if text == "Dropped!":
                print("Successful")
            else:
                print("Error")

        except NoSuchElementException as e:
            print(e)

        finally:
            self.wait(5)
            self.quit()

# create obj to call the Droppable class and perform the funcitons
url = "https://jqueryui.com/droppable/"
obj = Droppable(url)
obj.boot()
obj.dragDrop()