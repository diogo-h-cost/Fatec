import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: 'home',
    loadComponent: () => import('./home/home.page').then((m) => m.HomePage),
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full',
  },
  {
    path: 'sobre',
    loadComponent: () => import('./pages/sobre/sobre.page').then( m => m.SobrePage)
  },
  {
    path: 'contato',
    loadComponent: () => import('./pages/contato/contato.page').then( m => m.ContatoPage)
  },
  {
    path: 'projetos',
    loadComponent: () => import('./pages/projetos/projetos.page').then( m => m.ProjetosPage)
  },
  {
    path: 'galeria',
    loadComponent: () => import('./pages/galeria/galeria.page').then( m => m.GaleriaPage)
  },
];
