import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../api.service';


@Component({
  selector: 'app-plans',
//   templateUrl: './plans.component.html',
template:
'<table><tr><th> Cost </th><th> Data per day </th><th> Validity </th><th> Amount </th></tr><tr *ngFor="let item of items"><td> {{ item.plan_name }} </td><td>{{ item.usage }}<td>{{ item.validity }}</td><td>{{ item.amount }}</td></tr></table>{{ error?.message }}',
 styleUrls: ['./plans.component.css'],
 providers: [ApiService,],
})
export class PlansComponent implements OnInit {
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
 }

