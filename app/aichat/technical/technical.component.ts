import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-technical',
  templateUrl: './technical.component.html',
  styleUrls: ['./technical.component.css']
})
export class TechnicalComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {}
  flag=true
data=[
  {id:1,
  name:'Network coverage issues'
  },
  {id:2,
  name:'Frequent disconnections'
  },
  {id:3,
  name:'Dongle connectivity issues'
  },
  {id:4,
  name:'No connectivity'
  },

]
technical:string



Form2= new FormGroup({
name2: new FormControl(),
})

get()
{
console.log(this.Form2.value)
if (this.Form2.value.name2 =="1")
{
this.technical='Network coverage issues'
}
if (this.Form2.value.name2 =="2")
{
this.technical='Frequent disconnections'}
if (this.Form2.value.name2 =="3")
{
this.technical='Dongle connectivity issues'}
if (this.Form2.value.name2 =="4")
{
this.technical='No connectivity'}

if (this.Form2.value.name2 >="5")
{
alert("invalid")}
}


}
