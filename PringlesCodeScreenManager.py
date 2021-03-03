import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import PringlesCodeRandomizer

# This section of the code uses Selenium to interact with the browser.

# First you need to download the Chrome webdriver and copy the path where you stored it.  

path = "C:\Program Files (x86)\Google\Chrome\WebDriver\chromedriver.exe"

# Create the driver instance to start manipulating the web.

driver = webdriver.Chrome(path)

# Here the code opens a Chrome tab with the bot already in it.

driver.get("https://www.pringlesgamer.com.co/")

# This waits till the webpage is fully loaded.

time.sleep(3)

# This takes the email and password elements on the page. 

emailInput = driver.find_element_by_id("KSTL-Registration-UserName")    # This is the email ID element, replace it according to your Pringles page
passwordInput = driver.find_element_by_id("KSTL-Registration-Password") # This is the password ID element, replace it according to your Pringles page

emailInput.send_keys("")        # Here goes your email.
emailInput.send_keys(Keys.TAB)
passwordInput.send_keys("")     # And here your password.

# Because this bot cannot bypass reCAPTCHA, you need to complete it by yourself. Just 
# press "y" or "n" if you manage to complete it. 

login = "n"

while (login == "n" or login == "N" or login == "no" or login == "No" or login == "NO"):

    login = input("¿Did you manage to log in correctly? y|n\n")

    if (login == "y" or login == "Y" or login == "yes" or login == "Yes" or login == "YES"):

        # Then, if you were able to log in correctly, then the bot will scrape all the web site information
        # Such as Lote, Expiration date and type of Pringles can (Small, medium, or large). 

        loteInput = driver.find_element_by_id("lote")                                                                                       # Lote serial code
        fechaInput = driver.find_element_by_id("dateven")                                                                                   # Expiration date
        tipoInput = driver.find_element_by_id("marca")                                                                                      # Type of can
        sendButton = driver.find_element_by_id("enviar")                                                                                    # The button that you press to summit your entry
        quitbutton = driver.find_element_by_xpath("//button[contains(@class,\"close-btn\") and contains(@aria-label,\"cerrar modal\")]")    # This is the close button, more of this lately
        tipoObject = Select(tipoInput)                                                                                                      # Because of how HTML select item works, we need to do this.
        ranListnumbers = [1, 2, 3]                                                                                                          # Array with the three types of cans
        ranListDistribution = [0.75, 0.2, 0.05]                                                                                             # Probability of choose one of the three types of can, more of this lately

        for i in range(1000): # Change the number inside range() to change the number of entries that you want.

            # Calls the getLote() and getExpirationDate() functions from the other class. 

            loteKey = str(PringlesCodeRandomizer.getLote())
            fechaKey = str(PringlesCodeRandomizer.getExpirationDate())

            # After that, the bot enters the Lote and the Date on the webpage. It also prints the codes on the console just to make sure.

            loteInput.send_keys(loteKey)
            loteInput.send_keys(Keys.TAB)
            print(loteKey)

            fechaInput.send_keys(fechaKey)
            fechaInput.send_keys(Keys.TAB)
            print(fechaKey)

            # This selects one of the three types of cans based on probably. This is just for fun but aparently the GP website does not need this.

            ranList = random.choices(ranListnumbers, ranListDistribution)
            ranValue = ranList[0]

            if (ranValue == 1):

                tipoObject.select_by_value("f5422024-574e-4f24-80fb-251a38512b72")

            elif (ranValue == 2):

                tipoObject.select_by_value("da677ebf-3ce2-4e94-9ce1-52af9d2c9e6f")
            
            elif (ranValue == 3):

                tipoObject.select_by_value("2657fce8-8643-46e7-bdf3-f2364072e319")
            
            # Afther that, this summits the entry on the webside.

            sendButton.click()

            time.sleep(2)

            # The page pops up a sign telling you that it succesfully summited the entry. So, this code closes it. 

            driver.execute_script("arguments[0].click();", quitbutton)

            time.sleep(2)

            # At this point the bot finish the cicle and then it starts again.

        print("Thats all for today. Hope you liked my bot! Please subscribe to the Spiffin Brit.")

        driver.quit()

    elif (login == "n" or login == "N" or login == "no" or login == "No" or login == "NO"):

        print("Sorry to hear that, please try again\n")
        
        time.sleep(1)

    else:

        print("Are you sure you just pressed the correct key? Please try again\n")

        login = "n"

        time.sleep(1)


