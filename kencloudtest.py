#sudo apt-get install python-bs4 
#sudo pip install beautifulsoup4
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/


#https://pypi.python.org/pypi/selenium
#https://askubuntu.com/questions/851401/where-to-find-geckodriver-needed-by-selenium-python-package


#wget https://github.com/mozilla/geckodriver/releases/download/v0.19.0/geckodriver-v0.19.0-linux64.tar.gz
#tar -xvzf geckodriver-v0.19.0-linux64.tar.gz
#chmod +x geckodriver
#sudo pip install -U selenium
#sudo cp geckodriver /usr/local/bin/


# wget https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz
# tar -xvzf geckodriver-v0.11.1-linux64.tar.gz
# rm geckodriver-v0.11.1-linux64.tar.gz
# chmod +x geckodriver
# cp geckodriver /usr/local/bin/








# from BeautifulSoup import BeautifulSoup
# import urllib

# post_params = {
#     name : 'val1',
#     email : 'val2',
#     message : 'val3'
#         }
# post_args = urllib.urlencode(post_params)

# url = 'http://lucidleanlabs.com/'
# fp = urllib.urlopen(url, post_args)
# soup = BeautifulSoup(fp)

# import requests
# import lxml.html as lh


# def gender_genie(text, genre,message):
#     url = 'http://lucidleanlabs.com/'
#     caption = 'The Gender Genie thinks the author of this passage is:'

#     form_data = {
#         'name': text,
#         'email': genre,
#         'message':message,
#         'submit': 'submit',
#     }

#     response = requests.post(url, data=form_data)

#     tree = lh.document_fromstring(response.content)

#     return tree.xpath("//b[text()=$caption]", caption=caption)[0].tail.strip()


# if __name__ == '__main__':
#     print gender_genie('I have a beard!','test@gmail.com', 'blog')


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# # create a new Firefox session
# driver = webdriver.Firefox()
# driver.implicitly_wait(30)
# driver.maximize_window()

# # navigate to the application home page
# driver.get("http://www.google.com")

# # get the search textbox
# search_field = driver.find_element_by_id("lst-ib")
# search_field.clear()

# # enter search keyword and submit
# search_field.send_keys("Selenium WebDriver Interview questions")
# search_field.submit()

# # get the list of elements which are displayed after the search
# # currently on result page using find_elements_by_class_name  method
# lists= driver.find_elements_by_class_name("_Rm")

# # get the number of elements found
# print ("Found " + str(len(lists)) + "searches:")

# # iterate through each element and print the text that is
# # name of the search

# i=0
# for listitem in lists:
#    print (listitem)
#    i=i+1
#    if(i>10):
#       break

# # close the browser window
# driver.quit()












# import os
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path="/home/manikandan/Downloads/chromedriver")
# driver.get("http://stackoverflow.com")
# driver.quit()

# from selenium import webdriver

# driver = webdriver.Firefox()
# driver.get('http://www.python.org/')
# driver.save_screenshot('screenshot.png')
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()

# browser.get('http://www.yahoo.com')
# assert 'Yahoo' in browser.title

# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()




# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# browser = webdriver.Firefox()
# browser.get('http://www.google.com')
# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
# browser.save_screenshot('screenshot.png')
# browser.quit()


#screen shot




#from selenium import webdriver

#def mani(data):
# for i in data:
#     driver = webdriver.Firefox()
#     driver.get('http://www.%s.com'%(i))
#     driver.save_screenshot('img/%s.png'%(i))
#     driver.quit()


#data = ['google','yahoo','mindlogicx','ibm']


#mani(data)







# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# i = 2 # do it 2 times
# while i > 0:
#     driver = webdriver.Firefox()
#     driver.get("http://lucidleanlabs.com/")

#     def find_by_xpath(locator):
#         element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH, locator))
#         )

#         return element

#     class FormPage(object):
#         def fill_form(self, data):
#             import ipdb;ipdb.set_trace()
#             find_by_xpath('//input[@name = "name"]').send_keys(data['name'])
#             find_by_xpath('//input[@name = "email"]').send_keys(data['email'])
#             find_by_xpath('//input[@name = "x-message"]').send_keys(data['x-message'])
#             # find_by_xpath('//select[@name = "birthday_month"]').send_keys(data['month'])
#             # find_by_xpath('//select[@name = "birthday_day"]').send_keys(data['day'])
#             # find_by_xpath('//select[@name = "birthday_year"]').send_keys(data['year'])

#             return self # makes it so you can call .submit() after calling this function

#         def submit(self):
#             find_by_xpath('//input[@value = "Submit"]').click()

#     data = {
#         'name': 'Sheep',
#         'email': 'jess@sheeptest.com',
#         'x-message': 'Test',
#     }

#     FormPage().fill_form(data).submit()
#     driver.quit() # closes the webbrowser
#     i = i - 1



from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://127.0.0.1:8000/home/')
element = driver.find_element_by_name("name")
element.send_keys('hello')

element = driver.find_element_by_name("password")
element.send_keys('king')
# element.send_keys("some text");
driver.find_element_by_id("submit").click()
element.submit();
driver.quit()
