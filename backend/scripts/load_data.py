import psycopg2
import json

# connect to database
conn = psycopg2.connect(
    dbname="okc",
    user="okcapplicant",
    password="thunder",
    host="localhost"
)

cur = conn.cursor()

# load teams 
with open('raw_data/teams.json') as f:
    teams_data = json.load(f)
    for team in teams_data:
        cur.execute(
            """
            INSERT INTO teams (id, name) 
            VALUES (%s, %s)
            ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name
            """, 
            (team['id'], team['name'])
        )

# load Players
with open('raw_data/players.json') as f:
    players_data = json.load(f)
    for player in players_data:
        cur.execute(
            """
            INSERT INTO players (id, name) 
            VALUES (%s, %s)
            ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name
            """, 
            (player['id'], player['name'])
        )

# Load Games and Player Stats
with open('raw_data/games.json') as f:
    games_data = json.load(f)
    for game in games_data:
        # Insert game into games table
        cur.execute(
            """
            INSERT INTO games (id, date, home_team_id, away_team_id) 
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) DO UPDATE SET 
                date = EXCLUDED.date,
                home_team_id = EXCLUDED.home_team_id,
                away_team_id = EXCLUDED.away_team_id
            """,
            (game['id'], game['date'], game['homeTeam']['id'], game['awayTeam']['id'])
        )

        # Function to insert player stats
        def insert_player_stats(player_stats, team_id):
            cur.execute(
                """
                INSERT INTO player_stats (
                    game_id, player_id, team_id, is_starter, minutes, points, assists,
                    offensive_rebounds, defensive_rebounds, steals, blocks, turnovers, defensive_fouls, offensive_fouls,
                    freethrows_made, freethrows_attempted, twopointers_made, twopointers_attempted,
                    threepointers_made, threepointers_attempted
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (game_id, player_id) DO UPDATE SET 
                    is_starter = EXCLUDED.is_starter,
                    minutes = EXCLUDED.minutes,
                    points = EXCLUDED.points,
                    assists = EXCLUDED.assists,
                    offensive_rebounds = EXCLUDED.offensive_rebounds,
                    defensive_rebounds = EXCLUDED.defensive_rebounds,
                    steals = EXCLUDED.steals,
                    blocks = EXCLUDED.blocks,
                    turnovers = EXCLUDED.turnovers,
                    defensive_fouls = EXCLUDED.defensive_fouls,
                    offensive_fouls = EXCLUDED.offensive_fouls,
                    freethrows_made = EXCLUDED.freethrows_made,
                    freethrows_attempted = EXCLUDED.freethrows_attempted,
                    twopointers_made = EXCLUDED.twopointers_made,
                    twopointers_attempted = EXCLUDED.twopointers_attempted,
                    threepointers_made = EXCLUDED.threepointers_made,
                    threepointers_attempted = EXCLUDED.threepointers_attempted

                """,
                (
                    game['id'],  # game_id
                    player_stats['id'],  # player_id
                    team_id,  # team_id
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
                    player_stats.get('offensiveFouls', 0),  # offensive_fouls, default to 0
                    player_stats.get('freeThrowsMade', 0), 
                    player_stats.get('freeThrowsAttempted', 0),
                    player_stats.get('twoPointersMade', 0),
                    player_stats.get('twoPointersAttempted', 0),
                    player_stats.get('threePointersMade', 0),
                    player_stats.get('threePointersAttempted', 0),

                )
            )

        # Insert stats for both home and away team players
        for player_stats in game['homeTeam']['players']:
            insert_player_stats(player_stats, game['homeTeam']['id'])

        for player_stats in game['awayTeam']['players']:
            insert_player_stats(player_stats, game['awayTeam']['id'])
    

with open('raw_data/games.json') as f:
    games_data = json.load(f)

    for game in games_data:
        game_id = game['id']

        # Loop through all players in the home team
        for player_stats in game['homeTeam']['players']:
            player_id = player_stats['id']

            # Assuming each player has a list of shots taken in the stats
            for shot in player_stats['shots']:

                # Insert the shot into the shots table
                cur.execute(
                    """
                    INSERT INTO shots (player_id, game_id, is_made, location_x, location_y)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT DO NOTHING;
                    """,
                    (player_id, game_id, shot.get('isMake',0), shot.get('locationX',0.0), shot.get('locationY', 0.0))
                )

        # Loop through all players in the away team
        for player_stats in game['awayTeam']['players']:
            player_id = player_stats['id']

            # Assuming each player has a list of shots taken in the stats
            for shot in player_stats['shots']:

                # Insert the shot into the shots table
                cur.execute(
                    """
                    INSERT INTO shots (player_id, game_id, is_made, location_x, location_y)
                    VALUES (%s, %s, %s, %s, %s)
                    ON CONFLICT DO NOTHING;
                    """,
                    (player_id, game_id, shot.get('isMake',0), shot.get('locationX',0.0), shot.get('locationY', 0.0))
                )

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()
