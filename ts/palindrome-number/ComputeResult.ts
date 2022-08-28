class ComputeResult<ResultT> {
    private times;

    private result;

    constructor(times: number, result: ResultT) {
        this.times = times;
        this.result = result;
    }

    getTimes() {
        return this.times;
    }

    getResult() {
        return this.result;
    }

    print() {
        console.log(`计算了 ${this.times} 次, 计算结果: ${this.result}`);
    }
}

export default ComputeResult;
