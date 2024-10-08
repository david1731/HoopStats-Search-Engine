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
  ngOnInit(): void {
    // this.playersService.getPlayerSummary(1).pipe(untilDestroyed(this)).subscribe(data => {
    //   console.log(data.apiResponse);
    // });
  }

  onSearchChange(query: string): void {
    if (query.length > 1){
      this.http.get<PlayerSuggestion[]>(`http://localhost:8000/api/v1/playerAutocomplete?query=${query}`).subscribe(
        (data: PlayerSuggestion[]) => {
          this.suggestions = data;
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
  
}
