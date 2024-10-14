import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';
import { debounceTime, fromEvent } from 'rxjs';
import { SentimentService } from './sentiment.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})

export class AppComponent implements AfterViewInit {

  constructor(private dataService: SentimentService){}
  @ViewChild('input') input: ElementRef;
  currentValue: string;
  sentiment: string;

  /**
   * Waits a second since the keyup event emission before emptying the sentiment variable 
   * if currentValue is empty or calling the service to get the sentiment analysis from the 
   * server
   */
  ngAfterViewInit(): void {
    fromEvent(this.input.nativeElement, 'keyup').pipe(debounceTime(1000)).subscribe(c => 
    {
      if(this.currentValue === ""){
        this.sentiment = '';
      } else {
        this.dataService.getSentiment(this.currentValue).subscribe((result) => {
          this.sentiment = result;
        })
      }
    }
    );
  }

  /**
   * Clears both the sentiment output and the input value when the
   * material button X is clicked
   */
  clear(): void {
    this.sentiment = '';
    this.currentValue = '';
  }
}
