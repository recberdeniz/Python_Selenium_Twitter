# This code script is written by @recberdeniz to exercise about python selenium application for Python Programming
# Python selenium twitter script for find
# followed people, mutual following and just your followed.
# Also this script can automatically unfollow just your followed people
# Postscript: I used Mozilla Firefox as a web driver please check that your web driver option and revise the script.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common import exceptions
import time
usernames = list()
users = list()
ulist = list()
mutual_list = list()
to_getid = list()
options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
browser = webdriver.Firefox(executable_path=r'C:\Users\blue_\anaconda3\geckodriver.exe', options=options)
browser.get("https://twitter.com/")
time.sleep(5)
login = browser.find_element(By.XPATH, "//*[@id='layers']/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
login.click()
time.sleep(3)
username = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
username.send_keys("Enter your e-mail or username") # twitter username or email key section
forward = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div")
time.sleep(3)
forward.click()
time.sleep(3)
password = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password.send_keys("Enter your password") # twitter password key section
userlogin = browser.find_element(By.XPATH, "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
userlogin.click()
time.sleep(5)
profile_widget = browser.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div")
time.sleep(2)
profile_widget.click()
time.sleep(5)
followed_widget = browser.find_element(By.CSS_SELECTOR, ".css-4rbku5.css-18t94o4.css-901oao.r-18jsvk2.r-1loqt21.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-qvutc0")
followed_widget.click()
time.sleep(5)
try:
    for followed in browser.find_elements(By.CSS_SELECTOR, "div[data-testid='cellInnerDiv']"):
        users.append(followed.text)
except exceptions.StaleElementReferenceException:
    pass
time.sleep(2)
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage = document.body.scrollHeight; return lenOfPage;")
match = False
counter = 0
time.sleep(2)
while match == False:
    time.sleep(3)
    lastCount = lenOfPage
    try:
        for followed in browser.find_elements(By.CSS_SELECTOR, "div[data-testid='cellInnerDiv']"):
            users.append(followed.text)
        time.sleep(3)
        lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight); var lenOfPage = document.body.scrollHeight; return lenOfPage;")

        if lenOfPage == lastCount:
            match = True
    except exceptions.StaleElementReferenceException:
        pass
time.sleep(3)

ulist = list(dict.fromkeys(users)) # When browser getting data from html selector, some of elements could be duplicated, we need to remove duplicate elements

for i in ulist:
    if "Seni takip ediyor" in i: # It is depending on your language and "Seni takip ediyor" means that "Following you" in Turkish, please check with your language and change the string
        mutual_list.append(i)

just_followed = [i for i in ulist if i not in mutual_list] # list comprehension method to subtract between followed people and mutual following

# This part of code, creates three different text folder that includes all of your followed people, mutual followed and just your followed
with open("followed_people.txt", "w", encoding="UTF-8") as file:
    for i in ulist:
        file.write(i + "\n")
        file.write("**************************\n")

with open("mutual_followed.txt", "w", encoding="UTF-8") as file:
    for i in mutual_list:
        file.write(i + "\n")
        file.write("**************************\n")

with open("just_followed.txt", "w", encoding="UTF-8") as file:
    for i in just_followed:
        file.write(i + "\n")
        file.write("**************************\n")
# end of text folder process
# Here is a setting process that before unfollowing process,
# every list has one null cell and we need to filter and remove, thats why we put this code here.
just_followed = filter(None, just_followed)
for i in just_followed:
    to_getid.append(i.split("\n"))
time.sleep(2)
# Here is the last part of this application that check the username who are not followed you going to unfollow from you.
for i in to_getid:
    time.sleep(3)
    browser.get("https://twitter.com/" + i)
    try:
        time.sleep(5)
        unf = browser.find_element(By.CSS_SELECTOR,
                                   "div[data-testid='placementTracking']")
        unf.click()
        time.sleep(2)
        unf_second = browser.find_element(By.XPATH,
                                          "//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span/span")
        unf_second.click()
    except Exception:
        print("Here is a problem check this user " + i)
time.sleep(3)
browser.close()
