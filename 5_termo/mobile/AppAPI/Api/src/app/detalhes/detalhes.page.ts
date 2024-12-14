import { Component, inject, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonContent, IonHeader, IonTitle, IonToolbar, IonButtons, IonBackButton, IonList, IonImg, IonItem, IonAvatar, IonLabel } from '@ionic/angular/standalone';
import { ActivatedRoute } from '@angular/router';
import { TvService } from '../services/tv.service';

@Component({
  selector: 'app-detalhes',
  templateUrl: './detalhes.page.html',
  styleUrls: ['./detalhes.page.scss'],
  standalone: true,
  imports: [IonLabel, IonAvatar, IonItem, IonImg, IonList, IonBackButton, IonButtons, IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule]
})
export class DetalhesPage implements OnInit {

  private route = inject(ActivatedRoute);
  private tvService = inject(TvService);
  public id = "";
  public qtdeSessoes = 0;
  public session = null;
  public imagem = null;
  public nome = null;
  public summary = null;
  public dados = null;
  public elenco: { actorName: string, actorPhoto: string, characterName: string}[] = [];

  constructor() {}

  ngOnInit() {
    this.id = this.route.snapshot.paramMap.get('id') || "";

    this.tvService.getDetalhes(this.id)
    .subscribe((dados: any) => {
      this.dados = dados;
      this.nome = dados['name'];
      this.imagem = dados['image']['original'];
      this.summary = dados['summary'];
    });

    this.tvService.getSessions(this.id)
    .subscribe((dados: any) => {
      this.session = dados;
      this.qtdeSessoes = dados.length;
    });

    this.tvService.getElenco(this.id).subscribe((dados: any[]) => {
      this.elenco = dados.map((entry) => ({
        actorName: entry.person.name,
        actorPhoto: entry.person.image?.original || '',
        characterName: entry.character.name
      }));
    });
  }
}
