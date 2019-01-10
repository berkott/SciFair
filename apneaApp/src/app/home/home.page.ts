import { Component } from '@angular/core';
import { MenuController } from '@ionic/angular';
import { BackendService } from "../../services/backend/backend.service"

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  generalRisk: number = 0;
  heart: number = 0;
  eeg: number = 0;
  breath: number = 0;

  constructor(
  private menuCtrl: MenuController,
  private backendService: BackendService
  ) {
    this.menuCtrl.enable(true);
  }

  ngOnInit(){
    this.backendService.getMainData().then(val => {
      this.generalRisk = val[0]["score"];
      this.heart = val[0]["heartRate"];
      this.eeg = val[0]["eeg"];
      this.breath = val[0]["breathing"];
      
      console.log(val);

      this.changeColor(this.generalRisk, "generalRiskCir");
      this.changeColor(this.heart, "heartCir");
      this.changeColor(this.eeg, "eegCir");
      this.changeColor(this.breath, "breathCir");
    });
  }

  changeColor(val: number, name: string) {
    // let colorNum = value/100;
    // let value = val-50;

    // let red = 255 - Math.abs(value*5.1);
    // let green = 255 - value*5.1;

    // if (value <= 0){
    //   green = 255;
    // }
    // if (value >= 0){
    //   red = 255;
    // }

    let value = val-50;

    let red = 240 - Math.abs(value*4.8);
    let green = 240 - value*4.8;

    if (value <= 0){
      green = 240;
    }
    if (value >= 0){
      red = 240;
    }

    console.log(name);
    console.log("Green " + green);
    console.log("Red " + red);

    document.getElementById(name).style
      .stroke = "rgb(" + red + ", " + green + ", 10)";

    document.getElementById(name)
      .setAttribute('stroke-dasharray', val+",100");
  }
}
