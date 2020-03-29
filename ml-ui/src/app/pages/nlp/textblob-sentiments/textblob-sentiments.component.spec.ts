import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { TextblobSentimentsComponent } from './textblob-sentiments.component';

describe('TextblobSentimentsComponent', () => {
  let component: TextblobSentimentsComponent;
  let fixture: ComponentFixture<TextblobSentimentsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ TextblobSentimentsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(TextblobSentimentsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
