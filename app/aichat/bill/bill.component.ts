import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-bill',
  templateUrl: './bill.component.html',
  styleUrls: ['./bill.component.css']
})
export class BillComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {}
  flag=true
data=[
  {id:1,
  name:'when is my bill due?'
  },
  {id:2,
  name:'How to download my bill?'
  },
  {id:3,
  name:'Who do I contact for bill issues'
  },
  {id:4,
  name:'Bill not generated'
  },

]

Bill:string


  Form2= new FormGroup({
name2: new FormControl(),
})

get()
{
console.log(this.Form2.value)
if (this.Form2.value.name2 =="1")
{
this.Bill='when is my bill due?'
}
if (this.Form2.value.name2 =="2")
{
this.Bill='How to download my bill?'}
if (this.Form2.value.name2 =="3")
{
this.Bill='Who do I contact for bill issues'}
if (this.Form2.value.name2 =="4")
{
this.Bill='Bill not generated'}

if (this.Form2.value.name2 >="5")
{
alert("invalid")}
}

}
