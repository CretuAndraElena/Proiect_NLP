import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Question } from 'src/app/test/models/Test';

@Component({
  selector: 'app-input-questions',
  templateUrl: './input-questions.component.html',
  styleUrls: ['./input-questions.component.scss']
})
export class InputQuestionsComponent implements OnInit {
  @Input() question: Question;
  @Output()
  answered = new EventEmitter();
  public asnwers: Array<string>;
  public selected_answer: string;
  checked = -1;
  hasChecked = false;
  isCorrect = false;

  constructor() {}

  ngOnInit() {
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
