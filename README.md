# Web-Scraping-Challenge

Step 1: Webscraping
Utilized splinter and Beautiful Soup through jupyter notebook to scrape different websites. 
1. Scraped the latest news headline and blurb from NASA's Mars website.
2. Scraped the latest space image in the Mars category from NASA's Jet Propulsion Laboratory.
3. Scraped a table of Mars data from space-facts website. Used a loop to get data from each row and added the data to a new list. Merged the lists together into a dataframe then exported as an HTML table to use on my website.
4 . Scraped the USGS Astrogeology website to get photos of all 4 of Mars' hemispheres. Used a loop to click on a link by partial text, save the image URL and title to a dictionary, then return to the previous page and do the same thing for the next 3 images. The image dictionaries were saved as a list 

Setp 2: MongoDB and Flask Application
Converted Jupyter Notebook to python script using a function called scrape that executed the code from jupyter notebook.
Created a python dictionary to combine all the scraped data. Using flask, the dictionary was stored in Mongo which was then called on using render_template to populate the HTML page with the images and headlines.
Step 3: Submission
The instructions say at this point to create a new repository and only submit the jupyter notebook and screen shots of the final application. I contacted askBCS and was informed to just turn in this repo for the project and to not create a new one. 
