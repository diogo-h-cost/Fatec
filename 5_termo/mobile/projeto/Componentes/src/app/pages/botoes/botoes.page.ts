import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonButton, IonButtons, IonBackButton, IonIcon } from '@ionic/angular/standalone';
import { addIcons } from "ionicons";
import { star } from "ionicons/icons";

@Component({
  selector: 'app-botoes',
  templateUrl: './botoes.page.html',
  styleUrls: ['./botoes.page.scss'],
  standalone: true,
  imports: [IonIcon, IonBackButton, IonButtons, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonButton]
})
export class BotoesPage implements OnInit {

  constructor() { }

  ngOnInit() {
    addIcons({star});
  }

}
