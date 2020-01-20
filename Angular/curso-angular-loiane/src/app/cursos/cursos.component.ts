import { CursosService } from './cursos.service';
import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-cursos',
  templateUrl: './cursos.component.html',
  styleUrls: ['./cursos.component.css']
})
export class CursosComponent implements OnInit {

  nomePortal: string;
  listaDeCursos: string[];
  imgUrl = "https://i.picsum.photos/id/868/200/300.jpg";

  constructor(private cursosService : CursosService) { // Injeção de dependencia via construtor
    this.nomePortal = 'http://medium.com/@crazyccblog';

    this.listaDeCursos = this.cursosService.getCursos();

  }

  getNumber(){
    return 3;
  }

  ngOnInit() {
  }

}
