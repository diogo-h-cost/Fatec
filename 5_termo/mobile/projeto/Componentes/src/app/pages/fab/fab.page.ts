import { addIcons } from 'ionicons';
import { add, chevronForwardCircle, document, colorPalette, globe, chevronUp, chevronDown, chevronBack, chevronForward } from 'ionicons/icons';
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonBackButton, IonItem, IonFab, IonFabButton, IonIcon, IonFabList, IonList, IonLabel, IonAvatar, IonInfiniteScroll, IonInfiniteScrollContent } from '@ionic/angular/standalone';
import { InfiniteScrollCustomEvent } from '@ionic/angular';

@Component({
  selector: 'app-fab',
  templateUrl: './fab.page.html',
  styleUrls: ['./fab.page.scss'],
  standalone: true,
  imports: [IonInfiniteScrollContent, IonInfiniteScroll, IonAvatar, IonLabel, IonList, IonFabList, IonIcon, IonFabButton, IonFab, IonItem, IonBackButton, IonButtons, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule]
})
export class FabPage implements OnInit {
  items: string[] = [];

  constructor() {
    addIcons({ add, chevronForwardCircle, document, colorPalette, globe, chevronUp, chevronForward, chevronDown, chevronBack });
  }

  ngOnInit() {
    this.generateItems();
  }

  private generateItems() {
    const count = this.items.length + 1;
    for (let i = 0; i < 50; i++) {
      this.items.push(`Item ${count + i}`);
    }
  }

  onIonInfinite(ev: InfiniteScrollCustomEvent) {
    this.generateItems();
    setTimeout(() => {
      ev.target.complete();
    }, 500);
  }
}
