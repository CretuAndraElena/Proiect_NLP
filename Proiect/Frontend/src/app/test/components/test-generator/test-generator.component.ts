import { Component, OnInit } from '@angular/core';
import * as questions from '../../../../assets/questions.json';
import { Test, Question } from '../../models/Test.js';

@Component({
  selector: 'app-test-generator',
  templateUrl: './test-generator.component.html',
  styleUrls: ['./test-generator.component.scss']
})

export class TestGeneratorComponent implements OnInit {
  questions: any = questions;
  public multiple_question: Test = new Test();
  public input: Test = new Test();
  public translate: Test = new Test();

  constructor() {
    this.multiple_question.type = 1;
    this.multiple_question.questions = questions['multiple_choice']as Array<Question>;
    this.input.type = 0;
    this.input.questions = questions['input']as Array<Question>;
    this.translate.type = 0;
    this.translate.questions = questions['translate'] as Array<Question>;
  }

  ngOnInit() {}

}
