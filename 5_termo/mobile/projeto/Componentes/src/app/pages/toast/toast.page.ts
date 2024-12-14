import { addIcons } from 'ionicons';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonBackButton, IonToast, IonButton } from '@ionic/angular/standalone';
import { ToastController } from '@ionic/angular';
import { globe } from 'ionicons/icons';

@Component({
  selector: 'app-toast',
  templateUrl: './toast.page.html',
  styleUrls: ['./toast.page.scss'],
  standalone: true,
  imports: [IonButton, IonToast, IonBackButton, IonButtons, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule]
})
export class ToastPage {
  private isToastPresenting = false;

  toastButtons = [
    {
      text: 'Ação com texto longo',
    },
  ];

  public toastButtons2 = [
    {
      text: 'Dismiss',
      role: 'cancel',
    },
  ];

  constructor(private toastController: ToastController) {
    addIcons({ globe });
  }



  async presentToast(position: 'top' | 'middle' | 'bottom') {
    if (this.isToastPresenting) return;

    this.isToastPresenting = true;

    const toast = await this.toastController.create({
      message: 'Hello World!',
      duration: 1500,
      position: position,
    });

    toast.onDidDismiss().then(() => {
      this.isToastPresenting = false;
    });

    await toast.present();
  }

  async presentToast2() {
    if (this.isToastPresenting) return;

    this.isToastPresenting = true;

    const toast = await this.toastController.create({
      message: 'Hello World!',
      duration: 3000,
      icon: 'globe',
    });

    toast.onDidDismiss().then(() => {
      this.isToastPresenting = false;
    });

    await toast.present();
  }
}
