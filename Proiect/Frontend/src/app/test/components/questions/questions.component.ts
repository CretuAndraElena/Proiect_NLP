import { Component, OnInit, Input, ViewChild, ElementRef } from '@angular/core';
import * as questions from '../../../../assets/questions.json';
import { Test, Question } from '../../models/Test';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.scss']
})
export class QuestionsComponent implements OnInit {
  questions: any = questions;
  currentQuestionM = 0;
  currentQuestionI = -1;
  questionMode: 'Multiple' | 'Input';
  public multiple_questions: Test = new Test();
  public input: Test = new Test();
  public translate: Test = new Test();

  @ViewChild('question') div: ElementRef;

  constructor(private route: ActivatedRoute) {
    let category = '';
    this.route.params.subscribe(params => (category = params.term));

    this.multiple_questions.type = 1;
    //this.input.type = 0;
    const mq = questions['multiple_choice'] as Array<Question>;
    const iq = questions['input'] as Array<Question>;

    this.multiple_questions.questions = mq.filter(q => q.category === category);
    this.input.questions = iq.filter(q => q.category === category);
  }

  ngOnInit() {
    this.questionMode = 'Multiple';
  }

  onAnswered() {
    if (this.questionMode === 'Multiple') {
      this.currentQuestionM++;
      this.questionMode = 'Input';
      this.currentQuestionI++;
    } else {
      this.questionMode = 'Multiple';
    }
  }
}
