import requests
import json
# CONSTANTS
BASE_ENDPOINT = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/'

# Class object to retrieve JSON data usinh ESPN credentials
class ESPN_Cloud_Requests:
    def __init__(self, year: int, league_id: int, cookies: dict):
        self.year = year
        self.league_id = league_id
        self.cookies = cookies
        self.ENDPOINT = BASE_ENDPOINT + str(year)
        self.LEAGUE_ENDPOINT = BASE_ENDPOINT + str(year) + '/segments/0/leagues/' + str(league_id)
    
    def request_league(self, params: dict = None, headers: dict = None):
        endpoint = self.LEAGUE_ENDPOINT
        print('Requesting: ', endpoint)
        res = requests.get(endpoint, params=params, headers=headers, cookies=self.cookies)
        try:
            if res.status_code >= 400:
                res.raise_for_status()
        except Exception as err:
            raise err
        else:
            print('Accessing data for league', self.league_id, 'using params:', params)
            return res.json()

    
