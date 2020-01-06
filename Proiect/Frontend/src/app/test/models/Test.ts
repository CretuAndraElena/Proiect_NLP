export class Test {
  category: string;
  questions: Array<Question>;
}

export class Question {
  id: string;
  answers: Array<Answer>;
}

export class Answer {
  body: string;
  isCorresc: boolean;
}
