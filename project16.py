import requests
from bs4 import BeautifulSoup

def get_github_profile_image():
  
    github_url = input("Enter the GitHub profile URL: ")

 
    try:
        response = requests.get(github_url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

   
    soup = BeautifulSoup(response.content, "html.parser")

 
    image_tag = soup.find("img", class_="avatar avatar-user")
    
    if image_tag:
        
        image_url = image_tag['src']
        print(f"Profile image link: {image_url}")
    else:
        print("Could not find profile image.")

get_github_profile_image()
