import { Component } from '@angular/core';

@Component({
  selector: 'ngx-footer',
  styleUrls: ['./footer.component.scss'],
  
  template: `
  <div class="copyright pull-right"> 
            &copy; {{test | date: 'yyyy'}}, made by  <a href="https://www.linkedin.com/in/sajeed-shaikh-952a23125">Sajeed</a> and <a href="https://in.linkedin.com/in/sahrunnisha-rahamtullah-284728b8">Sahrunnisha</a>
        </div>
    <!-- <div class="socials">
      <a href="#" target="_blank" class="ion ion-social-github"></a> 
      <a href="#" target="_blank" class="ion ion-social-facebook"></a>
      <a href="#" target="_blank" class="ion ion-social-twitter"></a>
      <a href="#" target="_blank" class="ion ion-social-linkedin"></a>
    </div> 
    <div class="copyright pull-right"> 
            &copy; {{test | date: 'yyyy'}}, made by  <a href="https://www.linkedin.com/in/sajeed-shaikh-952a23125">Sajeed Shaikh</a>
        </div>
  
  
  -->
  `,
})
export class FooterComponent {
  test : Date = new Date()
}
