import { Component, OnInit } from '@angular/core';
import * as questions from '../../../../assets/questions.json';
import { Test } from '../../models/Test.js';

@Component({
  selector: 'app-test-generator',
  templateUrl: './test-generator.component.html',
  styleUrls: ['./test-generator.component.scss']
})
export class TestGeneratorComponent implements OnInit {
  questions: any = questions;

  constructor() {
    // const nameList = questions['multiple_choice'];
    console.log(questions);
  }

  ngOnInit() {}

}
