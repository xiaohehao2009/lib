const tokenize = str => [...str, ' '].reduce((o, c, i, a) =>
    !o.s ? /\d/.test(c) ? { s: 1, r: o.r, b: c } :
        /\s/.test(c) ? o : c === '*' && a[i + 1] === '*' ?
            { s: 2, r: [...o.r, '**'], b: '' } :
            { s: 0, r: [...o.r, c], b: '' } :
    o.s === 1 ? /\d/.test(c) ? { s: 1, r: o.r, b: o.b + c } :
        /\s/.test(c) ? { s: 0, r: [...o.r, +o.b], b: '' } :
            c === '*' && a[i + 1] === '*' ?
                { s: 2, r: [...o.r, +o.b, '**'], b: '' } :
                { s: 0, r: [...o.r, +o.b, c], b: '' } :
    { s: 0, r: o.r, b: '' }, { s: 0, r: [], b: '' }).r;
const calc = (arr, cf) => (({s, o, q}) => (
    s.findLast(d =>
        (o.push(cf.b.get(d)[2](...[o.pop(), o.pop()].reverse())), false)),
    q ? [o[0], q] : o[0])
)(arr.reduce(({ e, s, o, t, q }, c, i, a) =>
    !e ? cf.u.has(c) ? { e, s, o, t: [...t, c] } :
        (c === '(' ? ([c, q] = calc(arr.slice(i + 1), cf), q += i, e = 2) :
        e = 1,
        { e, s, o: [...o, t[0] ? t.reduceRight((n, m) =>
            cf.u.get(m)(n), c) : c], t: [], q}) :
    e === 2 ? i <= q ? { e: 2, s, o, t: [], q } : { e: 1, s, o, t: [] } :
    e === 3 ? { e, s, o, t, q } :
    c === ')' ? { e: 3, s, o, t: [], q: i } :
    !s[0] ? { e: 0, s: [c], o, t: [] } : (
        s.findLast(d => cf.b.get(d)[0] > cf.b.get(c)[0] ? true :
            cf.b.get(d)[0] < cf.b.get(c)[0] || cf.b.get(c)[1] === cf.l ?
               (o.push(cf.b.get(s.pop())[2](
                   ...[o.pop(), o.pop()].reverse())), false) :
               true), s.push(c), { e: 0, s, o, t: [] }),
    { e: 0, s: [], o: [], t: [] }));

const tokens = tokenize('1+2-3+4*5/6+7+8+9+10**(11+12-13-14/15)+16+(17+18+19+20+21+22+23+24+25+26+(27+28+29+(30+31+32+33+34+35+(36+37+38))))');
console.log(tokens);
const cf = {
    l: 0,
    u: new Map([['-', a => -a]]),
    b: new Map([['*', [0, 0, (a, b) => a * b]], ['+', [1, 0, (a, b) => a + b]], ['/', [0, 0, (a, b) => a / b]], ['-', [1, 0, (a, b) => a - b]], ['**', [-1, 1, (a, b) => a ** b]], ['%', [0, 0, (a, b) => a % b]]])
};
console.log(calc(tokens, cf));
// result: 1165915049.5131643
// real: 1165915049.5131643
