try{(() => {
    const width = 200;
    const height = 200;
    const squarePx = 10;
    function CanvasOperate() {
        this.el = document.createElement("canvas");
        this.wpx = width * squarePx + 1;
        this.hpx = height * squarePx + 1;
        this.el.width = this.wpx;
        this.el.height = this.hpx;
        this.ctx = this.el.getContext("2d");
        this.initGrid();
        this.ctx.fillStyle = "#fff";
        document.getElementById("app").appendChild(this.el);
    }
    CanvasOperate.prototype.initGrid = function () {
        const ctx = this.ctx;
        ctx.fillStyle = "#000";
        for (let i = 0; i <= width; i++) {
            ctx.fillRect(i * squarePx, 0, 1, this.hpx);
        }
        for (let i = 0; i <= height; i++) {
            ctx.fillRect(0, i * squarePx, this.hpx, 1);
        }
    };
    CanvasOperate.prototype.black = function (x, y) {
        this.ctx.clearRect(x * squarePx + 1, y * squarePx + 1, squarePx - 1, squarePx - 1);
    };
    CanvasOperate.prototype.white = function (x, y) {
        this.ctx.fillRect(x * squarePx + 1, y * squarePx + 1, squarePx - 1, squarePx - 1);
    };
    CanvasOperate.prototype.processClick = function (gr, x, y) {
        // if (x % squarePx === 0 || y % squarePx === 0) {
            // return;
        // }
        const nx = Math.floor(x / squarePx);
        const ny = Math.floor(y / squarePx);
        const flag = gr.rows[ny][nx] ^= 1;
        flag ? this.white(nx, ny) : this.black(nx, ny);
    };
    function Grid(co) {
        this.rows = this.genRows();
        this.lastRows = this.rows;
        this.co = co;
    }
    Grid.prototype.get = function (x, y) {
        if (y === -1 || y === height || x === -1 || x === width) return 0;
        return this.rows[y][x];
    }
    Grid.prototype.genRows = function () {
        const rows = Array(height);
        for (let i = 0; i < height; i++) {
            rows[i] = new Int8Array(width);
        }
        return rows;
    };
    Grid.prototype.clear = function () {
        this.lastRows = this.rows;
        this.rows = this.genRows();
        // for (let y = 0; y < height; y++) {
            // for (let x = 0; x < width; x++) {
                // this.rows[y][x] = 0;
            // }
        // }
    };
    Grid.prototype.update = function () {
        const newRows = this.genRows();
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                let num = ones([this.get(x-1,y-1),this.get(x-1,y),this.get(x-1,y+1),this.get(x,y-1),this.get(x,y+1),this.get(x+1,y-1),this.get(x+1,y),this.get(x+1,y+1)]);
                if (this.rows[y][x]) {
                    if (num === 2 || num === 3) {
                        newRows[y][x] = 1;
                    }
                }
                else {
                    if (num === 3) {
                        newRows[y][x] = 1;
                    }
                }
            }
        }
        this.lastRows = this.rows;
        this.rows = newRows;
    };
    Grid.prototype.random = function (num) {
        this.lastRows = this.rows;
        this.rows = this.genRows();
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                this.rows[y][x] = Math.random() < num;
            }
        }
    }
    Grid.prototype.render = function () {
        for (let y = 0; y < height; y++) {
            for (let x = 0; x < width; x++) {
                if (this.rows[y][x] === this.lastRows[y][x]) continue;
                this.rows[y][x] ? this.co.white(x, y) : this.co.black(x, y);
            }
        }
    };
    function ones(arr) {
        let num = 0;
        for (let i = 0; i < arr.length; i++) {
            if (arr[i]) num++;
        }
        return num;
    }
    const co = new CanvasOperate();
    const gr = new Grid(co);
    let intervalRunning = false;
    let interval = null;
    gr.render();
    document.getElementById("update").addEventListener("click", () => {
        if (intervalRunning) return;
        gr.update();
        gr.render();
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
            gr.render();
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
        gr.render();
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
        gr.render();
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
}catch(ex){alert(ex)}