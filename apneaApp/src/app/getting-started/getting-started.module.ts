import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { GettingStartedPage } from './getting-started.page';

const routes: Routes = [
  {
    path: '',
    component: GettingStartedPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes)
  ],
  declarations: [
    GettingStartedPage
  ]
})
export class GettingStartedPageModule {}
