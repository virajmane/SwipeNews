import requests
import json
from bs4 import BeautifulSoup
import random

def start():
    categories = ['india', 'business', 'politics', 'sports', 'technology', 'startups', 'entertainment', 'hatke', 'international', 'automobile', 'science', 'travel', 'miscellaneous', 'fashion', 'education']
    url = f'https://www.inshorts.com/en/read/{categories[random.randint(0, len(categories)-1)]}'

    response = requests.get(url)
    html_data = response.text

    soup = BeautifulSoup(html_data, 'html.parser')

    script_tag = soup.find('script', text=lambda x: x and 'window.__STATE__ =' in x)

    if script_tag:
        # Extract the content of the script tag
        script_content = script_tag.text

        json_content = script_content.replace('window.__STATE__ = ', '')

        try:
            # Load the JSON content into a Python dictionary
            state_data = json.loads(json_content[:-1])
            #return state_data
            lst2 = []
            #return i['news_obj']['title']
            # Display the resulting dictionary
            for i in state_data["news_list"]["list"]:
                lst = []
                return [i['news_obj']['title'], i['news_obj']['content'], i['news_obj']['image_url'], i['news_obj']['hash_id']]
                lst.append(i['news_obj']['content'])
                lst.append(i['news_obj']['image_url'])
                lst2.append(lst)
            return lst


        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        
    else:
        print("Script tag with window.__STATE__ not found.")