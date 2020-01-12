import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { HeaderComponent } from './components/header/header.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { HttpService } from './services/http.service';
import { AuthenticationService } from './services/auth.service';
import { AuthGuard } from './guards/auth.guard';
import { HttpClientModule } from '@angular/common/http';
import {SuiModule} from 'ng2-semantic-ui';

@NgModule({
  imports: [CommonModule, HttpClientModule, SuiModule],
  declarations: [NavbarComponent, HeaderComponent],
  exports: [NavbarComponent, HeaderComponent, SuiModule],
  providers: [HttpService, AuthenticationService, AuthGuard]
})
export class SharedModule {}
