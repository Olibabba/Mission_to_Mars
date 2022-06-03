#!/usr/bin/env python
# coding: utf-8

# In[49]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd


# In[107]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Visit the Mars Nasa News site
url = 'https://redplanetscience.com/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


teaser = slide_elem.find('div', class_='article_teaser_body').get_text()
teaser


# ### Featured Images

# In[8]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[12]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[13]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[20]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_full_url = f'{url}/{img_url_rel}'
img_full_url


# ### Mars Facts Scrape

# In[26]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[27]:


df.to_html()


# In[6]:


browser.quit()


# In[ ]:


db.zoo.insertOne({name: 'Giggles', species: 'Elephant', age: 55, hobbies: ['sloshing', 'trumpeting', 'stomping']})
db.zoo.insertOne({name: 'Sharp', species: 'Porcupine', age: 5, hobbies: ['poking', 'proding', 'sticking']})
db.zoo.insertOne({name: 'Pronto', species: 'Tortise', age: 150, hobbies: ['Chewing', 'Racing', 'Chewing']})


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[108]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[56]:


# html = browser.html
# find_mars = soup(html, 'html.parser')


# In[59]:


# items = find_mars.find_all('div', {'class': 'item'})


# In[65]:


# items[0].a['href']


# ### got the links

# In[66]:


# links = [url + x.a['href'] for x in items]
# links


# #### ^^^^^

# In[77]:


# hemisphere_image_urls = []

# for link in links:
#     browser.visit(link)
#     hemisphere_image_urls.append(browser.find_by_value('Sample')['href'])

#     browser.back()

# browser.quit()

# hemisphere_image_urls


# In[84]:


# browser.visit('https://marshemispheres.com/cerberus.html')


# In[86]:


# browser.find_by_tag('h2').text


# In[76]:


# browser.find_by_value('Sample')['href']


# In[101]:


browser.back()


# In[109]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
html = browser.html
find_mars = soup(html, 'html.parser')

items = find_mars.find_all('div', {'class': 'item'})
links = [url + x.a['href'] for x in items]
links

hemisphere_image_urls = []

for link in links:
    browser.visit(link)
    temp_title = browser.find_by_tag('h2').text
    temp_url = browser.find_by_value('Sample')['href']
    
    hemisphere_image_urls.append({'Img_Title': temp_title, 'Img_URL': temp_url})
    
    browser.back()


# In[110]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[111]:


# 5. Quit the browser
browser.quit()


# In[ ]:




