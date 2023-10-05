'use strict';

const vm = code => {
    const call = [code['main']];
    const loc = [[]];
    const arg = [[]];
    const ev = [];
    let i = 2, j = 0;
    const showStack = () =>
    console.log(
        call.map(
            v => Object.entries(code).find(([v0, v1])=>v1===v)[0]
        ).join('\n↓')
    );
    const funs = {
        [LOG]: () => console.log(ev.pop()),
        [UPTIME]: () => ev.push(process.uptime()),
        [TOSTR]: () => ev.push(String(ev.pop())),
        [CONCAT]: () => {//ev.push(((a,b)=>b+a)(ev.pop(),ev.pop()))
            const a = ev.pop();
            ev.push(String(ev.pop())+a);
        }
    };
    const br = () => {
        const l=call[j][i+1];
        i=call[j].findIndex((v,k)=>v===LABEL&&call[j][k+1]===l)+2;
        if (i===1) {
            console.log(`No such label: ${l}`);
            return true;
        }
    }
    while (true) {
        if (i >= call[j].length) {
            console.log('Function not returned');
            showStack();
            return;
        }
        // console.log({loc, arg, ev});
        // console.log([i,ev]);
        if (call[j][i] === CALL) {
            if (typeof call[j][i]==='number')
            funs[call[j][i+1]](),i+=2;
            else
            call[j].push(i+2),call[j+1]=code[call[j][i+1]],j++,
            arg[j]=ev.splice(ev.length-call[j][0],call[j][0]),
            loc[j]=[],i=2;
        }
        else if (call[j][i] === RET) {
            if (j===0)return;
            call[j]=arg[j]=loc[j]=null,i=call[--j].pop();
        }
        else if (call[j][i] === LDSTR) {
            ev.push(String(call[j][i+1])),i+=2;
        }
        else if (call[j][i] === LDC) {
            ev.push(Number(call[j][i+1])),i+=2;
        }
        else if (call[j][i] === NEWARR) {
            ev.push(Array.from({length:ev.pop()})),i++;
        }
        else if (call[j][i] === LDLOC) {
            if (call[j][i+1]>=call[j][1]) {
                console.log(`ldloc id out of range: ${call[j][i+1]}`);
                return;
            }
            ev.push(loc[j][call[j][i+1]]),i+=2;
        }
        else if (call[j][i] === LDARG) {
            if (call[j][i+1]>=call[j][0]) {
                console.log(`ldarg id out of range: ${call[j][i+1]}`);
                return;
            }
            ev.push(arg[j][call[j][i+1]]),i+=2;
        }
        else if (call[j][i] === STLOC) {
            if (call[j][i+1]>=call[j][1]) {
                console.log(`stloc id out of range: ${call[j][i+1]}`);
                return;
            }
            loc[j][call[j][i+1]]=ev.pop(),i+=2;
        }
        else if (call[j][i] === STARG) {
            if (call[j][i+1]>=call[j][0]) {
                console.log(`starg id out of range: ${call[j][i+1]}`);
                return;
            }
            arg[j][call[j][i+1]]=ev.pop(),i+=2;
        }
        else if (call[j][i] === LDELEM) {
            const a=ev.pop();
            ev.push(ev.pop()[a]),i++;
        }
        else if (call[j][i] === STELEM) {
            const a=ev.pop(),b=ev.pop();
            ev.pop()[b]=a,i++;
        }
        else if (call[j][i] === ADD) {
            const a=ev.pop();
            ev.push(ev.pop()+a),i++;
        }
        else if (call[j][i] === SUB) {
            const a=ev.pop();
            ev.push(ev.pop()-a),i++;
        }
        else if (call[j][i] === MUL) {
            const a=ev.pop();
            ev.push(ev.pop()*a),i++;
        }
        else if (call[j][i] === DIV) {
            const a=ev.pop();
            ev.push(ev.pop()/a),i++;
        }
        else if (call[j][i] === POW) {
            const a=ev.pop();
            ev.push(ev.pop()**a),i++;
        }
        else if (call[j][i] === REM) {
            const a=ev.pop();
            ev.push(ev.pop()%a),i++;
        }
        else if (call[j][i] === AND) {
            const a=ev.pop();
            ev.push(ev.pop()&a),i++;
        }
        else if (call[j][i] === OR) {
            const a=ev.pop();
            ev.push(ev.pop()|a),i++;
        }
        else if (call[j][i] === XOR) {
            const a=ev.pop();
            ev.push(ev.pop()^a),i++;
        }
        else if (call[j][i] === TAILCALL) {
            call[j]=code[call[j][i + 1]],
            arg[j]=ev.splice(ev.length-call[j][0],call[j][0]),
            loc[j].length=0,i=2;
        }
        else if (call[j][i] === LABEL) i+=2;
        else if (call[j][i] === BR) {
            if (br()) return;
        }
        else if (call[j][i] === BRTRUE) {
            if (ev.pop()) {if (br())return;}
            else i+=2;
        }
        else if (call[j][i] === BRFALSE) {
            if (!ev.pop()) {if(br())return;}
            else i+=2;
        }
        else if (call[j][i] === BEQ) {
            const a = ev.pop();
            if (ev.pop() === a) {if(br())return;}
            else i+=2;
        }
        else if (call[j][i] === BNE) {
            const a = ev.pop();
            if (ev.pop() !== a) {if(br())return;}
            else i+=2;
        }
        else if (call[j][i] === BGT) {
            const a = ev.pop();
            if (ev.pop() > a) {if(br())return;}
            else i+=2;
        }
        else if (call[j][i] === BLT) {
            const a = ev.pop();
            if (ev.pop() < a) {if(br())return;}
            else i+=2;
        }
        else if (call[j][i] === BGE) {
            const a = ev.pop();
            if (ev.pop() >= a) {if(br())return;}
            else i+=2;
        }
        else if (call[j][i] === BLE) {
            const a = ev.pop();
            if (ev.pop() <= a) {if(br())return;}
            else i+=2;
        }
        else if (call[j][i]===CEQ) {
            const a=ev.pop();
            ev.push(ev.pop() === a),i++;
        }
        else if (call[j][i]===CNE) {
            const a=ev.pop();
            ev.push(ev.pop() !== a),i++;
        }
        else if (call[j][i]===CGT) {
            const a=ev.pop();
            ev.push(ev.pop() > a),i++;
        }
        else if (call[j][i]===CLT) {
            const a=ev.pop();
            ev.push(ev.pop() < a),i++;
        }
        else if (call[j][i]===CGE) {
            const a=ev.pop();
            ev.push(ev.pop() >= a),i++;
        }
        else if (call[j][i]===CLE) {
            const a=ev.pop();
            ev.push(ev.pop() <= a),i++;
        }
        else if (call[j][i]===DUP)
        {
            ev.push(ev[ev.length-1]),i++;
        }
        else if (call[j][i]===LDGLOBAL)
        {
            ev.push(globalThis),i++;
        }
        else if (call[j][i]===LDPROP)
        {
            const a = ev.pop();
            ev.push(ev.pop()[a]),i++;
        }
        else if (call[j][i]===NEWOBJ)
        {
            ev.push({}),i++;
        }
        else if (call[j][i]===STPROP)
        {
            const a = ev.pop(), b = ev.pop();
            ev.pop()[b]=a,i++;
        }
        else if (call[j][i]===CALLVIRT)
        {
            const a=ev.splice(ev.length-call[j][i+1],call[j][i+1]);
            ev.push(ev.pop().apply(null,a)),
            i+=2;
        }
        else if (call[j][i]===CALLINST)
        {
            const a=ev.splice(ev.length-call[j][i+1],call[j][i+1]);
            const b=ev.pop();
            ev.push(ev.pop().apply(b,a)),
            i+=2;
        }
        else if (call[j][i] === POP) ev.pop();
        else if (call[j][i] === NOP) i++;
        else
        console.log(`Unknown opcode at ${i}: ${call[j][i++]}`);
    }
};
    // a => (g => g(g))
    // ((
        // (b, c, d, e, f) =>
        // g =>
        // f >= b[0].length ? console.log('NO RETURN') :
        // b[0][f]===RET?(b.length===1?/*console.log({b,c,d,e,f})*/0:(b.shift(),d.shift(),e.shift(),f=b[0].shift(),g(g))):
        // b[0][f]===CALL?(f++,b[0][f]===LOG?console.log((f++,c.shift())):b[0][f]===UPTIME?c.unshift((f++,process.uptime())):b[0][f]===TOSTR?(c[0]=c[0].toString(),f++):b[0][f]===CONCAT?(c[0]=c[1]+c.shift(),f++):(b.unshift(a[b[0][f]]),e.unshift(c.splice(0,b[0][0]).reverse()),b[1].unshift(f+1),f=1),g(g)):
        // b[0][f]===LDC||b[0][f]===LDSTR?(c.unshift(b[0][f+1]),f+=2,g(g)):
        // b[0][f]===NEWARR?(c.unshift([]),f++,g(g)):
        // b[0][f]===LDARG?(c.unshift(e[0][b[0][f+1]]),f+=2,g(g)):
        // b[0][f]===LDLOC?(c.unshift(d[0][b[0][f+1]]),f+=2,g(g)):
        // b[0][f]===STARG?(e[0][b[0][f+1]]=c.shift(),f+=2,g(g)):
        // b[0][f]===STLOC?(d[0][b[0][f+1]]=c.shift(),f+=2,g(g)):
        // b[0][f]===STELEM?(c[2][c[1]]=c.shift(),c.shift(),c.shift(),f++,g(g)):
        // b[0][f]===LDELEM?(c[0]=c[1][c.shift()],f++,g(g)):
        // b[0][f]===ADD?(c[0]=c[1]+c.shift(),f++,g(g)):
        // b[0][f]===SUB?(c[0]=c[1]-c.shift(),f++,g(g)):
        // b[0][f]===MUL?(c[0]=c[1]*c.shift(),f++,g(g)):
        // b[0][f]===DIV?(c[0]=c[1]/c.shift(),f++,g(g)):
        // b[0][f]===REM?(c[0]=c[1]%c.shift(),f++,g(g)):
        // b[0][f]===POW?(c[0]=c[1]**c.shift(),f++,g(g)):
        // b[0][f]===NEG?(c[0]=-c[0],f++,g(g)):
        // b[0][f]===NOT?(c[0]=!c[0],f++,g(g)):
        // b[0][f]===BR?(f=b[0][f+1],g(g)):
        // b[0][f]===BRTRUE?(c[0]?(f=b[0][f+1]):f+=2,g(g)):
        // b[0][f]===BRFALSE?(!c[0]?(f=b[0][f+1]):f+=2,g(g)):
        // b[0][f]===TAILCALL?(b[0]=a[b[0][f+1]],d[0].length=0,e[0]=c.splice(0,b[0][0]).reverse(),f=1,g(g)):
        // (console.log(`unknown:${b[0][f]}`),f++,g(g))
    // )([a['main']], [], /*loc*/[[]], /*arg*/[[]], 1));

