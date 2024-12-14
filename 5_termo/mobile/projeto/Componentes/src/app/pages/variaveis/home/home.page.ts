import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonSelect, IonSelectOption, IonContent, IonHeader, IonTitle, IonToolbar, IonLabel, IonItem, IonButton, IonButtons, IonBackButton, IonInput } from '@ionic/angular/standalone';
import { NavigationExtras, Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
  standalone: true,
  imports: [IonInput, IonBackButton, IonButtons, IonButton, IonItem, IonLabel, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonSelectOption, IonSelect]
})
export class HomePage {

  private router;
  public nome: String = '';
  public idade: Number = 0;
  public sexo: String = '';

  constructor() {
    this.router = inject(Router);
  }

  getValores() {
    console.log(this.nome);
    console.log(this.idade);
    console.log(this.sexo);
  }

  enviar() {
    let navigationExtras: NavigationExtras = {
      state: {
        nome: this.nome,
        idade: this.idade,
        sexo: this.sexo,
      },
    };
    this.router.navigate(['variaveis/detalhes'], navigationExtras);
  }
}
