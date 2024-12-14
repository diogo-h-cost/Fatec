import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive } from '@angular/router';
import { IonApp, IonSplitPane, IonMenu, IonContent, IonList, IonListHeader, IonNote, IonMenuToggle, IonItem, IonIcon, IonLabel, IonRouterOutlet, IonRouterLink } from '@ionic/angular/standalone';
import { addIcons } from 'ionicons';
import { heartOutline, heartSharp, warningOutline, warningSharp, albumsSharp, albumsOutline, browsersOutline, browsersSharp, addCircleOutline, addCircleSharp, notificationsOutline, notificationsSharp, bugOutline, bugSharp, bookmarkSharp, bookmarkOutline } from 'ionicons/icons';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  standalone: true,
  imports: [RouterLink, RouterLinkActive, CommonModule, IonApp, IonSplitPane, IonMenu, IonContent, IonList, IonListHeader, IonNote, IonMenuToggle, IonItem, IonIcon, IonLabel, IonRouterLink, IonRouterOutlet],
})
export class AppComponent {
  public appPages = [
    { title: 'Botões', url: '/botoes', icon: 'albums' },
    { title: 'Alerta', url: '/alerta', icon: 'warning' },
    { title: 'Badges', url: '/badges', icon: 'heart' },
    { title: 'Cartão', url: '/cartao', icon: 'browsers' },
    { title: 'Toast', url: '/toast', icon: 'notifications' },
    { title: 'Fab', url: '/fab', icon: 'add-circle' },
    { title: 'Variáveis', url: '/variaveis/home', icon: 'bug' }
  ];
  public labels = ['Work', 'Travel', 'Reminders'];
  constructor() {
    addIcons({ heartOutline, heartSharp, warningOutline, warningSharp, albumsSharp, albumsOutline, browsersOutline, browsersSharp, addCircleOutline, addCircleSharp, notificationsOutline, notificationsSharp, bugOutline, bugSharp, bookmarkSharp, bookmarkOutline });
  }
}
