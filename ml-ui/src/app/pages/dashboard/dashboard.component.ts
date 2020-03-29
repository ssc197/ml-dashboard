import {Component, OnDestroy} from '@angular/core';
import { NbThemeService, NbMediaBreakpoint, NbMediaBreakpointsService } from '@nebular/theme';
import { takeWhile } from 'rxjs/operators' ;
import { SolarData } from '../../@core/data/solar';

interface CardSettings {
  title: string;
  iconClass: string;
  type: string;
}

@Component({
  selector: 'ngx-dashboard',
  styleUrls: ['./dashboard.component.scss'],
  templateUrl: './dashboard.component.html',
})
export class DashboardComponent implements OnDestroy {
  breakpoint: NbMediaBreakpoint;
  breakpoints: any;
  private expanded: boolean;
  themeSubscription: any;
  themeChangeSubscription: any;

  constructor(private themeService: NbThemeService,
    private breakpointService: NbMediaBreakpointsService) {

this.breakpoints = this.breakpointService.getBreakpointsMap();
this.themeSubscription = this.themeService.onMediaQueryChange()
.subscribe(([, newValue]) => {
this.breakpoint = newValue;
});

}
expand() {
  this.expanded = true;
}

isCollapsed() {
  return !this.expanded;
}
  ngOnDestroy() {
  }
}
