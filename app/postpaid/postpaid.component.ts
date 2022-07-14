import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-postpaid',
  templateUrl: './postpaid.component.html',
  styleUrls: ['./postpaid.component.css']
})
export class PostpaidComponent implements OnInit {
items:any;
error: any;
 constructor(private api: ApiService) {}

ngOnInit():void{
this.get();
}
get=()=> {
this.api.getItems5().subscribe(
data=>{ this.items=data;},
);
  (error: any) => this.error = error
  }

}
