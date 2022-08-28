class BigNum {
    private num;

    private reverseResult;

    constructor(num: string) {
        this.num = num;
        this.reverseResult = num.split("").reverse().join("");
    }

    next() {
        const a = this.num;
        const b = this.reverseResult;
        const { length } = a;
        const arr: number[] = [];
        let flag = 0;
        for (let index = length - 1; index >= 0; index--) {
            let value = +a[index] + +b[index] + flag;
            if (value >= 10) {
                if (!flag) {
                    flag = 1;
                }
                value -= 10;
            } else if (flag) {
                flag = 0;
            }
            arr.unshift(value);
        }
        if (flag) {
            arr.unshift(1);
        }
        this.num = arr.join("");
        this.reverseResult = arr.reverse().join("");
        return this.num === this.reverseResult;
    }

    getNum() {
        return this.num;
    }

    getReverseResult() {
        return this.reverseResult;
    }
}

export default BigNum;
