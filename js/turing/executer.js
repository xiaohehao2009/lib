import compile from './compiler.js';
import Tape from './tape.js';

class Executer {
    static create(source) {
        return new Executer(compile(source));
    }
    static get(executer) {
        for (let i = 1; ; i++) {
            executer.next();
            if (executer.stopped) return {
                step: i,
                output: executer.toString()
            };
        }
    }
    static runFromSource(source) {
        const exe = Executer.create(source);
        const result = exe.result;
        const max = exe.result.statements.maxStep
        if (!(result.commands.includes('repl') ||
            result.commands.includes('REPL'))) {
            let step = 0;
            while (!exe.stopped) {
                exe.next();
                step++;
            }
            console.log(`Step: ${step}`);
            console.log(`Result: ${exe}`);
            return;
        }
        console.log(`Beginning: ${exe}`);
        console.log(`  with ${exe.states.length} states, ` +
            `${exe.symbols.length} symbols`);
        for (let step = 1; ; step++) {
            exe.next();
            console.log(`Step ${step}: ${exe}`);
            if (exe.stopped) break;
        }
    }

    tape;
    state;
    states;
    symbols;
    stop;
    result;
    stopped = false;
    step = 0;
    max;
    constructor(result) {
        this.result = result;
        this.state = result.states.initail;
        this.states = result.states;
        this.symbols = result.symbols;
        this.tape = new Tape(this.symbols.empty, result.data);
        this.stop = this.states.stop;
        this.max = result.max || Infinity;
    }
    next() {
        if (this.stopped) {
            return;
        }
        const symbol = this.tape.get();
        const code = this.result.get(this.state, symbol);
        if (code === null) {
            console.log(this.tape.toString());
            throw new Error(`state ${this.state}, ` +
                `symbol ${symbol} not defined`);
        }
        this.tape.set(code[1]);
        code[0](this.tape);
        this.state = code[2];
        this.step++;
        if (this.state === this.stop || this.step >= this.max) {
            this.stopped = true;
        }
    }
    toString() {
        return `State: ${this.state} Tape: ${this.tape}`;
    }
}

export default Executer;
