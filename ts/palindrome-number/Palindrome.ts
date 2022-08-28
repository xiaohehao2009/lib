import BigNum from "./BigNum";
import ComputeResult from "./ComputeResult";

class Palindrome {
    private num;

    private initNum;

    private maxComputeTimes;

    constructor(initNum: string | number, maxComputeTimes = 1000) {
        this.initNum = initNum;
        this.maxComputeTimes = maxComputeTimes;
        if (typeof initNum === "number") {
            this.num = new BigNum(initNum.toString());
            return;
        }
        this.num = new BigNum(initNum);
    }

    static create(initNum: string | number, maxComputeTimes = 1000) {
        return new Palindrome(initNum, maxComputeTimes);
    }

    compute() {
        if (this.initNum === this.num.getReverseResult()) {
            return new ComputeResult(0, `${this.initNum} 的回文数为 ${this.initNum}`);
        }
        for (let i = 0; i < this.maxComputeTimes; i++) {
            if (this.num.next()) {
                return new ComputeResult(i + 1, `${this.initNum} 的回文数为 ${this.num.getNum()}`);
            }
        }
        return new ComputeResult(this.maxComputeTimes, "没有找到回文数");
    }
}

export default Palindrome;
