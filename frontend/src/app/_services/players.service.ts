import {HttpClient, HttpParams} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable, BehaviorSubject} from 'rxjs';
import {map} from 'rxjs/operators';
// import {plainToClass} from 'class-transformer';

import {BaseService} from './base.service';

@Injectable({
  providedIn: 'root'
})
export class PlayersService extends BaseService {
  constructor(protected http: HttpClient) {
    super(http);
  }

  getPlayerList(): Observable<any>{
    const endpoint = `${this.baseUrl}/playerList`;
    return this.get(endpoint).pipe(map(
      (data: Object) => {
        return{
          endpoint: endpoint,
          apiResponse: data
        };
      },
      error => {
        return error;
      }
    ));
  }

  getPlayerSummary(playerName: string): Observable<any> {
    const endpoint = `${this.baseUrl}/playerSummary/${playerName}`;

    return this.get(endpoint).pipe(map(
      (data: Object) => {
          return {
            endpoint: endpoint,
            apiResponse: data
          };
      },
      error => {
          return error;
      }
    ));
  }

  // API endpoint for autocomplete
  getPlayerAutoComplete(query: string): Observable<any>{
    const endpoint = `${this.baseUrl}/playerAutocomplete?query=${query}`;
    return this.http.get(endpoint).pipe(
      map((data: any) => data.players)
    );
  }
}