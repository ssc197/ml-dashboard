import { Component, OnInit } from '@angular/core';

import { HttpClient} from '@angular/common/http';

import {ApiService} from '../../../service/api/api.service';

@Component({
  selector: 'ngx-textblob-sentiments',
  templateUrl: './textblob-sentiments.component.html',
  styleUrls: ['./textblob-sentiments.component.scss']
})

export class TextblobSentimentsComponent implements OnInit {
 
  formData = {
    analysis_query :""

  }
  constructor(
    private http: HttpClient,
    private apiService : ApiService
    // private formBuilder: FormBuilder,
    ) { }
  Sentiments = '';
  Emoji = '';
  ngOnInit(): void {
    
    // this.sentimentForm = this.formBuilder.group({ 13.232.12.140:8080
    //   analysis_query: new FormControl("", [
    //     Validators.required
    //   ]),
    // });
  }
  
  // get g() {
  //   return this.sentimentForm.controls;
  // }


  onSubmit(){
    console.log(this.formData)


    this.apiService.post('/sentiment-analysis',this.formData).subscribe((res)=>{
     console.log(res)
      if(res.sentiment == -1){
        this.Sentiments = "Negative";
        this.Emoji= ' 😡 ';
      }else if(res.sentiment == 1){
        this.Sentiments = "Postive"
        this.Emoji= ' 😁 ';
      }else{
        this.Sentiments = "Neutral";
        this.Emoji= ' 😐 ';
      }

    },(err) => console.log(err))  

 
  }



}
