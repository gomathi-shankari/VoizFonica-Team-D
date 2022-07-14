import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl} from '@angular/forms';

@Component({
  selector: 'app-buying',
  templateUrl: './buying.component.html',
  styleUrls: ['./buying.component.css']
})
export class BuyingComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {}

  form2= new FormGroup({
  date1: new FormControl(),
  time1: new FormControl(),})

  get1()
  {
  console.log(this.form2.value)
  if (this.form2.value.date1 =="12")
  if (this.form2.value.time1 =="1")
  {
  alert("valid user")}
  else{
  alert("invalid user")}
  }
}
