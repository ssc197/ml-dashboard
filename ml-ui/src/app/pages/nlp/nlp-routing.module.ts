import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {TextblobSentimentsComponent} from './textblob-sentiments/textblob-sentiments.component';
import { TopicModellingComponent } from "./topic-modelling/topic-modelling.component";

const routes: Routes = [
  {
    path: 'textblob',
    component: TextblobSentimentsComponent,
  },
  {
    path: '',
    redirectTo: 'textblob',
    pathMatch: 'full',
  },
  {
    path: 'topic-modelling',
    component: TopicModellingComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class NLPRoutingModule { }
