import { Component, OnInit } from '@angular/core';
import { ToastService } from 'src/services/toast/toast.service';
import { Router } from '@angular/router';
import { ModalController, MenuController } from '@ionic/angular';

import { EpworthPage } from '../epworth/epworth.page';
import { StopBangPage } from '../stop-bang/stop-bang.page';
import { BackendService } from 'src/services/backend/backend.service';

@Component({
  selector: 'app-getting-started',
  templateUrl: './getting-started.page.html',
  styleUrls: ['./getting-started.page.scss'],
})
export class GettingStartedPage implements OnInit {
  enStopBang: boolean = false;
  enEpworth: boolean = false;
  enFinish: boolean = true;
  username: string = "";
  password: string ="";

  constructor(
    private router: Router,
    private toaster: ToastService,
    private modalController: ModalController,
    private menuCtrl: MenuController,
    private backendService: BackendService
    ) {
      this.menuCtrl.enable(false);
    }

  ngOnInit() {
  }

  async pushData(){
    await this.backendService.pushMuseData(this.username, this.password).then(() => {
      console.log("sent answers successfully");
      this.toaster.toast("Response sent successfully");
    }).catch(err => {
      this.toaster.toast("Failed to send");
      console.error("could not send answers" , err);
    });
  }

  async epworth(){
    const modal = await this.modalController.create({
      component: EpworthPage
    });
    this.enEpworth = true;
    this.checkFinish();
    return await modal.present();
  }

  async stopBang(){
    const modal = await this.modalController.create({
      component: StopBangPage
    });
    this.enStopBang = true;
    console.log(this.enStopBang + " ep: "+ this.enEpworth)
    this.checkFinish();
    return await modal.present();
  }

  private checkFinish(){
    if(this.enStopBang == true && this.enEpworth == true){
      this.enFinish = false;
    }
  }

  async finish(){
    // if(this.enEpworth == true && this.enStopBang == true){
      // await this.storage.set('quest', 'yes');
      this.toaster.toast("Thank you for completing the questionnaires.");
      this.router.navigate(['/home']);
    // } else{
    //   this.toaster.toast("Please complete the questionnaires first.");
    // }
  }

}
