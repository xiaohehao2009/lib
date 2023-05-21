// this javascript file has been tested on Nodejs v19.6.1

const float2view = num => {
    /*num = +num;*/
    const view = new DataView(new ArrayBuffer(8));
    view.setFloat64(0, num);
    return view;
};
const view2float = view => {
    /*if (!(view instanceof DataView)) {
        throw new TypeError('view is not a dataview.');
    }
    if (view.byteLength < 8) {
        throw new RangeError('view is smaller than 8 bytes.');
    }*/
    return view.getFloat64(0);
};
const view2bits = view => {
    /*if (!(view instanceof DataView)) {
        throw new TypeError('view is not a dataview.');
    }*/
    return Array.from(new Uint8Array(view.buffer))
        .map(num => num.toString(2)
        .padStart(8, '0'))
        .join('');
};
const bits2floatbin = bits => {
    /*if (typeof bits !== 'string') {
        throw new TypeError('bits is not a string.');
    }
    if (bits.length !== 64) {
        throw new RangeError('bits is not a 64-byte string.');
    }
    if (!bits.every(bit => bit === '0' || bit === '1')) {
        throw new TypeError('bits is not a string only including 0 and 1.');
    }*/
    return [bits[0], bits.slice(1, 12), bits.slice(12)].join(' ');
};
const bits2view = bits => {
    /*if (typeof bits !== 'string') {
        throw new TypeError('bits is not a string.');
    }
    if (!bits.every(bit => bit === '0' || bit === '1')) {
        throw new TypeError('bits is not a string only including 0 and 1.');
    }*/
    bits = bits.replaceAll(' ', '');
    const length = Math.floor(bits.length / 8);
    const buffer = new ArrayBuffer(length);
    const arr = new Uint8Array(buffer);
    for (let i = 0; i < length;) {
        arr[i] = Number.parseInt(bits.slice(i * 8, (++i) * 8), 2);
    }
    return new DataView(buffer);
};
const tuple2floatbin = (sign, exp, frac) => {
    /*if (!Number.isInteger(exp)) {
        throw new TypeError('exp is not a integer.');
    }
    if (exp < 0 || exp > 2047) {
        throw new RangeError('exp is less than 0 or greater than 2047.');
    }
    if (typeof frac !== 'string') {
        throw new TypeError('frac is not a number or a string.');
    }*/
    return [
        +!!sign,
        exp.toString(2).padStart(11, '0'),
        frac.padEnd(52, '0')
    ].join(' ');
};
const floatbin2tuple = bits => {
    /*if (typeof bits !== 'string') {
        throw new TypeError('bits is not a string.');
    }
    if (bits.length !== 64) {
        throw new RangeError('bits is not a 64-byte string.');
    }
    if (!bits.every(bit => bit === '0' || bit === '1')) {
        throw new TypeError('bits is not a string only including 0 and 1.');
    }*/
    bits = bits.replaceAll(' ', '').padEnd(64, '0');
    return [+bits[0], Number.parseInt(bits.slice(1, 12), 2), bits.slice(12).replace(/0+$/, '')];
};
const float2floatbin = num => {
    return view2bits(float2view(num));
};
const floatbin2float = bits => {
    return view2float(bits2view(bits));
};

// the following codes are for test

// 1. test float2floatbin able to work and speed
/*const start = -80, count = 100000, step = 3.34542734948671e+33;
console.log('start calc (float to floatbin), args:');
console.log({start, count, step});
console.time('time');
for (let i = 0; i < count; i++) {
    float2floatbin(start + step * i);
}
console.timeEnd('time'); // about 600 ~ 700 ms*/

// 2. test floatbin2float and tuple2floatbin able to work
/*const pairs = [
    [tuple2floatbin(0, 1023, '0'), 1],
    [tuple2floatbin(1, 1024, '1'), -3],
    [tuple2floatbin(0, 1025, '01'), 5],
    [tuple2floatbin(0, 1028, '10101'), 0b110101]
];
console.log('start calc (floatbin to float), pairs:');
console.log(pairs);
for (const [bin, val] of pairs) {
    if (floatbin2float(bin) !== val) {
        console.log(bin, val);
        throw new Error('floatbin2float or tuple2floatbin ' +
            'gives out the wrong result.');
    }
}
console.log('no error'); // no error*/

// 3. test floatbin2float speed
/*const count = 100000, pos = 15, max = 2 ** pos;
const bin = tuple2floatbin(0, 1468, '11111101010001')
    .replaceAll(' ', '')
    .slice(0, 64 - pos);
console.log('start calc (floatbin to float), args:');
console.log({count, pos, max, bin});
console.time('time');
for (let i = 0; i < count; i++) {
    floatbin2float(bin +
        Math.floor(Math.random() * max).toString(2).padStart(pos, '0'));
}
console.timeEnd('time'); // about 450 ms*/
