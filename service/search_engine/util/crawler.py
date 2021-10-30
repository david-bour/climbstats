import requests
from bs4 import BeautifulSoup

def crawl_athletes():
    """ Returns a list of IFSC Athletes """
    url = 'https://www.ifsc-climbing.org/index.php/athletes'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    athletes = [node.text.strip() for node in soup.find_all(attrs={"class":"name"})]
    return athletes

def athlete_info(name):
    """ Returns one or more athletes info from IFSC """
    url = "https://www.ifsc-climbing.org/index.php?option=com_ifsc&task=athletes.search"
    request = requests.post(url, data={'search_string': name})
    return request.json()
