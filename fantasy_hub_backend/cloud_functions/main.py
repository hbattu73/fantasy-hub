import functions_framework
import json
import firebase_admin
from firebase_admin import db, auth
from espn_api import ESPN_Cloud_Requests
# CONSTANTS
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
PRO_TEAMS = {
    0 : 'FA',
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

firebase_admin.initialize_app(options={'databaseURL': DB_URL})

def authenticate_token(token):
    try:
        uid = auth.verify_id_token(token)['uid']
        print('User ID: ', uid)
    except Exception as err:
        print('Invalid user token:', err)
        return False
    return True

def box_scores(req, team_id, scoring_period, matchup_period):
    params = {
            'view': ['mMatchupScore', 'mScoreboard'],
            'scoringPeriodId': scoring_period,
    }
    filters = {"schedule":{"filterMatchupPeriodIds":{"value":[matchup_period]}}}
    headers = {'x-fantasy-filter': json.dumps(filters)}
    try:
        data = req.request_league(params=params, headers=headers)
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
                    # TODO:FIX HOW U CALC. POINTS
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
        print('Error in accessing box scores:', err)
        raise err

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        # Allows GET requests from any origin with the Content-Type
        # header and caches preflight response for an 3600s
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Authorization, Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    
    # Authenticate firebase user token
    if not authenticate_token(request.headers['Authorization']): 
        return ('Server Error: Token Authentication', 401, headers)
    
    data = request.args
    print(data)
    uid = data['uid']
    print('Validating league and cookie information...')
    # Authenticate input against ESPN's API
    swid = data['swid']
    espn_s2 = data['espn_s2']
    leagues = json.loads(data['leagues'])
    cookies = {
        'SWID': swid,
        'espn_s2': espn_s2
    }
    print(cookies, leagues)   
    cloud_requests = [ESPN_Cloud_Requests(year=2022, league_id=id, cookies=cookies) for id in leagues]
    scoring_range_map, team_id_map, matchup_map = {}, {}, {}  
    try:
        for req in cloud_requests:
            data = req.request_league(params={'view': ['mTeam', 'mSettings']})
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
            print('Successfully accessed team data for league', req.league_id)
    except Exception as err:
        print('Error in accessing league info:', err)
        return ('Invalid Cookie or League ID Input.', 404, headers)
    
    print('Ranges:', scoring_range_map)
    print('Team Ids:', team_id_map)
    print('Matchups:', matchup_map)
    # TODO: upload league name, icon, and id, etc somehow to database
    db_map = {}
    print('Calculating box scores...')
    try:
        for week in range(1, 19):
            print('Week:', week)
            scores = {} 
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
    except Exception as err:
        return ('Server Error: Error in Retrieving Dashboard', 404, headers)
    
    print('Writing to database location')
    ref = db.reference('/')
    stats_ref = ref.child('stats/' + uid)
    try:
        stats_ref.set(db_map)
        print('Successfully wrote stats to Firebase Realtime Database.')
        return ('Hello World!', 200, headers)
    except Exception as err:
        print('Error in saving stats to Firebase DB: ', err)
        return ('Database Error: Contact Site Owner for More Assistance', 404, headers)

    # return ('Hello World!', 200, headers)
