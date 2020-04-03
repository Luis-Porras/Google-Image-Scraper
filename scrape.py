from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from math import ceil
import os
import base64
import time 
import getpass
import platform

def search(driver,term):
    
    #Specify search term and sends a google query for the term
    driver.get('https://google.com')
    WebDriverWait(driver,1)
    search_box = driver.find_element_by_class_name('gLFyf')
    search_box.send_keys(term)
    search_box.send_keys(Keys.ENTER)

    #Finds the google "Images" box for the search term and clicks on it
    google_image_box = driver.find_element_by_link_text('Images')
    google_image_box.click()
    
def create_folder():  
    
    #Attempts to create new folder in Downloads. 
    #If it already exists, user is asked if they would like to save their images to existing folder 
    #or make new folder
    
    folder_name =  input('What would you like to name your new folder of images? You\'ll find this folder in your Downloads: ')
    valid_folder_name = False
    
    while not valid_folder_name:
        try:
            if platform.system() == 'Darwin':
                os.mkdir(f'/Users/Luis/Downloads/{folder_name}')
            elif platform.system() == 'Windows':
                os.mkdir(f'{homedir}\Downloads\\{folder_name}')
                
            valid_folder_name = True
            
        except FileExistsError: 
            
            folder_response = int(input(f'''The folder named \'{folder_name}\' already exists. Would you like to add your pictures to the existing folder, or save them to a new folder name? \n Press 1 to save them to the existing folder. 
            \n Press 2 to save them to a new folder \n Response:  '''))
            
            if folder_response == 1:
                print(f'New images will be downloaded to the existing \'{folder_name}\' folder')
                return folder_name
                
            elif folder_response == 2:
                folder_name =  input('''What would you like to name your new folder of images? \n You\'ll find this folder in your Downloads: ''')
            
            else:
                print('Please type 1 or 2 as your response....')
                time.sleep(1)
                
    return folder_name

def load_images(driver, images_to_retrieve = 100):
    
    #function using javascript to scroll to the bottom of a page.
    def scroll(driver):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
    #calculates necessary page scrolls to load the amount of images the user has asked for.
    scroll_amount = ceil((images_to_retrieve/90))
    
    #begins scrolling, but also checks if the "show more results" button needs to be pressed to keep scrolling.
    for i in range(scroll_amount):
        try:
            
            driver.find_element_by_css_selector('input.mye4qd').click()
            time.sleep(2)
            scroll(driver)
            time.sleep(2)    
            
        except:
            
            scroll(driver)
            time.sleep(2)
            
        
#Clicks on an image thumbnail and gets the uri of the newly expanded image. 
#The images returned from this function are base64 encoded images.
def get_images(driver, images_to_retrieve):
    
    elements = driver.find_elements_by_class_name('rg_i')
    images = []
    
    for i in elements[:images_to_retrieve+1]:
        i.click()
        time.sleep(2)
        real_image = driver.find_element_by_class_name('n3VNCb')
        if 'data:image' in real_image.get_attribute('src'):
            images.append(real_image.get_attribute('src'))
            
    return images
    
    
#Images must be decoded, and then can be saved as an image to a desired path               
def decode_and_save(images,folder_name):
    
    homedir = os.path.expanduser('~')
    
    if platform.system() == 'Darwin':
        download_path = homedir+'/Downloads/'+folder_name+'/image'
    elif platform.system() == 'Windows':
        download_path = homedir+'\Downloads\\'+folder_name+'\image'
    
    #Retrieves the base64 encoded picture and it's corresponding file extension(.png, .jpg, .gif, .tif, etc.)
    for i in images: 
        head = i.split(',')[0]
        data = i.split(',')[1]
        file_type = head.split('/')[1].split(';')[0]
        decoded = base64.b64decode(data)
        
        #writes each newly decoded picture to a sub-directory in the Downloads directory
        with open(f'{download_path}{images.index(i)}.{file_type}', 'wb') as f:
            f.write(decoded)         
def scrape(driver_path):
    search_term = input('What images would you like to search on Google? ')
    image_amount= int(input('How many pictures would you like to download? '))
    folder_name =  create_folder()
    wd = webdriver.Chrome(driver_path)
    
    search(wd,search_term)
    load_images(wd, image_amount)
    images = get_images(wd,image_amount)
    decode_and_save(images, folder_name)
    wd.quit()


#specify location of webdriver 
driver_path = '/Users/Luis/Downloads/ChromeDriver'

#call function
scrape(driver_path)



