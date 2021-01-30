from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

def scrapeRunningData(): 

    PATH = "/home/ethanlee000/chromedriver_linux64/chromedriver"
    driver = webdriver.Chrome(PATH)

    #driver = webdriver.Firefox(executable_path='/home/ethanlee000/geckodriver v0.29/geckodriver') 

    driver.get("https://sso.garmin.com/sso/signin?service=https%3A%2F%2Fconnect.garmin.com%2Fmodern%2F&webhost=https%3A%2F%2Fconnect.garmin.com%2Fmodern%2F&source=https%3A%2F%2Fconnect.garmin.com%2Fsignin%2F&redirectAfterAccountLoginUrl=https%3A%2F%2Fconnect.garmin.com%2Fmodern%2F&redirectAfterAccountCreationUrl=https%3A%2F%2Fconnect.garmin.com%2Fmodern%2F&gauthHost=https%3A%2F%2Fsso.garmin.com%2Fsso&locale=en_CA&id=gauth-widget&cssUrl=https%3A%2F%2Fconnect.garmin.com%2Fgauth-custom-v1.2-min.css&privacyStatementUrl=https%3A%2F%2Fwww.garmin.com%2Fen-CA%2Fprivacy%2Fconnect%2F&clientId=GarminConnect&rememberMeShown=true&rememberMeChecked=false&createAccountShown=true&openCreateAccount=false&displayNameShown=false&consumeServiceTicket=false&initialFocus=true&embedWidget=false&generateExtraServiceTicket=true&generateTwoExtraServiceTickets=true&generateNoServiceTicket=false&globalOptInShown=true&globalOptInChecked=false&mobile=false&connectLegalTerms=true&showTermsOfUse=false&showPrivacyPolicy=false&showConnectLegalAge=false&locationPromptShown=true&showPassword=true&useCustomHeader=false&mfaRequired=false&rememberMyBrowserShown=false&rememberMyBrowserChecked=false#")

    try: 
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-state-default"))
        )

    except: 
        print("Could not find Login Screen")
        driver.quit()

    try:
        usrname = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        usrname.clear()
        usrname.send_keys("ethanlee000@gmail.com")
            
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password.clear()
        password.send_keys("Wongchukhang38*")

        button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-btn-signin"))
        )
        button.click()
    except: 
        print("Could not log in")
        
    driver.get("https://connect.garmin.com/modern/activities")


    try: 
        Export = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "export-btn"))
        )
        Export.click()
        time.sleep(3)

        print("Download successful")
        

    except: 
        print("Could not find csv")

