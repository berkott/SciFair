import { Component, OnInit } from '@angular/core';
import { BackendService } from '../../services/backend/backend.service';
import { ToastService } from '../../services/toast/toast.service';
import { Router } from '@angular/router';
import { Storage } from '@ionic/storage';
import { MenuController } from '@ionic/angular';


@Component({
  selector: 'app-login',
  templateUrl: './login.page.html',
  styleUrls: ['./login.page.scss'],
})
export class LoginPage implements OnInit {
  username: string = "";
  password: string = "";

  constructor(
    private backendService : BackendService,
    private toaster: ToastService,
    private router: Router,
    private storage: Storage,
    private menuCtrl: MenuController
    ) {
      this.menuCtrl.enable(false);
    }

  async ngOnInit() {
    await this.storage.get('username').then((user) => {
      this.storage.get('password').then((pass) => {
        console.log(user);
        console.log(pass);
        
        this.username = user;
        this.password = pass;
        this.login(false); 
      }).catch(() => {
        console.log("Please login");
      });
    }).catch(() => {
      console.log("Please login");
    });
  }

  async login(print: boolean){
    // this.backendService.login(this.username, this.password);
    this.backendService.login(this.username, this.password).then(() => {
      console.log("yay");
      this.toaster.toast("Logged in Successfully");
      this.storage.set('username', this.username);
      this.storage.set('password', this.password);

      this.backendService.checkQuests().then(val => {
        if(val == true){
          this.router.navigate(['/home']);
          document.getElementById("content").style.display = "block";
        } else {
          this.router.navigate(['/getting-started']);
          document.getElementById("content").style.display = "block";
        }
      });
    }).catch(() => {
      console.log("nay");
      if(print == true){
        this.toaster.toast("Please try again");
      }
      document.getElementById("content").style.display = "block";
    });
  }

}
