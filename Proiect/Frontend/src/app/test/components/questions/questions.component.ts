import { Component, OnInit, Input, ViewChild, ElementRef } from '@angular/core';
import * as questions from '../../../../assets/questions.json';
import { Test, Question } from '../../models/Test';
import { MultipleChoiseQuestionComponent } from './multiple_choise_question/multiple_choise_question.component.js';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.scss']
})
export class QuestionsComponent implements OnInit {
  questions: any = questions;
  public multiple_questions: Test = new Test();
  public input: Test = new Test();
  public translate: Test = new Test();

  @ViewChild('question') div: ElementRef;

  constructor(private route: ActivatedRoute) {
    let category = '';
    this.route.params.subscribe(params => (category = params.term));

    this.multiple_questions.type = 1;
    const mq = questions['multiple_choice'] as Array<Question>;
    const iq = questions['input'] as Array<Question>;

    this.multiple_questions.questions = mq.filter(q => q.category === category);
    this.input.questions = iq.filter(q => q.category === category);
  }

  ngOnInit() {}
}
