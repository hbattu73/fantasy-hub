import requests
import json
import firebase_admin # type: ignore
from firebase_admin import db # type: ignore
BASE_ENDPOINT = 'https://fantasy.espn.com/apis/v3/games/ffl/seasons/'
BASE_PLAYER_HEADSHOT_URL = 'https://a.espncdn.com/i/headshots/nfl/players/full/'
BASE_TEAM_HEADSHOT_URL = 'https://a.espncdn.com/i/teamlogos/nfl/500/'
POSITIONS = {
    1: 'QB',
    2: 'RB',
    3: 'WR',
    4: 'TE',
    5: 'K',
    6: '', 
    7: 'P',
    8: '',
    9: 'DL',
    10: 'DE',
    11: 'LB',
    12: 'CB',
    13: 'S',
    14: 'HC',
    15: 'TQB',
    16: 'D/ST'
}
LINEUP_SLOTS = {
    0: 'QB',
    1: 'TQB',
    2: 'RB',
    3: 'RB/WR',
    4: 'WR',
    5: 'WR/TE',
    6: 'TE',
    7: 'OP',
    8: 'DT',
    9: 'DE',
    10: 'LB',
    11: 'DL',
    12: 'CB',
    13: 'S',
    14: 'DB',
    15: 'DP',
    16: 'D/ST',
    17: 'K',
    18: 'P',
    19: 'HC',
    20: 'BE',
    21: 'IR',
    22: '',
    23: 'RB/WR/TE',
    24: 'ER',
    25: 'Rookie',
}
PRO_TEAMS = {
    0 : 'None',
    1 : 'ATL',
    2 : 'BUF',
    3 : 'CHI',
    4 : 'CIN',
    5 : 'CLE',
    6 : 'DAL',
    7 : 'DEN',
    8 : 'DET',
    9 : 'GB',
    10: 'TEN',
    11: 'IND',
    12: 'KC',
    13: 'LV',
    14: 'LAR',
    15: 'MIA',
    16: 'MIN',
    17: 'NE',
    18: 'NO',
    19: 'NYG',
    20: 'NYJ',
    21: 'PHI',
    22: 'ARI',
    23: 'PIT',
    24: 'LAC',
    25: 'SF',
    26: 'SEA',
    27: 'TB',
    28: 'WSH',
    29: 'CAR',
    30: 'JAX',
    33: 'BAL',
    34: 'HOU'
}
DB_URL = 'https://fantasy-hub-c58bf-default-rtdb.firebaseio.com/'

class ESPN_Cloud_Requests:
    def __init__(self, year: int, league_id: int=None, cookies: dict=None):
        self.year = year
        self.league_id = league_id
        self.cookies = cookies
        self.ENDPOINT = BASE_ENDPOINT + str(year)
        self.LEAGUE_ENDPOINT = BASE_ENDPOINT + str(year) + '/segments/0/leagues/' + str(league_id)

    def league_get(self, params: dict = None, headers: dict = None, extend: str = ''):
        endpoint = self.LEAGUE_ENDPOINT + extend
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

    def get_league(self):
        params = {
            'view': ['mTeam', 'mRoster', 'mMatchup', 'mSettings', 'mStandings']
        }
        data = self.league_get(params=params)
        return data

    def get_pro_schedule(self):
        params = {
            'view': 'proTeamSchedules_wl'
        }
        endpoint = self.ENDPOINT
        r = requests.get(endpoint, params=params, cookies=self.cookies)
        return r.json()
    
# box scores
def box_scores(req, team_id, scoring_period, matchup_period):
    params = {
            'view': ['mMatchupScore', 'mScoreboard'],
            'scoringPeriodId': scoring_period,
    }
    filters = {"schedule":{"filterMatchupPeriodIds":{"value":[matchup_period]}}}
    headers = {'x-fantasy-filter': json.dumps(filters)}
    try:
        data = req.league_get(params=params, headers=headers)
        schedule = data['schedule']
        team_players, opp_players = [], []
        for matchup in schedule:
            team = None
            if matchup['home']['teamId'] == team_id: team = 'home'
            elif 'away' in matchup and matchup['away']['teamId'] == team_id: team = 'away'
            if team:
                for player in matchup[team]['rosterForCurrentScoringPeriod']['entries']: 
                    if player['lineupSlotId'] == 20 or player['lineupSlotId'] == 21: continue
                    player_id = player['playerId']
                    meta = player['playerPoolEntry']['player']
                    name = meta['fullName']
                    pos = POSITIONS[meta['defaultPositionId']]
                    pro_team = PRO_TEAMS[meta['proTeamId']]
                    headshot = BASE_PLAYER_HEADSHOT_URL + str(player_id) + '.png' if player_id > 0 else BASE_TEAM_HEADSHOT_URL + pro_team.lower() + '.png'
                    # TODO:FIX HOW U CALC. POINTS
                    stats = meta['stats']
                    points, projected, bye = 0.0, 0.0, True
                    if len(stats) > 1:
                        bye = False
                        points = round(stats[0]['appliedTotal'], 1) if stats[0]['statSourceId'] == 0 else round(stats[1]['appliedTotal'], 1)
                        projected = round(stats[1]['appliedTotal'], 1) if stats[1]['statSourceId'] == 1 else round(stats[0]['appliedTotal'], 1)
                    team_players.append((player_id, name, pos, pro_team, headshot, points, projected, bye))
                team = 'away' if team == 'home' else 'home'
                for player in matchup[team]['rosterForCurrentScoringPeriod']['entries']: 
                    if player['lineupSlotId'] == 20 or player['lineupSlotId'] == 21: continue
                    player_id = player['playerId']
                    meta = player['playerPoolEntry']['player']
                    name = meta['fullName']
                    pos = POSITIONS[meta['defaultPositionId']]
                    pro_team = PRO_TEAMS[meta['proTeamId']]
                    headshot = BASE_PLAYER_HEADSHOT_URL + str(player_id) + '.png' if player_id > 0 else BASE_TEAM_HEADSHOT_URL + pro_team.lower() + '.png'
                    stats = meta['stats']
                    points, projected, bye = 0.0, 0.0, True
                    if len(stats) > 1:
                        bye = False
                        points = round(stats[0]['appliedTotal'], 1) if stats[0]['statSourceId'] == 0 else round(stats[1]['appliedTotal'], 1)
                        projected = round(stats[1]['appliedTotal'], 1) if stats[1]['statSourceId'] == 1 else round(stats[0]['appliedTotal'], 1)
                    opp_players.append((player_id, name, pos, pro_team, headshot, points, projected, bye))
                break
        return team_players, opp_players
    except Exception as err:
        print('Error in accessing box scores ->', err)

