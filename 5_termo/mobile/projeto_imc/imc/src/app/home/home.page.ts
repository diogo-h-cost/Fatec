import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonSelect, IonSelectOption, IonHeader, IonToolbar, IonTitle, IonContent, IonItem, IonLabel, IonInput, IonButton } from '@ionic/angular/standalone';
import { NavigationExtras, Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  standalone: true,
  imports: [IonButton, IonInput, IonSelect, IonSelectOption, IonLabel, IonItem, IonHeader, IonToolbar, IonTitle, IonContent, FormsModule, CommonModule],
})
export class HomePage {

  private router;
  public sexo: String = '';
  public peso: Number = 0;
  public altura: Number = 0;

  constructor() {
    this.router = inject(Router);
  }

  enviar() {
    let navigationExtras: NavigationExtras = {
      state: {
        sexo: this.sexo,
        peso: this.peso,
        altura: this.altura,
      },
    };
    this.router.navigate(['indice'], navigationExtras);
  }
}
