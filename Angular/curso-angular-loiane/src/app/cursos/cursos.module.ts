import { CursosService } from './cursos.service';
import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CursosComponent } from './cursos.component';
import { DetalheComponent } from './detalhe/detalhe.component';
import { TooltipModule } from 'ngx-bootstrap/tooltip';


@NgModule({
  declarations: [CursosComponent, DetalheComponent],
  imports: [
    CommonModule,
    TooltipModule.forRoot()
  ],
  exports: [CursosComponent],
  providers : [CursosService]
})
export class CursosModule { }
