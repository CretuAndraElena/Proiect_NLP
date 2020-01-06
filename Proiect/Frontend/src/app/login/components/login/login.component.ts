import { Component, OnInit, ViewChild } from '@angular/core';
import { Router } from '@angular/router';
import { LoginService } from '../../services/login.service';
import { AuthenticationService } from 'src/app/shared/services/auth.service';

@Component({
  // tslint:disable-next-line: component-selector
  selector: 'sn-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  @ViewChild('loginForm') loginForm;

  public loading = false;
  public error = false;

  constructor(
    private loginService: LoginService,
    private auth: AuthenticationService,
    private router: Router
  ) {}

  ngOnInit() {}

  submit(loginModel): void {
    if (loginModel.valid) {
      this.loading = true;
      this.loginService.login(loginModel.value).subscribe(
        (res: any) => {
          localStorage.setItem('id', res.toString());
          this.auth.saveToken('succes');
          this.loading = false;
          this.error = false;
          this.router.navigate(['/generate']);
        },
        () => {
          this.loading = false;
          this.error = true;
        }
      );
    }
  }
}
