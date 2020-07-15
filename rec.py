import json
import requests
from colorama import init, Fore
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time

init()

URL = 'https://www.recreation.gov/api/permits/233273/availability/month?'
headers = {
    "User-Agent": UserAgent().random
}
params = {
    "start_date": '2020-07-01T00:00:00.000Z'
}

found_colch = False
found_core = False
while True:
    page = requests.get(URL, headers=headers, params=params)

    resp = page.json()
    with open('resp.json', 'w') as f:
        f.write(json.dumps(resp, indent=2))

    avail = resp['payload']['availability']['30']['date_availability']
    # check all dates in range
    for date, info in avail.items():
        if date != "2020-07-03T00:00:00Z" and info['remaining'] != 0:
            found_core = True
            print(Fore.RED + 'AVAILABILITY FOUND COREEEE')
            print(date)
            print(info)
    if not found_core:
        print('--nothing yet core')
    else:
        print(Fore.RED + 'FOUND STUFF CORE')
    
    avail = resp['payload']['availability']['29']['date_availability']
    # check all dates in range
    for date, info in avail.items():
        if date != "2020-07-03T00:00:00Z" and info['remaining'] != 0:
            found_colch = True
            print(Fore.RED + 'AVAILABILITY FOUND COLCH')
            print(date)
            print(info)
    if not found_colch:
        print('--nothing yet colch')
    else:
        print(Fore.RED + 'FOUND STUFF COLCH')
    
    time.sleep(1) 


# soup = BeautifulSoup(page.content)

# overnight = soup.find(id='recApp')
# print(overnight)