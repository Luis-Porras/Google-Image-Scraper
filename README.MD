
***Description***

Collects images and saves them to your local Downloads folder. Works on Windows and Unix-based operating systems. The motivation for this project was to create a tool that would free users from relying on online datasets. The Google-Image-Scraper will run in the background, saving users the time and stress that usually comes with image hunting for ML classification problems, website dummy data, or an other projects requiring image collection. 


***Basic Requirements***

Python3: https://www.python.org/downloads/ 
Selenium: https://selenium-python.readthedocs.io/installation.html
Web Driver: https://chromedriver.chromium.org/downloads 


***How To Use***

1. After downloading the required dependencies, head to the <code>scrape.py</code> file and change the <code>driver_path</code> variable at the bottom of the file to the location of your webdriver. 

<code>driver_path = /Users/Luis/Downloads/chromedriver</code>

2. Run the scrape.py file in a command line interface.

<code>python3 scrape.py</code>

3. Follow the console prompts, which ask:
-'What images would you like to search on Google? '
-'How many pictures would you like to download? '
-'What would you like to name your new folder of images? You'll find this folder in your Downloads: '

The scraper will begin shortly after specifying the new folder name. You will have your pictures downloaded 

It takes approximately 3-4 seconds to scrape each image. This is because of a required sleep timer to allow pictures to render in the browser before attempting to retrieve it. 


