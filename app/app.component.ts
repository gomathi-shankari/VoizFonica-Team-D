import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from './api.service';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Voizfonica';
  items:any;
error: any;
 constructor(private api: ApiService) {}

ngOnInit():void{
this.get();
}
get=()=> {
this.api.getItems1().subscribe(
data=>{ this.items=data;},
);
  (error: any) => this.error = error
  }
imgCollection: Array<object> = [
      {
        image: '../assets/MicrosoftTeams-image.png',
        thumbImage: '../assets/MicrosoftTeams-image.png',
        alt: 'Image 1',
        title: 'Image 1'
      }, {
        image: '../assets/MicrosoftTeams-image (1).png',
        thumbImage: '../assets/MicrosoftTeams-image (1).png',
        title: 'Image 2',
        alt: 'Image 2'
      }, {
        image: '../assets/MicrosoftTeams-image (2).png',
        thumbImage: '../assets/MicrosoftTeams-image (2).png',
        title: 'Image 3',
        alt: 'Image 3'
      }, {
        image: '../assets/MicrosoftTeams-image (3).png',
        thumbImage: '../assets/MicrosoftTeams-image (3).png',
        title: 'Image 4',
        alt: 'Image 4'
      }, {
        image: '../assets/offer.jpg',
        thumbImage: '../assets/offer.jpg',
        title: 'Image 5',
        alt: 'Image 5'
      }, {
        image: '../assets/free data.png',
        thumbImage: '../assets/free data.png',
        title: 'Image 6',
        alt: 'Image 6'
      }
  ];
}
