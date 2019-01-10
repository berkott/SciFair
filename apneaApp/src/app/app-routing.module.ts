import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'login',
    pathMatch: 'full'
  },
  {
    path: 'home',
    loadChildren: './home/home.module#HomePageModule'
  },
  { 
    path: 'login', 
    loadChildren: './login/login.module#LoginPageModule' 
  },
  { 
    path: 'getting-started',
    loadChildren: './getting-started/getting-started.module#GettingStartedPageModule' 
  },
  { 
    path: 'epworth', 
    loadChildren: './epworth/epworth.module#EpworthPageModule' 
  },
  { 
    path: 'stop-bang', 
    loadChildren: './stop-bang/stop-bang.module#StopBangPageModule' 
  },
  { 
    path: 'record', 
    loadChildren: './record/record.module#RecordPageModule' 
  },
  { 
    path: 'help', 
    loadChildren: './help/help.module#HelpPageModule' 
  },
  { 
    path: 'post-sleep', 
    loadChildren: './post-sleep/post-sleep.module#PostSleepPageModule' 
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
