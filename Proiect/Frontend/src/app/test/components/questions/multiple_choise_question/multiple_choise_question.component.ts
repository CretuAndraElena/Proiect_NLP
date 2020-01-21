import { Component, OnInit, Input } from '@angular/core';
import { Question } from 'src/app/test/models/Test';

@Component({
  selector: 'app-multiple-choise-question',
  templateUrl: './multiple_choise_question.component.html',
  styleUrls: ['./multiple_choise_question.component.scss']
})
export class MultipleChoiseQuestionComponent implements OnInit {
  @Input() question: Question;
  public asnwers: Array<string>;
  public selected_answer: string;
  isCorrect?: boolean;
  constructor() {}

  ngOnInit() {
    this.asnwers = this.question.wrong_answers;
    this.asnwers.push(this.question.corect);
  }

  onClickSubmit(data: { answer: string; }) {
    if (data.answer === this.question.corect) {
      alert('Raspuns corect :D');
      this.isCorrect = true;
    } else {
      alert('Raspuns gresit. :(\n Vei reusi data viitoare.');
      this.isCorrect = false;
    }
  }
}