const RET = 0, CALL = 1, LDC = 2, NEWARR = 3, LDARG = 4, LDLOC = 5,
      STARG = 6, STLOC = 7, LDELEM = 8, STELEM = 9,
      ADD = 10, SUB = 11, MUL = 12, DIV = 13, POW = 14, REM = 15,
      NEG = 16, NOT = 17, TAILCALL = 18, LDSTR = 19, BR = 20,
      BRTRUE = 21, BRFALSE = 22, CGT = 23, CLT = 24, CGE = 25, CLE = 26,
      DUP = 27, CEQ = 28, CNE = 29, AND = 30, OR = 31, XOR = 32, LABEL = 33,
      BEQ = 34, BNE = 35, BGT = 36, BGE = 37, BLT = 38, BLE = 39, POP = 40,
      LDGLOBAL = 41, LDPROP = 42, NEWOBJ = 43, STPROP = 44, NOP = 45,
      CALLVIRT = 46, CALLINST = 47;

const LOG = 0, UPTIME = 1, TOSTR = 2, CONCAT = 3;

/*vm({
    main: [ 0, 4,
        CALL, UPTIME,
        STLOC, 3,
        LDC, 2.5,
        STLOC, 0,
        LDC, 1/6,
        STLOC, 1,
        LDC, 4,
        STLOC, 2,

    LABEL, 'aaa',
        LDLOC, 0,
        LDLOC, 1,
        ADD,
        STLOC, 0,
        LDLOC, 1,
        LDLOC, 2,
        DIV,
        STLOC, 1,
        LDLOC, 2,
        LDC, 1,
        ADD,
        STLOC, 2,
        LDLOC, 2,
        LDC, 66,
    BLT, 'aaa',

        LDSTR, 'Time: ',
        LDGLOBAL,
        LDSTR, 'Number',
        LDPROP,
        LDSTR, 'prototype',
        LDPROP,
        LDSTR, 'toFixed',
        LDPROP,
        CALL, UPTIME,
        LDLOC, 3,
        SUB,
        LDC, 59,
        CALLINST, 1,
        CALL, CONCAT,
        LDSTR, ' ms',
        CALL, CONCAT,
        CALL, LOG,
        LDSTR, 'E = ',
        LDLOC, 0,
        CALL, TOSTR,
        CALL, CONCAT,
        CALL, LOG,
        LDSTR, 'Math.E = ',
        LDGLOBAL,
        LDSTR, 'Math',
        LDPROP,
        LDSTR, 'E',
        LDPROP,
        CALL, TOSTR,
        CALL, CONCAT,
        CALL, LOG,
        RET
    ]
});*/ // calc E === 1/0!+1/1!+1/2!+1/3!+1/4!+...

vm({
    main: [ 0, 3,
        LDC, 0, STLOC, 0, LDC, 0, STLOC, 1,
        LDGLOBAL, LDSTR, 'Math', LDPROP, LDSTR, 'sqrt',
        LDPROP, STLOC, 2,
        LABEL, 0, LDLOC, 0, LDLOC, 2,
        LDC, 1, LDLOC, 1, LDLOC, 1, MUL, SUB,
        CALLVIRT, 1, ADD, STLOC, 0,
        LDLOC, 1, LDC, 1/2**16, ADD, STLOC, 1,
        LDLOC, 1, LDC, 1, BLE, 0, LDSTR, 'PI = ',
        LDLOC, 0, LDC, 4/2**16, MUL,
        CALL, TOSTR, CALL, CONCAT, CALL, LOG,
        LDSTR, 'Math.PI = ',
        LDGLOBAL, LDSTR, 'Math', LDPROP, LDSTR, 'PI',
        LDPROP, CALL, TOSTR, CALL, CONCAT, CALL, LOG,
        RET
    ]
});
