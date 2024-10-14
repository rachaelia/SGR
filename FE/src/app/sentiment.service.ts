import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { catchError, Observable, throwError } from 'rxjs';

@Injectable()
export class SentimentService {
  private baseUrl = 'http://127.0.0.1:5000';
  constructor(protected httpClient: HttpClient) {}

  
  getSentiment(text: string): Observable<string>{
    return this.httpClient.post<string>(this.baseUrl, {
      input_text: text
    }).pipe(
      catchError((error: HttpErrorResponse) => {
        return throwError({
          error: error,
          msg: 'Could not get the sentiment analysis',
        });
      }),
    );
  }
}