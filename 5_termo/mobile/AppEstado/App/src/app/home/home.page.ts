import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonSelect, IonSelectOption, IonHeader, IonToolbar, IonTitle, IonContent, IonList } from '@ionic/angular/standalone';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  standalone: true,
  imports: [IonSelect, IonSelectOption, IonList, IonHeader, IonToolbar, IonTitle, IonContent, FormsModule, CommonModule],
})
export class HomePage {

  public estados: Array<any> = [];
  public selectedEstado: any = null;

  constructor() {
    this.estados = [
      {"nome": "Acre", "sigla": "AC", "regiao": "Norte", "capital": "Rio Branco", "habitantes": 413418},
      {"nome": "Alagoas", "sigla": "AL", "regiao": "Nordeste", "capital": "Maceió", "habitantes": 1031910},
      {"nome": "Amapá", "sigla": "AP", "regiao": "Norte", "capital": "Macapá", "habitantes": 512902},
      {"nome": "Amazonas", "sigla": "AM", "regiao": "Norte", "capital": "Manaus", "habitantes": 2277015},
      {"nome": "Bahia", "sigla": "BA", "regiao": "Nordeste", "capital": "Salvador", "habitantes": 2930012},
      {"nome": "Ceará", "sigla": "CE", "regiao": "Nordeste", "capital": "Fortaleza", "habitantes": 2686612},
      {"nome": "Distrito Federal", "sigla": "DF", "regiao": "Centro-Oeste", "capital": "Brasília", "habitantes": 3189401},
      {"nome": "Espírito Santo", "sigla": "ES", "regiao": "Sudeste", "capital": "Vitória", "habitantes": 365855},
      {"nome": "Goiás", "sigla": "GO", "regiao": "Centro-Oeste", "capital": "Goiânia", "habitantes": 1572866},
      {"nome": "Maranhão", "sigla": "MA", "regiao": "Nordeste", "capital": "São Luís", "habitantes": 1180423},
      {"nome": "Mato Grosso", "sigla": "MT", "regiao": "Centro-Oeste", "capital": "Cuiabá", "habitantes": 636478},
      {"nome": "Mato Grosso do Sul", "sigla": "MS", "regiao": "Centro-Oeste", "capital": "Campo Grande", "habitantes": 904737},
      {"nome": "Minas Gerais", "sigla": "MG", "regiao": "Sudeste", "capital": "Belo Horizonte", "habitantes": 2521564},
      {"nome": "Pará", "sigla": "PA", "regiao": "Norte", "capital": "Belém", "habitantes": 1691000},
      {"nome": "Paraíba", "sigla": "PB", "regiao": "Nordeste", "capital": "João Pessoa", "habitantes": 817511},
      {"nome": "Paraná", "sigla": "PR", "regiao": "Sul", "capital": "Curitiba", "habitantes": 1963726},
      {"nome": "Pernambuco", "sigla": "PE", "regiao": "Nordeste", "capital": "Recife", "habitantes": 1645727},
      {"nome": "Piauí", "sigla": "PI", "regiao": "Nordeste", "capital": "Teresina", "habitantes": 874314},
      {"nome": "Rio de Janeiro", "sigla": "RJ", "regiao": "Sudeste", "capital": "Rio de Janeiro", "habitantes": 6748000},
      {"nome": "Rio Grande do Norte", "sigla": "RN", "regiao": "Nordeste", "capital": "Natal", "habitantes": 896708},
      {"nome": "Rio Grande do Sul", "sigla": "RS", "regiao": "Sul", "capital": "Porto Alegre", "habitantes": 1480000},
      {"nome": "Rondônia", "sigla": "RO", "regiao": "Norte", "capital": "Porto Velho", "habitantes": 539354},
      {"nome": "Roraima", "sigla": "RR", "regiao": "Norte", "capital": "Boa Vista", "habitantes": 438273},
      {"nome": "Santa Catarina", "sigla": "SC", "regiao": "Sul", "capital": "Florianópolis", "habitantes": 508826},
      {"nome": "São Paulo", "sigla": "SP", "regiao": "Sudeste", "capital": "São Paulo", "habitantes": 12300000},
      {"nome": "Sergipe", "sigla": "SE", "regiao": "Nordeste", "capital": "Aracaju", "habitantes": 657013},
      {"nome": "Tocantins", "sigla": "TO", "regiao": "Norte", "capital": "Palmas", "habitantes": 306296}
    ];
  }

  onEstadoChange() {
    console.log("Estado selecionado: ", this.selectedEstado);
  }
}
