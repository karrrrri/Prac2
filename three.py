#В гугл коллаб
from bs4 import BeautifulSoup
import requests
def generate_groups():

    url = 'http://kispython.ru/'
    request = requests.get(url)
    soup = BeautifulSoup(request.text, 'html.parser')

    buttons = soup.find_all('a', {'class': 'btn btn-outline-primary mb-2 mr-3'})
    groups = [button.get_text().replace('\n', '').replace(' ', '') for button in buttons]

    return groups

a = generate_groups()
print(a)
