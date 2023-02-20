from api.utills.constraints import GameIdEnum, GameNoPlayersEnum

class TeamResponse:
    team: list
    total: int
    def __init__(self,teams) -> None:
        self.team = teams
        self.total = len(teams)

class Team:
    def create_team(self, json_data):
        game_type = json_data['gameType']
        players = json_data['players']
        teams = self.__get_teams(game_type, players)
        response =TeamResponse(teams)
        return response, len(teams) > 0

    def get_players_per_team(self, game_type):
        no_of_players = 0
        if GameIdEnum.CRICKET.value == game_type:
            no_of_players = GameNoPlayersEnum.CRICKET.value 
        elif GameIdEnum.CHESS.value == game_type:
            no_of_players = GameNoPlayersEnum.CHESS.value
        return no_of_players

    def __get_teams(self, game_type, players):
        players_per_team = self.get_players_per_team(game_type)
        if players_per_team == 0:
            return []
        team_start_char_ancii = 97
        id = 1
        teams = []
        for index in range(int(len(players)/players_per_team)):
            team = {
                "id": id,
                "name": f"Team - {chr(team_start_char_ancii).upper()}",
                "gameType": game_type,
                "players": [players[index * players_per_team + player_index] for player_index in range(players_per_team)]
            }
            id = id + 1
            team_start_char_ancii = team_start_char_ancii + 1
            teams.append(team)
        return teams
