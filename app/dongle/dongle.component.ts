import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-dongle',
  templateUrl: './dongle.component.html',
  styleUrls: ['./dongle.component.css']
})
export class DongleComponent implements OnInit {
items:any;
error: any;
 constructor(private api: ApiService) {}

ngOnInit():void{
this.get();
}
get=()=> {
this.api.getItems6().subscribe(
data=>{ this.items=data;},
);
  (error: any) => this.error = error
  }

}
