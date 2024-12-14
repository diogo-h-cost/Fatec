import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonButton, IonButtons, IonBackButton, IonImg, IonItem, IonLabel } from '@ionic/angular/standalone';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-indice',
  templateUrl: './indice.page.html',
  styleUrls: ['./indice.page.scss'],
  standalone: true,
  imports: [IonLabel, IonItem, IonImg, IonBackButton, IonButtons, IonButton, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule]
})
export class IndicePage {

  private route = inject(Router);
  private activedRoute = inject(ActivatedRoute);
  public sexo!: string;
  public s!: string;
  public peso!: number;
  public altura!: number;
  public imc!: number;
  public clas!: string;

  constructor() {
    this.activedRoute.queryParams.subscribe(() => {
      let state = this.route.getCurrentNavigation()?.extras.state;
      if (state) {
        this.s = state['sexo'];
        this.peso = state['peso'];
        this.altura = state['altura'];
      }
      if (this.s == 'm') {
        this.sexo = 'Masculino';
      } else {
        this.sexo = 'Feminino';
      }
    });
  }

  calcularIMC(): void {
    if (this.peso && this.altura) {
      this.imc = this.peso / (this.altura * this.altura);
      this.clas = this.classificacaoIMC(this.imc, this.sexo);
    } else {
      console.error('Peso ou altura não foram definidos corretamente.');
    }
  }

  classificacaoIMC(imc: number, sexo: string): string {
    if (sexo == 'Masculino') {
      if (imc < 20.0) return 'Abaixo do peso';
      else if (imc < 25.0) return 'Normal';
      else if (imc < 30.0) return 'Obesidade leve';
      else if (imc < 40.0) return 'Obesidade moderada';
      else return 'Obesidade mórbida';
    } else { // Feminino
      if (imc < 19.0) return 'Abaixo do peso';
      else if (imc < 24.0) return 'Normal';
      else if (imc < 29.0) return 'Obesidade leve';
      else if (imc < 39.0) return 'Obesidade moderada';
      else return 'Obesidade mórbida';
    }
  }
}
