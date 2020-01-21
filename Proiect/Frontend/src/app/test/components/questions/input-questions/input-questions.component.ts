import { Component, OnInit, Input } from '@angular/core';
import { Question } from 'src/app/test/models/Test';

@Component({
  selector: 'app-input-questions',
  templateUrl: './input-questions.component.html',
  styleUrls: ['./input-questions.component.scss']
})
export class InputQuestionsComponent implements OnInit {

  @Input() question: Question;
  public asnwers: Array<string>;
  public selected_answer: string;
  isChecked = false;
  constructor() {}

  ngOnInit() {
    this.asnwers = this.question.wrong_answers;
    this.asnwers.push(this.question.corect);
  }

  onClickSubmit(data) {
    if (data.answer === this.question.corect) {
      alert('Raspuns corect :D');
    } else {
      alert('Raspuns gresit. :(\n Vei reusi data viitoare.');
    }
    this.isChecked = true;
  }

}
