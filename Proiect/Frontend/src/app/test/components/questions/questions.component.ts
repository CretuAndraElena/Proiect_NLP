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
    const mq = questions['multiple_choice'] as Array<Question>;
    const iq = questions['input'] as Array<Question>;

    this.multiple_questions.questions = this.shuffle(mq.filter(q => q.category === category));
    this.input.questions = this.shuffle(iq.filter(q => q.category === category));
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

  shuffle(arra1: any[]) {
      let ctr = arra1.length;
      let temp;
      let index;

      while (ctr > 0) {
          index = Math.floor(Math.random() * ctr);
          ctr--;
          temp = arra1[ctr];
          arra1[ctr] = arra1[index];
          arra1[index] = temp;
      }
      return arra1;
  }
}
