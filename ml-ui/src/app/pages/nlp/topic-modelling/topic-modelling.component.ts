import { Component, OnInit } from '@angular/core';

import { HttpClient} from '@angular/common/http';

import {ApiService} from '../../../service/api/api.service';

@Component({
  selector: 'ngx-topic-modelling',
  templateUrl: './topic-modelling.component.html',
  styleUrls: ['./topic-modelling.component.scss']
})
export class TopicModellingComponent implements OnInit {

  formData = {
    search_query :""
  }
  constructor(
    private http: HttpClient,
    private apiService : ApiService
    // private formBuilder: FormBuilder,
    ) { }
    graph = "";
    show_graph=false;
  ngOnInit(): void {
  }
  

  onSubmit(){
    this.apiService.post('/topic-modelling',this.formData).subscribe((res)=>{
      if(res){
        this.graph = res;
        this.show_graph = true;
      }

    },(err) => {console.log(err)
      this.show_graph=false;
      this.graph="";
    })  

 
  }

}
