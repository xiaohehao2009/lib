import TapeMove from './tapemove.js';
import States from './states.js';
import Symbols from './symbols.js';

class CompileResult {
    result = new Map();
    generics = [];
    symbols = new Symbols();
    states = new States();
    commands;
    statements;
    data;
    max;

    constructor({ commands, statements, rules }) {
        this.commands = commands;
        this.statements = statements;
        this.symbols = new Symbols((statements.replaceEmpty || [])[0]);
        this.states = new States(
            (statements.replaceInitail || [])[0],
            (statements.replaceStop || [])[0]);
        this.max = +(statements.maxStep || [])[0];
        if (typeof this.max !== 'number' || this.max < 0) {
            throw new Error('Invalid maxstep: ' + this.max);
        }
        this.data = statements.tapeData;
        for (const rule of rules) this.add(...rule);
        this.end();
    }

    add(state, symbol, newSymbol, tapeMove, newState) {
        const move = TapeMove.get(tapeMove);
        this.states.add(state);
        if (newState === '$') newState = state;
        else this.states.add(newState);
        if (newSymbol !== '$') this.symbols.add(newSymbol);
        if (symbol === '*') {
            this.generics.push([state, newSymbol, move, newState]);
            return;
        }
        if (newSymbol === '$') newSymbol = symbol;
        this.symbols.add(symbol);
        if (this.has(state, symbol)) {
            throw new Error(`${state}, ${symbol} defined repeatedly`);
        }
        this.set(state, symbol, newSymbol, move, newState);
    }
    set(state, symbol, newSymbol, move, newState) {
        this.result.set(`${state} ${symbol}`, [move, newSymbol, newState]);
    }
    get(state, symbol) {
        if (this.result.has(`${state} ${symbol}`)) {
            return this.result.get(`${state} ${symbol}`);
        }
        if (this.result.has(state)) {
            return this.result.get(state);
        }
        return null;
    }
    has(state, symbol) {
        return this.result.has(`${state} ${symbol}`);
    }
    end() {
        for (const [state, newSymbol, move, newState] of this.generics) {
            if (newSymbol === '$') {
                for (const symbol of this.symbols.symbols) {
                    if (this.has(state, symbol)) continue;
                    this.set(state, symbol, symbol, move, newState);
                }
            } else {
                for (const symbol of this.symbols.symbols) {
                    if (this.has(state, symbol)) continue;
                    this.set(state, symbol, newSymbol, move, newState);
                }
            }
        }
    }
}

export default CompileResult;
