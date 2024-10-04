import {
  ChangeDetectorRef,
  Component,
  OnDestroy,
  OnInit,
  ViewEncapsulation
} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {untilDestroyed, UntilDestroy} from '@ngneat/until-destroy';
import {PlayersService} from '../_services/players.service';
import { HttpClient } from '@angular/common/http';

interface SearchResults {
  players: { id: number, name: string }[];
  teams: { id: number, name: string }[];
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
  results: SearchResults = { players: [], teams: [] };

  constructor(
    protected activatedRoute: ActivatedRoute,
    protected cdr: ChangeDetectorRef,
    protected playersService: PlayersService,
    private http: HttpClient
  ) {

  }
  onSearch(): void {
    if (this.searchQuery) {
      this.http
        .get<SearchResults>(`http://localhost:8000/api/v1/autocomplete?query=${this.searchQuery}`)
        .subscribe((data) => {
          this.results = data;
        });
    }
  }

  ngOnInit(): void {
    this.playersService.getPlayerSummary(1).pipe(untilDestroyed(this)).subscribe(data => {
      console.log(data.apiResponse);
    });
  }

  ngOnDestroy() {
  }

}