# 858357711, 131299 - ids will come in a list
leagues, swid, espn_s2 = [858357711, 131299], '{27995341-0F75-4AD5-A749-D57E542FC49B}', 'AEBBBB9mu/HhG4GSZYieKPWAZEiv6LYv4HVTAtUGUt32GXFH8OqaxKrm+JIIP6zaiRB8XGWotWx0PuOE7pdENgwrkYF/uVWnPlgIc9AW3vNVo5+3ldzLRbXy14zklaAxgHAVcdDE9fkOQoFuhCAvVKjZt/QYe0/gnDHOne0W3mXlENvrH12RXkQpA6NGMKlgkzeTmQiKZHniwtfDP8sJESR0nzKy8dyXPUCyUwt6R/V9RY6PKzoYgAlqp9dYNpqzVNXpx1LFlhxrjHtgEK/Epr7C'
cookies = {
    'SWID': swid,
    'espn_s2': espn_s2
}
cloud_requests = [ESPN_Cloud_Requests(year=2022, league_id=id, cookies=cookies) for id in leagues]
scoring_range_map, team_id_map, matchup_map = {}, {}, {}

print('Validating league and cookie information...')
for req in cloud_requests:
    try:
        # try league data retrieval
        data = req.league_get(params={'view': ['mTeam', 'mSettings']})
        # calculate scoring ranges (weeks)
        scoring_period_id = data['scoringPeriodId']
        first_scoring_period = data['status']['firstScoringPeriod']
        final_scoring_period = data['status']['finalScoringPeriod']
        current_week = scoring_period_id if scoring_period_id <= final_scoring_period else final_scoring_period
        scoring_range_map[req.league_id] = (first_scoring_period, current_week+1)
        # map scoring periods to matchup periods
        matchup_periods = data['settings']['scheduleSettings']['matchupPeriods']
        scoring_to_matchup_ids = {}
        for matchup_id in matchup_periods:
            for scoring_period in matchup_periods[matchup_id]:
                scoring_to_matchup_ids[scoring_period] = matchup_id
        matchup_map[req.league_id] = scoring_to_matchup_ids
        # get team id for each league
        teams = data['teams']
        for team in teams:
            if team['owners'] and req.cookies['SWID'] in set(team['owners']):
                team_id_map[req.league_id] = team['id']
                break
        print('Sucessfully accessed team data for league', req.league_id)
    except Exception as err:
        print('Error in accessing league info ->', err)
        # return with 404 in server code
print('scoring_range_map', scoring_range_map)
print('team_id_map', team_id_map)
print('matchup_map', matchup_map)
# exit(1)
db_map = {}
print('Calculating box scores...')
for week in range(1, 19):
    print('Week:', week)
    scores = {} 
    root, conflict, boo = set(), set(), set()
    for req in cloud_requests:
        if week not in range(scoring_range_map[req.league_id][0], scoring_range_map[req.league_id][1]): continue
        team_players, opp_players = box_scores(req, team_id_map[req.league_id], week, int(matchup_map[req.league_id][week]))
        for player in team_players:
            player_id = player[0]
            if player_id not in scores: 
                scores[player_id] = {}
                scores[player_id]['Name'] = player[1]
                scores[player_id]['Position'] = player[2]
                scores[player_id]['Team'] = player[3]
                scores[player_id]['Headshot'] = player[4]
                scores[player_id]['Points'] = player[5]
                scores[player_id]['Projected'] = player[6]
                scores[player_id]['Bye'] = player[7]
                scores[player_id]['Status'] = 'ROOT'
            if scores[player_id]['Status'] == 'BOO': scores[player_id]['Status'] = 'CONFLICTED'

        for player in opp_players:
            player_id = player[0]
            if player_id not in scores: 
                scores[player_id] = {}
                scores[player_id]['Name'] = player[1]
                scores[player_id]['Position'] = player[2]
                scores[player_id]['Team'] = player[3]
                scores[player_id]['Headshot'] = player[4]
                scores[player_id]['Points'] = player[5]
                scores[player_id]['Projected'] = player[6]
                scores[player_id]['Bye'] = player[7]
                scores[player_id]['Status'] = 'BOO'
            if scores[player_id]['Status'] == 'ROOT': scores[player_id]['Status'] = 'CONFLICTED'

    db_map[week] = scores

print(db_map)

print('Initializing Database:', DB_URL)
try:
    firebase_admin.initialize_app(options={'databaseURL': DB_URL})
    print('Successful Initialization')
except Exception as err:
    raise err

print('Writing to database location')
ref = db.reference('/')
stats_ref = ref.child('stats')
try:
    stats_ref.set(db_map)
    print('Successfully wrote stats to Firebase Realtime Database.')
except Exception as err:
    print('Error in saving stats to Firebase DB: ', err)