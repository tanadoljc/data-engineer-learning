import { Component, signal, computed, effect } from '@angular/core';

@Component({
  selector: 'app-hello',
  imports: [],
  templateUrl: './hello.html',
  styleUrl: './hello.scss',
})
export class Hello {
  protected title = 'This is for Practice!'
  protected isDisabled = false;
  protected count = signal(0);
  protected double = computed(() => this.count() * 2);
  protected readonly countLog = effect(() => {
    console.log('Count: ', this.count());
  })

  // receive value from Parent -> Child
  // readonly product = input.required<Interface>();
  // readonly buttonLabel = input(initValue);

  // emit value from Child -> Parent
  // readonly addToCart = output<Interface>();
  // protected onAddToCard() {
  //  this.addToCart.emit(this.product())
  // }

  protected onClick() {
    this.isDisabled = !this.isDisabled;
  }

  protected addValue() {
    this.count.update(value=>value+1);
  }

  protected minusValue() {
    this.count.update(value=>value-1);
  }

  protected resetValue() {
    this.count.set(0);
  }
}
