import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms'
import { Router } from '@angular/router';
import { RouterModule, Routes } from '@angular/router';

@Component({
  selector: 'app-faq',
  templateUrl: './faq.component.html',
  styleUrls: ['./faq.component.css']
})
export class FaqComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {}
  flag=true
data=[
  {id:1,
  name:'Bill'
  },
  {id:2,
  name:'Speed'
  },
  {id:3,
  name:'Plan related'
  },
  {id:4,
  name:'Technical'
  },
  {id:5,
  name:'Offer related '
  },
  {id:6,
  name:'Other Issues '
  },

]
FAQ:string

  Form2= new FormGroup({
name2: new FormControl(),
})

get()
{
console.log(this.Form2.value)
if (this.Form2.value.name2 =="1")
{
this.FAQ='Bill'
}
if (this.Form2.value.name2 =="2")
{
this.FAQ='Speed'}
if (this.Form2.value.name2 =="3")
{
this.FAQ='Plan related'}
if (this.Form2.value.name2 =="4")
{
this.FAQ='Technical'}
if (this.Form2.value.name2 =="5")
{
this.FAQ='Offer related'}
if (this.Form2.value.name2 =="6")
{
this.FAQ='Other Issues'}
if (this.Form2.value.name2 >="7")
{
alert("invalid")
}
}

}
