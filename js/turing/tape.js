import chalk from 'chalk';

class Tape {
    tape;
    index;
    empty;

    constructor(empty, data) {
        this.empty = empty;
        if (data.length) {
            this.tape = [...data];
            this.index = this.tape.length - 1;
        } else {
            this.tape = [empty];
            this.index = 0;
        }
    }
    get() {
        return this.tape[this.index];
    }
    set(value) {
        this.tape[this.index] = value;
    }
    R() {
        if (!this.index) {
            this.tape.unshift(this.empty);
        }
        else this.index--;
    }
    L() {
        this.index++;
        if (this.index === this.tape.length) {
            this.tape.push(this.empty);
        }
    }
    toString() {
        return this.tape.with(this.index,
            chalk.bgWhite.black(this.get())).join(' ');
    }
}

export default Tape;
