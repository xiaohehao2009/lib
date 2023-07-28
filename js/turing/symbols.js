class Symbols {
    symbols = new Set();
    empty;
    constructor(empty) {
        if (empty == null) empty = '_';
        this.empty = empty;
        this.add(empty);
    }
    add(symbol) {
        this.symbols.add(symbol);
    }
    get length() {
        return this.symbols.size;
    }
}

export default Symbols;
