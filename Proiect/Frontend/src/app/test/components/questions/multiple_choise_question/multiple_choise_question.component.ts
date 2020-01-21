import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Question } from 'src/app/test/models/Test';

@Component({
  selector: 'app-multiple-choise-question',
  templateUrl: './multiple_choise_question.component.html',
  styleUrls: ['./multiple_choise_question.component.scss']
})
export class MultipleChoiseQuestionComponent implements OnInit {
  @Input() question: Question;
  @Output()
  answered = new EventEmitter();
  checked = -1;
  hasChecked = false;

  public asnwers: Array<string>;
  public selected_answer: string;
  isCorrect: boolean;
  constructor() {}

  ngOnInit() {
    this.asnwers = this.question.wrong_answers;
    this.asnwers.push(this.question.corect);
  }

  onClickSubmit() {
    this.answered.emit();
  }

  onCheck(data: { answer: string }) {
    if (data.answer === this.question.corect) {
      this.isCorrect = true;
    } else {
      this.isCorrect = false;
    }

    this.hasChecked = true;
  }
}
