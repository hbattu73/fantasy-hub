import requests
import json
from .constants import BASE_ENDPOINT, POSITIONS, COOKIES, BASE_PLAYER_HEADSHOT_URL

class ESPN_Requests:
    def __init__(self, year: int, league_id: int=None, cookies: dict=None):
        self.year = year
        self.league_id = league_id
        self.cookies = cookies if cookies else COOKIES
        self.ENDPOINT = BASE_ENDPOINT + str(year)
        self.LEAGUE_ENDPOINT = BASE_ENDPOINT + str(year) + '/segments/0/leagues/' + str(league_id)

    def request_players(self):
        params = {'view': 'players_wl'}
        filters = {"filterActive": {"value": True}}
        headers = {'x-fantasy-filter': json.dumps(filters)}
        endpoint = self.ENDPOINT + '/players'
        print('Requesting: ', endpoint)
        res = requests.get(endpoint, params=params, headers=headers, cookies=self.cookies)
        try:
            if res.status_code >= 400:
                res.raise_for_status()
        except Exception as err:
            print('Error in retrieving players: ', err)
        else:
            print('Successfully retrieved players!')
            return res.json()
    
    def player_id_maps(self):
        name_to_id = {}  # (name, pos) : (id)
        id_to_name = {}  # (id) : (name, headshot)
        players = self.request_players()
        for p in players:
            pos = POSITIONS[p['defaultPositionId']]
            name_to_id[(p['fullName'], pos)] = p['id']
            id_to_name[p['id']] = (p['fullName'], self.headshot_url(p['id']))
        return name_to_id, id_to_name
    
    def headshot_url(self, id):
        return BASE_PLAYER_HEADSHOT_URL + str(id) + '.png'

