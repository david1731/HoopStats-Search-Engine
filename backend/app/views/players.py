# -*- coding: utf-8 -*-
import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Player, PlayerStats, Shots, Game

LOGGER = logging.getLogger('django')

class PlayerSummary(APIView):
    logger = LOGGER

    def get(self, request, playerID):
        """Return player summary data based on the playerID"""

        try:
            # Fetch the player from the database
            player = Player.objects.get(id=playerID)

            # Fetch all games and stats where the player participated
            player_stats = PlayerStats.objects.filter(player_id=player.id).select_related('game')

            # Prepare the response structure
            response_data = {
                "name": player.name,
                "games": []
            }

            for stats in player_stats:
                game = stats.game

                # Fetch all shots for this player in the specific game
                shots = Shots.objects.filter(player_id=player.id, game_id=game.id)

                # Prepare shot data
                shots_data = [
                    {
                        "isMake": shot.is_made,
                        "locationX": shot.location_x,
                        "locationY": shot.location_y
                    }
                    for shot in shots
                ]

                # Prepare the game summary
                game_summary = {
                    "date": game.date,
                    "isStarter": stats.is_starter,
                    "minutes": stats.minutes,
                    "points": stats.points,
                    "assists": stats.assists,
                    "offensiveRebounds": stats.offensive_rebounds,
                    "defensiveRebounds": stats.defensive_rebounds,
                    "steals": stats.steals,
                    "blocks": stats.blocks,
                    "turnovers": stats.turnovers,
                    "defensiveFouls": stats.defensive_fouls,
                    "offensiveFouls": stats.offensive_fouls,
                    "freeThrowsMade": stats.free_throws_made,
                    "freeThrowsAttempted": stats.free_throws_attempted,
                    "twoPointersMade": stats.two_pointers_made,
                    "twoPointersAttempted": stats.two_pointers_attempted,
                    "threePointersMade": stats.three_pointers_made,
                    "threePointersAttempted": stats.three_pointers_attempted,
                    "shots": shots_data
                }

                # Add game summary to the response
                response_data["games"].append(game_summary)

            # Return the player summary as a response
            return Response(response_data)

        except Player.DoesNotExist:
            # Return 404 error if player is not found
            return Response({"error": "Player not found"}, status=404)


