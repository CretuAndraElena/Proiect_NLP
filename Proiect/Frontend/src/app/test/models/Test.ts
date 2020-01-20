export class Test {
  type: boolean;
  questions: Array<Question>;
}

export class Question {
  body: string;
  goodAnswer: string;
  answers?: Array<Answer>;
  category: string;
}

export class Answer {
  body: string;
  isCorrect: boolean;
}
