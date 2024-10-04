import psycopg2
import json

# connect to database
conn = psycopg2.connect(
    dbname = "okc",
    user = "okcapplicant",
    host = "localhost"
)

cur = conn.cursor()

# load teams 
with open('raw_data/teams.json') as f:
    teams_data = json.load(f)
    for team in teams_data:
        cur.execute("INSERT INTO teams (id, name) VALUES (%s, %s)", (team['id'],team['name']))

# load Players
with open('raw_data/players.json') as f:
    players_data = json.load(f)
    for player in players_data:
        cur.execute("INSERT INTO players (id, name) VALUES (%s, %s)", (player['id'], player['name']))

# Load Games and Player Stats
with open('raw_data/games.json') as f:
    games_data = json.load(f)
    for game in games_data:
        # Insert game into games table
        cur.execute(
            "INSERT INTO games (id, date, home_team_id, away_team_id) VALUES (%s, %s, %s, %s)",
            (game['id'], game['date'], game['homeTeam']['id'], game['awayTeam']['id'])
        )

        # Insert player stats for home team players
        for player_stats in game['homeTeam']['players']:
            cur.execute(
                """INSERT INTO player_stats (game_id, player_id, team_id, is_starter, minutes, points, assists,
                   offensive_rebounds, defensive_rebounds, steals, blocks, turnovers, defensive_fouls, offensive_fouls)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    game['id'],  # game_id
                    player_stats['id'],  # player_id
                    game['homeTeam']['id'],  # team_id (home team)
                    player_stats.get('isStarter', False),  # is_starter, default to False if not found
                    player_stats.get('minutes', 0),  # minutes, default to 0
                    player_stats.get('points', 0),  # points, default to 0
                    player_stats.get('assists', 0),  # assists, default to 0
                    player_stats.get('offensiveRebounds', 0),  # offensive_rebounds, default to 0
                    player_stats.get('defensiveRebounds', 0),  # defensive_rebounds, default to 0
                    player_stats.get('steals', 0),  # steals, default to 0
                    player_stats.get('blocks', 0),  # blocks, default to 0
                    player_stats.get('turnovers', 0),  # turnovers, default to 0
                    player_stats.get('defensiveFouls', 0),  # defensive_fouls, default to 0
                    player_stats.get('offensiveFouls', 0)  # offensive_fouls, default to 0
                )
            )

        # Insert player stats for away team players
        for player_stats in game['awayTeam']['players']:
            cur.execute(
                """INSERT INTO player_stats (game_id, player_id, team_id, is_starter, minutes, points, assists,
                   offensive_rebounds, defensive_rebounds, steals, blocks, turnovers, defensive_fouls, offensive_fouls)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    game['id'],  # game_id
                    player_stats['id'],  # player_id
                    game['awayTeam']['id'],  # team_id (away team)
                    player_stats.get('isStarter', False),  # is_starter, default to False if not found
                    player_stats.get('minutes', 0),  # minutes, default to 0
                    player_stats.get('points', 0),  # points, default to 0
                    player_stats.get('assists', 0),  # assists, default to 0
                    player_stats.get('offensiveRebounds', 0),  # offensive_rebounds, default to 0
                    player_stats.get('defensiveRebounds', 0),  # defensive_rebounds, default to 0
                    player_stats.get('steals', 0),  # steals, default to 0
                    player_stats.get('blocks', 0),  # blocks, default to 0
                    player_stats.get('turnovers', 0),  # turnovers, default to 0
                    player_stats.get('defensiveFouls', 0),  # defensive_fouls, default to 0
                    player_stats.get('offensiveFouls', 0)  # offensive_fouls, default to 0
                )
            )

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()