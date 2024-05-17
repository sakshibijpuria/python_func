# Works only if urls are present in HTML Content
import requests
import re

def get_social_media_handles(url):
    """Get social media handles from a webpage.
    
    Args:
        url (str): The URL of the webpage.
    
    Returns:
        dict: A dictionary containing social media handles for each platform.
    """
    # Local function to generate regex pattern for social media URLs
    def generate_regex_pattern():
        """Generate regex pattern for social media URLs.
        
        Returns:
            str: The regex pattern for social media URLs.
        """
        return r'(https?://(?:www\.)?(facebook\.com|twitter\.com|instagram\.com|linkedin\.com)/[^/?"]+)'

    response = requests.get(url)
    
    if response.status_code == 200:
        content = response.text
        social_media_handles = {}
        regex = generate_regex_pattern()
        matches = re.findall(regex, content)
        
        # If any matches are found, add them to the social media handles dictionary
        if matches:
            for match in matches:
                platform = match[1] 
                if platform not in social_media_handles:
                    social_media_handles[platform] = []
                social_media_handles[platform].append(match[0])
        
        return social_media_handles
    else:
        return {'error': f"Failed to fetch data from {url} with response {response.status_code}"}

url = "https://www.amazon.in/"
social_media_handles = get_social_media_handles(url)
print(social_media_handles)
