# -*- coding: utf-8 -*-
import logging
from django.db import connection
from rest_framework.response import Response
from rest_framework.views import APIView

LOGGER = logging.getLogger('django')

class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        """Return player summary data based on the playerID"""

        try:
            # Fetch player details using raw SQL
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM players WHERE id = %s", [playerID])
                player = cursor.fetchone()
                
                if not player:
                    return Response({"error": "Player not found"}, status=404)

                player_name = player[0]

            # Fetch all player stats and games using the correct SQL query
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT 
                        g.date, ps.is_starter, ps.minutes, ps.points, ps.assists, 
                        ps.offensive_rebounds, ps.defensive_rebounds, ps.steals, 
                        ps.blocks, ps.turnovers, ps.defensive_fouls, ps.offensive_fouls,
                        ps.freethrows_made, ps.freethrows_attempted, 
                        ps.twopointers_made, ps.twopointers_attempted,
                        ps.threepointers_made, ps.threepointers_attempted,
                        g.id AS game_id
                    FROM player_stats ps
                    JOIN games g ON ps.game_id = g.id
                    WHERE ps.player_id = %s
                """, [playerID])
                player_stats = cursor.fetchall()
                print(f"player Stats: {player_stats}")

            # Prepare the response structure
            response_data = {
                "name": player_name,
                "games": []
            }

            for stats in player_stats:
                (game_date, is_starter, minutes, points, assists, 
                offensive_rebounds, defensive_rebounds, steals, blocks, turnovers, 
                defensive_fouls, offensive_fouls, freethrows_made, freethrows_attempted, 
                twopointers_made, twopointers_attempted, threepointers_made, 
                threepointers_attempted, game_id) = stats

                # Fetch all shots for this player in the specific game
                with connection.cursor() as cursor:
                    cursor.execute("""
                        SELECT is_made, location_x, location_y
                        FROM shots
                        WHERE player_id = %s AND game_id = %s
                    """, [playerID, game_id])
                    shots = cursor.fetchall()
                    print(f"shots: {shots}, shots length: {len(shots)}")

                # Prepare shot data
                shots_data = [
                    {
                        "isMake": shot[0],
                        "locationX": shot[1],
                        "locationY": shot[2]
                    }
                    for shot in shots
                ]

                # Prepare the game summary
                game_summary = {
                    "date": game_date,
                    "isStarter": is_starter,
                    "minutes": minutes,
                    "points": points,
                    "assists": assists,
                    "offensiveRebounds": offensive_rebounds,
                    "defensiveRebounds": defensive_rebounds,
                    "steals": steals,
                    "blocks": blocks,
                    "turnovers": turnovers,
                    "defensiveFouls": defensive_fouls,
                    "offensiveFouls": offensive_fouls,
                    "freeThrowsMade": freethrows_made,
                    "freeThrowsAttempted": freethrows_attempted,
                    "twoPointersMade": twopointers_made,
                    "twoPointersAttempted": twopointers_attempted,
                    "threePointersMade": threepointers_made,
                    "threePointersAttempted": threepointers_attempted,
                    "shots": shots_data
                }

                # Add game summary to the response
                response_data["games"].append(game_summary)

            # Return the player summary as a response
            return Response(response_data)

        except Exception as e:
            LOGGER.error(f"Error fetching player summary: {str(e)}")
            return Response({"error": "Internal Server Error"}, status=500)




