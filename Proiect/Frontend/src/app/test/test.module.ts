import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SharedModule } from '../shared/shared.module';
import { FormsModule } from '@angular/forms';
import { TestGeneratorComponent } from './components/test-generator/test-generator.component';
import { QuestionsComponent } from './components/questions/questions.component';
import { QuestionComponent } from './components/questions/question/question.component';

@NgModule({
  imports: [CommonModule, SharedModule, FormsModule],
  declarations: [TestGeneratorComponent, QuestionsComponent, QuestionComponent]
})
export class TestModule {}
