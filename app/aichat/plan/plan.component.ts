import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-plan',
  templateUrl: './plan.component.html',
  styleUrls: ['./plan.component.css']
})
export class PlanComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {}
  flag=true
data=[
  {id:1,
  name:'Unable to see plans'
  },
  {id:2,
  name:'What is prepaid?'
  },
  {id:3,
  name:'What is postpaid?'
  },
  {id:4,
  name:'What is dongle?'
  },

]
plan:string

  Form2= new FormGroup({
name2: new FormControl(),
})

get()
{
console.log(this.Form2.value)
if (this.Form2.value.name2 =="1")
{
this.plan='Unable to see plans'
}
if (this.Form2.value.name2 =="2")
{
this.plan='What is prepaid?'}
if (this.Form2.value.name2 =="3")
{
this.plan='What is postpaid?'}
if (this.Form2.value.name2 =="4")
{
this.plan='What is dongle?'}

if (this.Form2.value.name2 >="5")
{
alert("invalid")}
}

}
