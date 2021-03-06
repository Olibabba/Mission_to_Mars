from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt

import pandas as pd

def scrape_all():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    news_title, teaser = mars_news(browser)
    
    data = {
      "news_title": news_title,
      "news_paragraph": teaser,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now(),
      "mars_images": mars_images(browser)
    }

    browser.quit()  
    return data

def mars_news(browser):
    # Visit the Mars Nasa News site
    url = 'https://redplanetscience.com/'
    browser.visit(url)
    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        
        teaser = slide_elem.find('div', class_='article_teaser_body').get_text()
    except AttributeError:
        return None, None

    return teaser, news_title

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        img_full_url = f'{url}/{img_url_rel}'

    except AttributeError:
        return None

    return img_full_url

def mars_facts():
    try:
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
      return None

    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    return df.to_html(classes="table-responsive table-striped",index=False)

def mars_images(browser):
    # Visit URL
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)
    
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
    
    return hemisphere_image_urls
    
    

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())