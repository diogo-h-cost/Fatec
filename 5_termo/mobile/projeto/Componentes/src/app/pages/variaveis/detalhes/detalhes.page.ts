import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonBackButton, IonItem, IonLabel } from '@ionic/angular/standalone';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-detalhes',
  templateUrl: './detalhes.page.html',
  styleUrls: ['./detalhes.page.scss'],
  standalone: true,
  imports: [IonLabel, IonItem, IonBackButton, IonButtons, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule]
})
export class DetalhesPage {

  private route = inject(Router);
  private activedRoute = inject(ActivatedRoute);
  public nome!: String;
  public idade!: Number;
  public sexo!: String;
  public s!: String;

  constructor() {
    this.activedRoute.queryParams.subscribe(() => {
      let state = this.route.getCurrentNavigation()?.extras.state;
      if (state) {
        this.nome = state['nome'];
        this.idade = state['idade'];
        this.s = state['sexo'];
      }
      if (this.s == 'm') {
        this.sexo = 'Masculino';
      } else {
        this.sexo = 'Feminino';
      }
    });
  }
}
