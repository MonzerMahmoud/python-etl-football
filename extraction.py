import requests
import json
import pandas as pd

token = "bd5ae1beb98f4adab67518ec06df33e0"

headers = {
    "X-Auth-Token" : token
}

class Extraction:

    def __init__(self):
        print("Extraction")
        #self.data_sources = json.load(open("data_sources.json"))
        #self.api = self.data_sources["data_sources"]["api"]
        self.api = "http://api.football-data.org/v2/"

    def get_Matches(self) -> pd.DataFrame:
        url = self.api + "competitions/PL/matches?dateFrom=2022-03-10&dateTo=2022-03-25"
        response = requests.get(url, headers=headers)
        matchId_arr = []
        date_arr = []
        status_arr = []
        match_day_arr = []
        home_team_arr = []
        home_team_id_arr = []
        away_team_arr = []
        away_team_id_arr = []
        winner_arr = []
        score_arr = []
        for match in response.json()['matches']:
            matchId_arr.append(match['id'])
            date_arr.append(match['utcDate'])
            status_arr.append(match['status'])
            match_day_arr.append(match['matchday'])
            home_team_arr.append(match['homeTeam']['name'])
            home_team_id_arr.append(match['homeTeam']['id'])
            away_team_arr.append(match['awayTeam']['name'])
            away_team_id_arr.append(match['awayTeam']['id'])
            winner_arr.append(match['score']['winner'])
            score_arr.append(str(match['score']['fullTime']['homeTeam'])+":"+str(match['score']['fullTime']['awayTeam']))

        match_data = {
            "matchId" : matchId_arr,
            "date" : date_arr,
            "status" : status_arr,
            "match_day" : match_day_arr,
            "home_team" : home_team_arr,
            "home_team_id" : home_team_id_arr,
            "away_team" : away_team_arr,
            "away_team_id" : away_team_id_arr,
            "winner" : winner_arr,
            "score" : score_arr
        }
        
        matches_df = pd.DataFrame(match_data, columns=["matchId", "date", "status", "match_day", "home_team", "home_team_id", "away_team", "away_team_id", "winner", "score"])
        return matches_df