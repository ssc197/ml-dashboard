import { Component, OnInit } from '@angular/core';


import {   FormBuilder,
  FormControl,
  FormGroup,
  FormGroupDirective,
  NgForm,
  Validators} from '@angular/forms'
import { HttpClient} from '@angular/common/http';

@Component({
  selector: 'ngx-textblob-sentiments',
  templateUrl: './textblob-sentiments.component.html',
  styleUrls: ['./textblob-sentiments.component.scss']
})

export class TextblobSentimentsComponent implements OnInit {
  SERVER_URL = "http://3.15.28.219:8080/sentiment-analysis";
  sentimentForm: FormGroup;
  constructor(private http: HttpClient,
    private formBuilder: FormBuilder,
    ) { }
  Sentiments = '';
  Emoji = '';
  ngOnInit(): void {
    
    this.sentimentForm = this.formBuilder.group({
      analysis_query: new FormControl("", [
        Validators.required
      ]),
    });
  }
  
  // get g() {
  //   return this.sentimentForm.controls;
  // }


  onSubmit(){
    const formData = new FormData();
    formData.append('analysis_query', this.sentimentForm.get('analysis_query').value);
    this.http.post<any>(this.SERVER_URL, formData).subscribe(
      (res) => {
        // console.log(res)
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
      },
      (err) => console.log(err)
    );
  }


  toggleEvent(){
    // console.log('changes')
    this.sentimentForm.reset();
    this.Sentiments = "";
    this.Emoji= '';
  }
}
