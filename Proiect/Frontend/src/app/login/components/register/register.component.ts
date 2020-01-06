import { Component, OnInit, ViewChild } from '@angular/core';
import { LoginService } from '../../services/login.service';

@Component({
  // tslint:disable-next-line: component-selector
  selector: 'sn-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  @ViewChild('registerForm') registerForm: { value: any; };
  public loading = false;
  public error = false;
  public success = false;

  constructor(private loginService: LoginService) {}

  ngOnInit() {}

  submit(): void {
    this.loading = true;
    this.loginService.createAccount(this.registerForm.value).subscribe(
      () => {
        this.loading = false;
        this.error = false;
        this.success = true;
      },
      () => {
        this.error = true;
        this.loading = false;
        this.success = false;
      }
    );
  }
}
