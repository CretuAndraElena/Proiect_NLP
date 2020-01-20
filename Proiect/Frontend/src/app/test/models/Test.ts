export class Test {
  type: number; // 1 - multiple_choise ; 0 - input
  questions: Array<Question>;
}

export class Question {
  question: string;
  corect: string;
  wrong_answers?: Array<string>;
  category: string;
}
