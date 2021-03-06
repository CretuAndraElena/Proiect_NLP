import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginComponent } from './login/components/login/login.component';
import { RegisterComponent } from './login/components/register/register.component';
import { TestGeneratorComponent } from './test/components/test-generator/test-generator.component';
import { AuthGuard } from './shared/guards/auth.guard';
import { StatsComponent } from './stats/components/stats/stats.component';
import { QuestionsComponent } from './test/components/questions/questions.component';
import { HomeComponent } from './home/components/home/home.component';

const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'home', component: HomeComponent },
  {
    path: 'generate/:term',
    component: QuestionsComponent,
    canActivate: [AuthGuard]
  },
  {
    path: 'newtest',
    component: TestGeneratorComponent
    // canActivate: [AuthGuard],
  },
  { path: 'statistics', component: StatsComponent, canActivate: [AuthGuard] },
  {
    path: '**',
    redirectTo: ''
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
