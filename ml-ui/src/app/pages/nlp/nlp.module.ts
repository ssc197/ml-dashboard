import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  NbActionsModule,
  NbButtonModule,
  NbCardModule,
  NbCheckboxModule,
  NbDatepickerModule, NbIconModule,
  NbInputModule,
  NbRadioModule,
  NbSelectModule,
  NbUserModule,
} from '@nebular/theme';
// import { FormsModule as ngFormsModule } from '@angular/forms';
import { FormsModule , ReactiveFormsModule} from '@angular/forms';


import { NLPRoutingModule } from './nlp-routing.module';
import { TextblobSentimentsComponent } from './textblob-sentiments/textblob-sentiments.component';

@NgModule({
  declarations: [TextblobSentimentsComponent],
  imports: [
    CommonModule,
    NLPRoutingModule,
    NbInputModule,
    NbCardModule,
    NbButtonModule,
    NbActionsModule,
    NbUserModule,
    NbCheckboxModule,
    NbRadioModule,
    NbDatepickerModule,
    NbSelectModule,
    NbIconModule,
    FormsModule
  ]
})
export class NLPModule { }
