import { Component } from '@angular/core';

import { Platform, MenuController } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';
import { BackendService } from '../services/backend/backend.service';

import { Router } from '@angular/router';
import { Storage } from '@ionic/storage';
import { ToastService } from 'src/services/toast/toast.service';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html'
})
export class AppComponent {
  public appPages = [
    {
      title: 'Home',
      url: '/home',
      icon: 'home'
    },
    {
      title: 'Record',
      url: '/record',
      icon: 'recording'
    },
    {
      title: 'Post Sleep',
      url: '/post-sleep',
      icon: 'paper'
    },
    {
      title: 'Help',
      url: '/help',
      icon: 'help-circle'
    }
  ];

  constructor(
    private platform: Platform,
    private splashScreen: SplashScreen,
    private statusBar: StatusBar,
    private backendService : BackendService,    
    private router: Router,
    private storage: Storage,
    private toaster: ToastService,
    private menuCtrl: MenuController
    ) {
      this.menuCtrl.enable(true);
      this.initializeApp();
    }

  initializeApp() {
    this.platform.ready().then(() => {
      this.statusBar.styleDefault();
      this.splashScreen.hide();
    });
  }

  async logout(){
    await this.backendService.logout();
    await this.storage.set('username', '');
    await this.storage.set('password', '');
    await this.toaster.toast("Logged out Successfully");
    await this.menuCtrl.enable(false);
    await this.router.navigate(['/login']);
  }
}
