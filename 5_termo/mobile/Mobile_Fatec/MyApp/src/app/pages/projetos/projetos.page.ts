import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonBackButton, IonButton, IonFooter, IonItem, IonCard, IonCardHeader, IonCardTitle, IonCardContent, IonList } from '@ionic/angular/standalone';

@Component({
  selector: 'app-projetos',
  templateUrl: './projetos.page.html',
  styleUrls: ['./projetos.page.scss'],
  standalone: true,
  imports: [IonList, IonCardContent, IonCardTitle, IonCardHeader, IonCard, IonItem, IonFooter, IonButton, IonBackButton, IonButtons, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule]
})
export class ProjetosPage implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  navigateHome() {
    this.router.navigate(['/home']);
  }
}
