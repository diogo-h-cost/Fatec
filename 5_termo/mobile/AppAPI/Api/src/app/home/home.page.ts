import { Component, inject } from '@angular/core';
import { IonHeader, IonToolbar, IonTitle, IonContent, IonAvatar, IonList, IonItem, IonLabel, IonBadge, IonSkeletonText } from '@ionic/angular/standalone';
import { TvService } from '../services/tv.service';
import { finalize } from 'rxjs';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  standalone: true,
  imports: [RouterModule, CommonModule, IonSkeletonText, IonBadge, IonLabel, IonHeader, IonToolbar, IonTitle, IonContent, IonAvatar, IonList, IonItem],
})
export class HomePage {

  private tvService = inject(TvService);
  public listaShow: any;
  public isLoading = false;
  public dummyArray = new Array(7);

  constructor() {

    this.isLoading = true;
    this.tvService.getShows()
    .pipe(
      finalize(() => {
        this.isLoading = false;
      })
    )
    .subscribe((dados) => {
        console.log(dados);
        this.listaShow = dados;
      });

    this.tvService.getShows().subscribe((dados) => {
      console.log(dados);
      this.listaShow = dados;
    });
  }
}
