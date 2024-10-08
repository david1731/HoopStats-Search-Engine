import {
  ChangeDetectorRef,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation
} from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { untilDestroyed, UntilDestroy } from '@ngneat/until-destroy';
import { PlayersService } from '../_services/players.service';
import { HttpClient } from '@angular/common/http';


// Define the interface for the shot
interface Shot {
  isMake: boolean;
  locationX: number;
  locationY: number;
}

// Define the interface for each game
interface Game {
  date: string;
  isStarter: boolean;
  minutes: number;
  points: number;
  assists: number;
  offensiveRebounds: number;
  defensiveRebounds: number;
  steals: number;
  blocks: number;
  turnovers: number;
  defensiveFouls: number;
  offensiveFouls: number;
  freeThrowsMade: number;
  freeThrowsAttempted: number;
  twoPointersMade: number;
  twoPointersAttempted: number;
  threePointersMade: number;
  threePointersAttempted: number;
  shots: Shot[];
}

// Define the interface for the player summary
interface PlayerSummary {
  name: string;
  games: Game[];
}

interface PlayerSuggestion{
  id: number;
  name: string;
}

interface PlayerAutocompleteResponse {
  players: PlayerSuggestion[];
}

@UntilDestroy()
@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss']
})
export class PlayerSummaryComponent implements OnInit{
  searchQuery: string = '';
  results: any[] = [];
  suggestions: PlayerSuggestion[] = [];

  playerSummary: PlayerSummary | null = null;

  constructor(
    // protected activatedRoute: ActivatedRoute,
    // protected cdr: ChangeDetectorRef,
    // protected playersService: PlayersService,
    private http: HttpClient
  ) {}

  // ngOnInit method properly declared
  ngOnInit(): void {}

  onSearchChange(query: string): void {
    this.playerSummary = null;
    if (query.length > 1){
      this.http.get<PlayerAutocompleteResponse>(`http://localhost:8000/api/v1/playerAutocomplete?query=${query}`).subscribe(
        (data) => {
          this.suggestions = data.players;
          console.log('Autocomplete Suggestions:', data.players); // Log the suggestions
        },
        (error) => {
          console.error('Error fetching autocomplete suggestions', error);
        }
      );
    } else{
      this.suggestions = []; // clear suggestions if the query is to short
    }
  }

  onSelectPlayer(playerName: string): void{
    this.searchQuery = playerName; // set the input value to the selected name
    this.fetchPlayerSummary(playerName); // fetch the player summary based on the name 
    this.suggestions = []; // clear suggestions after selection
  }

  // Correctly declared onSearch method
  fetchPlayerSummary(playerName: string): void {
      // Make the API call to get the player summary
      this.http.get<PlayerSummary>(`http://localhost:8000/api/v1/playerSummary/${playerName}`).subscribe(
        (data: PlayerSummary) => {
          this.playerSummary = data;
        },
        (error) => {
          console.error('Error fetching player summary', error);
        }
      );
  }

  // calculate the distance between were the shot attempt was made from and the hoop
  calculateDistance(locationX: number, locationY: number): number{
    console.log(`Calculating distance for shot at (${locationX}, ${locationY})`);
    return Math.sqrt(Math.pow(locationX,2) + Math.pow(locationY,2));
  }

  calculate3PTFG(threePointersAttempted: number, threePointersMade: number): string{
    return ((threePointersMade/threePointersAttempted * 100)).toFixed(1);
  }

  calculateFT_FG(FT_Attempted:number, FT_Made:number): string{
    if (FT_Attempted == 0) return "0.0";
    return ((FT_Made/FT_Attempted) * 100).toFixed(1);
  }
  
  calculateFG(threePointersAttempted: number, threePointersMade: number, twoPointersAttempted: number, twoPointersMade: number): string{
    return ((threePointersMade + twoPointersMade) / (threePointersAttempted + twoPointersAttempted) * 100).toFixed(1);
  }
}
