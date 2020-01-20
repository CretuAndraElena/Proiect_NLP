import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpModule} from '@angular/http';
import { AppComponent } from './app.component';
import { TestModule } from './test/test.module';
import { SharedModule } from './shared/shared.module';
import { AppRoutingModule } from './app-rounting.module';
import { LoginModule } from './login/login.module';
import { StatsModule } from './stats/stats.module';
import { HomeComponent } from './home/components/home/home.component';

@NgModule({
  declarations: [AppComponent, HomeComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    TestModule,
    SharedModule,
    LoginModule,
    StatsModule,
    HttpModule
  ],
  providers: [],
  exports: [SharedModule],
  bootstrap: [AppComponent]
})
export class AppModule {}
