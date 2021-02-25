from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
path = "./chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://moodle.iitd.ac.in/login/index.php")
username = driver.find_element_by_name("username")
usergiven = input("\nEnter your Kebros Username :")
username.send_keys(usergiven)
password = driver.find_element_by_name("password")
passgiven = input("\nEnter your Kebros password :")
password.send_keys(passgiven)
cat = driver.find_element_by_name("valuepkg3")
form_text = driver.find_element_by_id("login").text
Captcha_text = form_text.splitlines()[3]
t = Captcha_text.split()
if "add" in t:
    ans = int(t[-4]) + int(t[-2])
elif "subtract" in t:
    ans = int(t[-4]) - int(t[-2])
elif "second" in t:
    ans = int(t[-2])
else:
    ans = int(t[-4])
cat.send_keys(Keys.BACKSPACE)
cat.send_keys(ans)
cat.send_keys(Keys.RETURN)
try:
    l= driver.find_element_by_id("loginerrormessage")
    print ("\n\n\nInvalid Username or password !!!!!,\n!!Re-Run the program")
    driver.quit()
except NoSuchElementException:
    print ("\n\nDo you want to work on moodle now")
    yes = ["yes","Y","y","yep","1","Yes","On","on"]
    no = ["no","N","n","nope","0","No","Off","off"]
    op = input("Enter Yes/No ----> ")
    if op in yes:
        print("\nHave a good Day")
    else:
        driver.quit()


