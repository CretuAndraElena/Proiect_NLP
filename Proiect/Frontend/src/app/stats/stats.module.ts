import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SharedModule } from '../shared/shared.module';
import { StatsComponent } from './components/stats/stats.component';

@NgModule({
  imports: [CommonModule, SharedModule, FormsModule],
  declarations: [StatsComponent]
})
export class StatsModule {}
