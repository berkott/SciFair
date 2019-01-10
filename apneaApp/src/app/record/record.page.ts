import { Component, OnInit } from '@angular/core';
import { MenuController } from '@ionic/angular';

@Component({
  selector: 'app-record',
  templateUrl: './record.page.html',
  styleUrls: ['./record.page.scss'],
})
export class RecordPage implements OnInit {

  constructor(
    private menuCtrl: MenuController
    ) {
      this.menuCtrl.enable(true);
    }
  
    ngOnInit() {
  }

}
