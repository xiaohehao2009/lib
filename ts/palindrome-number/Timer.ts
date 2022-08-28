class Timer {
    private start;

    constructor() {
        this.start = performance.now();
    }

    static create() {
        return new Timer();
    }

    do(fn: () => void) {
        fn();
        return this;
    }

    end() {
        console.log(`用时: ${(performance.now() - this.start).toFixed(3)} ms`);
    }
}

export default Timer;
