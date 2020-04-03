import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import base64



#Specify search term and sends a google query for the term
search_term = 'cats'
wd = webdriver.Chrome('../../Downloads/ChromeDriver')
wd.get('https://google.com')
WebDriverWait(wd,1)
search_box = wd.find_element_by_class_name('gLFyf')
search_box.send_keys(search_term)
search_box.send_keys(Keys.ENTER)

#Finds the google "Images" box for the search term and clicks on it
google_image_box = wd.find_element_by_class_name('qs')
google_image_box.click()

#must scroll to bottom of the images page, or else it does not grab the correct url/src attribute. 
#this function uses simple javascript to scroll to the bottom of the page
def scroll(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        

scroll(wd)

#Returns a list of all the images on the page
images = wd.find_elements_by_class_name('rg_i')

#Clicks on an image thumbnail and gets the url of the newly expanded image. 
urls = []
for i in images:
    i.click()
    time.sleep(2)
    real_img = wd.find_element_by_class_name('n3VNCb')
    print(real_img.get_attribute('src'), '\n\n')

    if 'data:image' in real_img.get_attribute('src'):
    	
    # else:
    # 	print(real_img.get_attribute('src'))




 

    
    
