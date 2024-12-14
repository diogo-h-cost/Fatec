import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { IonHeader, IonToolbar, IonTitle, IonContent, IonButton, IonIcon, IonList, IonListHeader, IonLabel, IonItem, IonCard, IonCardHeader, IonCardTitle, IonCardContent, IonNote, IonButtons, IonFooter, IonRouterLink } from '@ionic/angular/standalone';
import { addIcons } from 'ionicons';
import { informationCircle } from 'ionicons/icons'

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  standalone: true,
  imports: [IonRouterLink, IonFooter, IonButtons, IonNote, IonCardContent, IonCardTitle, IonCardHeader, IonCard, IonItem, IonLabel, IonListHeader, IonList, IonHeader, IonToolbar, IonTitle, IonContent, IonButton, IonIcon],
})
export class HomePage {

  constructor(private router: Router) {
    addIcons({informationCircle});
  }

  navigateHome() {
    this.router.navigate(['/home']);
  }

  sobre(){
    this.router.navigate(["/sobre"]);
  }

  contato(){
    this.router.navigate(["/contato"]);
  }

  projetos(){
    this.router.navigate(["/projetos"]);
  }
}
