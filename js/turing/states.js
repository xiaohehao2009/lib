class States {
    states = new Set();
    initail;
    stop;
    constructor(initail, stop) {
        if (initail != null) this.initail = initail;
        if (stop == null) this.stop = 'stop';
        else this.stop = stop;
        this.states.add(this.stop);
    }
    add(state) {
        this.states.add(state);
        if (!this.initail) {
            this.initail = state;
        }
    }
    get length() {
        return this.states.size;
    }
}

export default States;
