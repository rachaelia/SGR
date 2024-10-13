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

  ngAfterViewInit(): void {
    fromEvent(this.input.nativeElement, 'keyup').pipe(debounceTime(1200)).subscribe(c => 
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

  clear(): void {
    this.sentiment = '';
    this.currentValue = '';
  }
}
