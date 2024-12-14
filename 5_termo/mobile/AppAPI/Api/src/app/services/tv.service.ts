import { delay, Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TvService {

  private http = inject(HttpClient);

  constructor() {}

  getShows(): Observable<object> {
    return this.http.get('http://api.tvmaze.com/show').pipe(
      delay(1000),
      (res: any) => {
        console.log('res', res);
        return res;
      }
    );
  }

  getDetalhes(idShow: string): Observable<object> {
    return this.http.get('http://api.tvmaze.com/shows/' + idShow).pipe(
      (res: any) => {
        return res;
      }
    );
  }

  getSessions(id: string): Observable<object> {
    return this.http.get('http://api.tvmaze.com/shows/' + id + '/seasons').pipe(
      (res: any) => {
        return res;
      }
    );
  }

  getElenco(id: string): Observable<any[]> {
    return this.http.get<any[]>('https://api.tvmaze.com/shows/' + id + '/cast').pipe(
      (res: any) => {
        return res;
      }
    );
  }
}
