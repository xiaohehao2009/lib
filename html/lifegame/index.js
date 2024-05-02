(() => {
    const width = 300;
    const height = 300;
    const squarePx = 2;
    const time = document.getElementById("time");

    function CanvasOperate() {
        this.el = document.createElement("canvas");
        this.wpx = width * squarePx + 1;
        this.hpx = height * squarePx + 1;
        this.el.width = this.wpx;
        this.el.height = this.hpx;
        this.ctx = this.el.getContext("2d", { alpha: false });
        this.whites = [];
        this.blacks = [];
        this.initGrid();
        document.getElementById("app").appendChild(this.el);
    }
    CanvasOperate.prototype.initGrid = function () {
        const ctx = this.ctx;
        ctx.fillStyle = "#555";
        ctx.fillRect(1, 1, width * squarePx, height * squarePx)
        ctx.fillStyle = "#000";
        for (let i = 0; i <= width; i++) {
            ctx.fillRect(i * squarePx, 0, 1, this.hpx);
        }
        for (let i = 0; i <= height; i++) {
            ctx.fillRect(0, i * squarePx, this.hpx, 1);
        }
    };
    CanvasOperate.prototype.black = function (x, y) {
        this.blacks.push(x, y);
    };
    CanvasOperate.prototype.white = function (x, y) {
        this.whites.push(x, y);
    };
    CanvasOperate.prototype.done = function () {
        const w = this.whites;
        const b = this.blacks;
        const ctx = this.ctx;
        ctx.beginPath();
        for (let i = 0; i < w.length; i += 2) {
            ctx.rect(w[i] * squarePx + 1, w[i+1] * squarePx + 1, squarePx - 1, squarePx - 1);
        }
        ctx.fillStyle = "#fff";
        ctx.fill();
        ctx.beginPath();
        for (let i = 0; i < b.length; i += 2) {
            ctx.rect(b[i] * squarePx + 1, b[i+1] * squarePx + 1, squarePx - 1, squarePx - 1);
        }
        ctx.fillStyle = "#555";
        ctx.fill();
        w.length = b.length = 0;
    }
    CanvasOperate.prototype.draw = function (x, y, flag) {
        flag ? this.white(x, y) : this.black(x, y);
    }
    CanvasOperate.prototype.processClick = function (gr, x, y) {
        // if (x % squarePx === 0 || y % squarePx === 0) {
            // return;
        // }
        const nx = Math.floor(x / squarePx);
        const ny = Math.floor(y / squarePx);
        gr.invert(nx, ny);
        this.done();
        gr.mark[ny * width + nx] = 1;
    };
    function Grid(co) {
        this.rows = this.genRows();
        this.key = this.genRows();
        // key: 相邻八格内白色块数
        this.mark = this.genRows();
        // mark: 是否可以 update
        this.co = co;
    }
    Grid.prototype.genRows = function () {
        return new Int8Array(width * height);
    };
    Grid.prototype.clear = function () {
        const rows = this.rows;
        const co = this.co;
        this.key.fill(0);
        for (let y = 0; y < height; y++) {
            const left = width * y;
            for (let x = 0; x < width; x++) {
                if (rows[left + x]) {
                    co.black(x, y);
                }
            }
        }
        co.done();
        rows.fill(0);
    };
    Grid.prototype.update = function () {
        const start = performance.now();
        const co = this.co;
        const key = new Int8Array(this.key);
        const mark = this.mark;
        this.mark = this.genRows();
        const rows = this.rows;
        for (let y = 0; y < height; y++) {
            const left = width * y;
            for (let x = 0; x < width; x++) {
                if (!mark[left + x]) continue;
                const num = key[left + x];
                if (rows[left + x]) {
                    if (num !== 2 && num !== 3) {
                        co.black(x, y);
                        rows[left + x] = 0;
                        this.keyDec(x, y);
                        this.markAround(x, y)
                    }
                }
                else if (num === 3) {
                    rows[left + x] = 1;
                    co.white(x, y);
                    this.keyInc(x, y);
                    this.markAround(x, y);
                }
            }
        }
        co.done();
        time.textContent = (performance.now() - start).toFixed(2);
        // alert(key.map(v=>v.join('')).join('\n'))
    };
    Grid.prototype.keyInc = function (x, y) {
        const k = this.key;
        const left = y * width;
        if (x !== 0) {
            k[left + x-1]++;
            if (y !== 0) k[left - width + x-1]++;
            if (y !== height - 1) k[left + width + x-1]++;
        }
        if (x !== width - 1) {
            k[left + x+1]++;
            if (y !== height - 1) k[left + width + x+1]++;
            if (y !== 0) k[left - width + x+1]++;
        }
        if (y !== 0) {
            k[left - width + x]++;
        }
        if (y !== height - 1) {
            k[left + width + x]++;
        }
    };
    Grid.prototype.keyDec = function (x, y) {
        const k = this.key;
        const left = y * width;
        if (x !== 0) {
            k[left + x-1]--;
            if (y !== 0) k[left - width + x-1]--;
            if (y !== height - 1) k[left + width + x-1]--;
        }
        if (x !== width - 1) {
            k[left + x+1]--;
            if (y !== height - 1) k[left + width + x+1]--;
            if (y !== 0) k[left - width + x+1]--;
        }
        if (y !== 0) {
            k[left - width + x]--;
        }
        if (y !== height - 1) {
            k[left + width + x]--;
        }
    };
    Grid.prototype.markAround = function (x, y) {
        const k = this.mark;
        const left = y * width;
        if (x !== 0) {
            k[left + x-1] = 1;
            if (y !== 0) k[left - width + x-1] = 1;
            if (y !== height - 1) k[left + width + x-1] = 1;
        }
        if (x !== width - 1) {
            k[left + x+1] = 1;
            if (y !== height - 1) k[left + width + x+1] = 1;
            if (y !== 0) k[left - width + x+1] = 1;
        }
        if (y !== 0) {
            k[left - width + x] = 1;
        }
        if (y !== height - 1) {
            k[left + width + x] = 1;
        }
    };
    Grid.prototype.invert = function (x, y) {
        this.co.draw(x, y, this.rows[y * width + x] ^= 1);
        this.markAround(x, y);
        if (this.rows[y * width + x]) {
            this.keyInc(x, y);
        }
        else {
            this.keyDec(x, y);
        }
    };
    Grid.prototype.random = function (num) {
        const start = performance.now();
        const key = this.key;
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                if (Math.random() < num) {
                    this.invert(x, y);
                }
            }
        }
        this.co.done();
        time.textContent = (performance.now() - start).toFixed(2);
    }
    const co = new CanvasOperate();
    const gr = new Grid(co);
    let intervalRunning = false;
    let interval = null;
    document.getElementById("update").addEventListener("click", () => {
        if (intervalRunning) return;
        gr.update();
    });
    document.getElementById("updaten").addEventListener("click", () => {
        if (intervalRunning) return;
        const str = prompt("重复的次数（0.05秒1次）", "1000");
        if (str === null) return;
        let num = +str;
        if (!Number.isInteger(num) || num <= 0) {
            alert("数据不合法");
            return;
        }
        intervalRunning = true;
        interval = setInterval(() => {
            if (num === 0 || !intervalRunning) {
                clearInterval(interval);
                interval = null;
                intervalRunning = false;
            }
            num--;
            gr.update();
        }, 50);
    });
    document.getElementById("pause").addEventListener("click", () => {
        if (intervalRunning) {
            intervalRunning = false;
            clearInterval(interval);
            interval = null;
        }
    });
    document.getElementById("clear").addEventListener("click", () => {
        if (intervalRunning) {
            intervalRunning = false;
            clearInterval(interval);
            interval = null;
        }
        gr.clear();
    });
    document.getElementById("random").addEventListener("click", () => {
        const str = prompt("白色方块的密度（大概）", "0.4");
        if (str === null) return;
        const num = +str;
        if (num <= 0 || num >= 1) {
            alert("数据不合法");
            return;
        }
        gr.random(num);
    });
    document.getElementById("picture").addEventListener("click", () => {
        const img = new Image();
        img.src = co.el.toDataURL("image/png");
        co.el.parentElement.appendChild(img);
    });
    co.el.addEventListener("click", event => {
        const x = event.offsetX;
        const y = event.offsetY;
        co.processClick(gr, x, y);
    });
})();
