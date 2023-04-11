#!/usr/bin/python
import sys
from bs4 import BeautifulSoup
import requests, json
from requests.exceptions import HTTPError
from espn.espn_api import ESPN_Requests

TRADE_VALS_DIR = '../trade_values/'
FILTER_PUNCT = '[]/'

def dump_json(file, values):
    json_file = TRADE_VALS_DIR + file
    with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(values, f, ensure_ascii=False)
            print('Successfuly dumped JSON object to file: ', json_file)

def fetch_players():
    espn_request = ESPN_Requests(year=2022)     # use personal cookies
    name_to_id, id_to_name = espn_request.player_id_maps()
    return name_to_id, id_to_name

def process_name(name):
    # hardcode slight disparities in names from ESPN's pool and FantasyPro's pool
    if name == 'Patrick Mahomes II': return 'Patrick Mahomes'
    elif name == 'Ken Walker III': return 'Kenneth Walker III'
    elif name == 'D.J. Chark Jr.': return 'DJ Chark'
    name = name.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    return name

def main(argv):
    # Handle invalid number of arguments
    if len(argv) != 3:
        print("Arguments must be in form: scraper.py <URL> <week> <file_name>")
        sys.exit(1)
    # Request exception handling
    try:
        page = requests.get(argv[0])
    except HTTPError as http_err:
        print('An HTTP error has occured: ', http_err)
        sys.exit(1)
    except Exception as err:
        print('A Non-HTTP error occurred: ', err)
        sys.exit(1)
    # Process the BeautifulSoup of the page
    if page.status_code == requests.codes.ok:
        print('Successfully retrieved trade values.')
        bs = BeautifulSoup(page.text, 'lxml')
        # 4 tables for trade values -> QB, RB, WR, TE in that order
        tables = bs.find_all('table')
        positions = ["QB", "RB", "WR", "TE"]
        trade_values = {}   # dictionary to store player dictionaries
        # trade_values['Week'] = argv[1]  # store the current week
        name_to_id, id_to_name = fetch_players()
        # print(name_to_id)
        for i in range(len(tables)):
            # each row of table that is NOT the 1st row contains player trade values
            players = tables[i].find_all('tr')[1:]
            for p in players:
                # the first 4 columns are what we need -> Name, Team, Value, Change
                vals = [v.getText() for v in p.find_all('td')[:4]]
                # TODO: process strings before checking for equality in name_to_id
                name = process_name(vals[0].translate(str.maketrans('', '', FILTER_PUNCT)))
                id_ = name_to_id[(name, positions[i])]
                headshot = id_to_name[id_][1]
                data = {}
                data['Name'] = name
                data['Headshot'] = headshot
                data['Position'] = positions[i]
                data['Team'] = vals[1]
                data['Value'] = float(vals[2])
                data['Change'] = vals[3]
                # store by ESPN player id
                trade_values[id_] = data
        dump_json(argv[2], trade_values)
    else:
        print('Unsuccesful Request with valid URL. Status Code: ', page.status_code)

if __name__ == '__main__':
    main(sys.argv[1:])