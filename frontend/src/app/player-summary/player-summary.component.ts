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

interface SearchResults {
  players: { id: number, name: string }[];
  teams: { id: number, name: string }[];
}

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

@UntilDestroy()
@Component({
  selector: 'player-summary-component',
  templateUrl: './player-summary.component.html',
  styleUrls: ['./player-summary.component.scss'],
  encapsulation: ViewEncapsulation.None,
})
export class PlayerSummaryComponent implements OnInit, OnDestroy {
  searchQuery: string = '';
  results: any[] = [];
  playerSummary: PlayerSummary | null = null;

  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected playersService: PlayersService,
    private http: HttpClient
  ) {}

  // Correctly declared onSearch method
  onSearch(): void {
    if (this.searchQuery) {
      // Make the API call to get the player summary
      this.http.get<PlayerSummary>(`/api/v1/playerSummary/${this.searchQuery}`).subscribe(
        (data: PlayerSummary) => {
          this.playerSummary = data;
        },
        (error) => {
          console.error('Error fetching player summary', error);
        }
      );
    }
  }

  // ngOnInit method properly declared
  ngOnInit(): void {
    this.playersService.getPlayerSummary(1).pipe(untilDestroyed(this)).subscribe(data => {
      console.log(data.apiResponse);
    });
  }

  // ngOnDestroy method properly declared, even if it's empty
  ngOnDestroy(): void {
    // Cleanup logic (if needed)
  }
}
