import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonBackButton, IonBadge, IonItem, IonLabel, IonButton, IonList } from '@ionic/angular/standalone';

@Component({
  selector: 'app-badges',
  templateUrl: './badges.page.html',
  styleUrls: ['./badges.page.scss'],
  standalone: true,
  imports: [IonList, IonButton, IonLabel, IonItem, IonBadge, IonBackButton, IonButtons, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule]
})
export class BadgesPage implements OnInit {

  constructor() { }

  ngOnInit() {
  }

}
