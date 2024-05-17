from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_social_media_handles(url):
    """Get social media handles from a webpage.
    
    Args:
        url (str): The URL of the webpage.
    
    Returns:
        dict: A dictionary containing social media handles for each platform.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    social_media_handles = {}
    
    # Find social media links
    social_media_selector = 'a[href*="facebook.com"], a[href*="twitter.com"], a[href*="instagram.com"], a[href*="linkedin.com"]'
    social_media_links = driver.find_elements(By.CSS_SELECTOR, social_media_selector)
    
    # Extract social media handles from the URLs and store them in the dictionary
    for link in social_media_links:
        platform = link.get_attribute('href').split('/')[2]
        if platform not in social_media_handles:
            social_media_handles[platform] = []
        social_media_handles[platform].append(link.get_attribute('href'))
    
    driver.quit()
    return social_media_handles


# url = "https://give.do/"
url ="https://www.microsoft.com/en-in"
# url = "https://www.amazon.in/"
social_media_handles = get_social_media_handles(url)
print(social_media_handles)
