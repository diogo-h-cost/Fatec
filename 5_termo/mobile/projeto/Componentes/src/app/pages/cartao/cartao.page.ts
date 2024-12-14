import { addIcons } from 'ionicons';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonButton, IonButtons, IonBackButton, IonCard, IonIcon, IonImg, IonCardHeader, IonCardTitle, IonCardSubtitle, IonCardContent, IonItem, IonLabel, IonRow, IonCol } from '@ionic/angular/standalone';
import { pin, wifi, wine, warning, walk } from 'ionicons/icons'

@Component({
  selector: 'app-cartao',
  templateUrl: './cartao.page.html',
  styleUrls: ['./cartao.page.scss'],
  standalone: true,
  imports: [IonCol, IonRow, IonLabel, IonItem, IonCardContent, IonCardSubtitle, IonCardTitle, IonCardHeader, IonImg, IonIcon, IonCard, IonBackButton, IonButtons, IonButton, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule]
})
export class CartaoPage implements OnInit {

  constructor() {
    addIcons({pin, wifi, wine, warning, walk})
  }

  ngOnInit() {}

}
