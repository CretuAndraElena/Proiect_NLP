import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class LoginService {
  public prefix = '/api';

  private loginUrl: string = this.prefix + '/v1/user/login';
  private registerUrl: string = this.prefix + '/v1/user/register';
  private createTokenURL = '/api/token';

  constructor(private http: HttpClient) {}

  createAccount(account) {
    return this.http.post(this.registerUrl, account);
  }

  login(loginModel) {
    return this.http.post(this.loginUrl, loginModel);
  }
}
