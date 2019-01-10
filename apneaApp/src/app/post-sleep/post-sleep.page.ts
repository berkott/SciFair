import { Component, OnInit } from '@angular/core';
import { BackendService } from 'src/services/backend/backend.service';
import { ModalController, MenuController } from '@ionic/angular';
import { ToastService } from 'src/services/toast/toast.service';

@Component({
  selector: 'app-post-sleep',
  templateUrl: './post-sleep.page.html',
  styleUrls: ['./post-sleep.page.scss'],
})
export class PostSleepPage implements OnInit {
  val1: number = 0;
  val2: number = 0;
  val3: number = 0;
  val4: number = 0;
  val5: number = 0;
  val6: number = 0;
  val7: number = 0;
  val71: string = "";
  val8: number = 0;
  val9: number = 0;
  val91: string = "";
  val10: number = 0;
  val11: string = "";

  constructor(
    private backendService: BackendService,
    private modalController: ModalController,
    private toaster: ToastService,
    private menuCtrl: MenuController
    ) {
      this.menuCtrl.enable(true);
    }

  ngOnInit() {
  }

  async submit(){
    let answers = [Number(this.val1), Number(this.val2), Number(this.val3), 
                  Number(this.val4), Number(this.val5), Number(this.val6), 
                  Number(this.val7), this.val71, Number(this.val8), 
                  Number(this.val9), this.val91, Number(this.val10), 
                  this.val11];
                   
    await this.backendService.sendPostAnswers(answers).then(() => {
      console.log("sent answers successfully");
      this.toaster.toast("Response sent successfully");
      this.modalController.dismiss();
      // this.epworthState = true;
    }).catch(err => {
      this.toaster.toast("Failed to send");
      console.error("could not send answers" , err);
      // this.epworthState = false;
    });
  }

}
