import CompileResult from './compile-result.js';

function zip(arrs) {
    const length = Math.min(...arrs.map(arr => arr.length));
    const results = [];
    for (let i = 0; i < length; i++) {
        results.push(arrs.map(arr => arr[i]));
    }
    return results;
}

function product(arrs) {
    let results = [[]];
    for (const arr of arrs) {
        const x = [...results];
        results = [];
        for (const i of arr) {
            results.push(...x.map(v => [...v, i]));
        }
    }
    return results;
}

function removeEmpty(arr) {
    return arr.filter(value => value);
}

function getFromIndexes(arr, indexes) {
    const results = Array(indexes.length);
    for (let index = 0; index < indexes.length; index++) {
        results[index] = arr[indexes[index]];
    }
    return results;
}

// function removeInlineComments(source, commentStart) {
    // const NORMAL = 0, COMMENT = 1;
    // let state = NORMAL;
    // const results = [];
    // const stopMatchIndex = source.length - commentStart.length;
    // for (let index = 0; index < source.length; index++) {
        // const char = source[index];
        // if (state === COMMENT) {
            // if (char === '\n' || char === '\r') {
                // results.push(char);
                // state = NORMAL;
            // }
            // continue;
        // }
        // if (index > stopMatchIndex || char !== commentStart[0]) {
            // results.push(char);
            // continue;
        // }
        // let matched = 1;
        // for ( ; ; ) {
            // const ptr = index + matched;
            // if (matched === commentStart.length) {
                // index = ptr - 1;
                // state = COMMENT;
                // break;
            // }
            // if (source[ptr] === commentStart[matched]) {
                // matched++;
            // } else break;
        // }
    // }
    // return results;
// }

function isWhiteSpace(char) {
    return /\s/.test(char);
}

function sourceToLines(source) {
    const lines = [[]];
    for (let index = 0; index < source.length; index++) {
        const char = source[index];
        switch (char) {
            case '\r':
                lines[0].push('\r');
                lines.unshift([]);
                continue;
            case '\n':
                if (index && source[index - 1] === '\r') {
                    lines[1].push('\n');
                } else {
                    lines[0].push('\n');
                    lines.unshift([]);
                }
                continue;
            default: lines[0].push(char);
        }
    }
    return lines.reverse();
}

function getCharPosition(lines, index) {
    for (let line = 0; line < lines.length; line++) {
        const length = lines[line].length;
        if (index < length) return [line, index];
        index -= length;
    }
    throw new Error(`Invalid char at ${index}`);
}

function removeEndLinebreak(line) {
    if (line.endsWith('\n')) {
        return line.slice(0, line.at(-2) === '\r' ? -2 : -1);
    }
    if (line.endsWith('\r')) {
        return line.slice(0, -1);
    }
    return line;
}

function isValidIDChar(char) {
    return !('()[]{}@:;\'\"'.includes(char) || isWhiteSpace(char));
}

function isLinebreak(char) {
    return char === '\n' || char === '\r';
}

function error(lines, msg, start, end) {
    const [linePos, colPos] = getCharPosition(lines, end);
    const line = lines[linePos].join('');
    const startPos = Math.max(0, colPos + start - end);
    console.log(removeEndLinebreak(line));
    console.log(' '.repeat(startPos).padEnd(colPos + 1, '^'));
    throw new SyntaxError(msg);
}

function tokenize(source) {
    const START = 'start',
        COMMENT = 'comment',
        IDENTIFIER = 'identifier',
        LIST1 = '[list]',
        LIST2 = '{list}',
        USE1 = 'use\'',
        USE2 = 'use\"',
        DATATYPE = 'datatype',
        DATAVALUESHORT = 'datavalue_short',
        DATAVALUELONG = 'datavalue_long',
        BLOCKCOMMENT = 'block_comment';
    const tokens = [];
    let token = { start: 0, value: '' };
    let state = START;
    const lines = sourceToLines(source);
    function send() {
        token.end = index;
        tokens.push(token);
        token = { start: index + 1, value: '' };
        state = START;
    }
    const err = (msg, start, end) => {
        if (msg == null) msg = 'Invalid or unexpected token';
        if (start == null) start = token.start;
        if (end == null) end = index;
        error(lines, msg, start, end);
    };
    let index = 0;
    for (; index < source.length; index++) {
        const char = source[index];
        switch (state) {
            case START:
                if (isWhiteSpace(char)) {
                    token.start++;
                    continue;
                }
                switch (char) {
                    case '[':
                        state = LIST1;
                        token.value = [''];
                        token.type = 'ListType1';
                        continue;
                    case '{':
                        state = LIST2;
                        token.value = [''];
                        token.type = 'ListType2';
                        continue;
                    case '\'':
                        index += 4;
                        if (source.slice(index - 3, index + 1)
                            .join('') !== 'use ') {
                            index = Math.min(index, source.length);
                            err('Invalid command');
                        }
                        state = USE1;
                        token.type = 'UseType1';
                        continue;
                    case '\"':
                        index += 4;
                        if (source.slice(index - 3, index + 1)
                            .join('') !== 'use ') {
                            index = Math.min(index, source.length);
                            err('Invalid command');
                        }
                        state = USE2;
                        token.type = 'UseType2';
                        continue;
                    case ';':
                        if (index + 1 !== source.length &&
                            source[index + 1] === '#') {
                            index++;
                            state = BLOCKCOMMENT;
                        } else state = COMMENT;
                        token.type = 'Comment';
                        continue;
                    case ':':
                        token.value = '';
                        state = DATATYPE;
                        token.type = 'DataType';
                        continue;
                    default:
                        if (!isValidIDChar(char)) err();
                        state = IDENTIFIER;
                        token.type = 'Identifier';
                        token.value += char;
                }
                continue;
            case COMMENT:
                if (char === '\r') {
                    index--;
                    send();
                    if (source[index + 1] === '\n') index += 2;
                    else index++;
                    continue;
                }
                if (char === '\n') {
                    index--;
                    send();
                    index++;
                    continue;
                }
                token.value += char;
                continue;
            case BLOCKCOMMENT:
                if (source.length - index >= 3 && char === '#' &&
                    source.slice(index + 1, index + 3).join('') === '##') {
                    index += 3;
                    send();
                    continue;
                }
                token.value += char;
                continue;
            case IDENTIFIER:
                if (!isValidIDChar(char)) {
                    index--;
                    send();
                    continue;
                }
                token.value += char;
                continue;
            case LIST1:
                if (char === ']') {
                    if (token.value[0].length) token.value.reverse();
                    else {
                        token.value.reverse();
                        token.value.pop();
                    }
                    if (!token.value.length) {
                        err('Empty identifier list');
                    }
                    send();
                    continue;
                }
                if (isWhiteSpace(char)) {
                    if (token.value[0].length) {
                        token.value.unshift('');
                    }
                    continue;
                }
                if (!isValidIDChar(char)) {
                    err(null, index - token.value[0].length);
                }
                token.value[0] += char;
                continue;
            case LIST2:
                if (char === '}') {
                    if (token.value[0].length) token.value.reverse();
                    else {
                        token.value.reverse();
                        token.value.pop();
                    }
                    if (!token.value.length) {
                        err('Empty identifier list');
                    }
                    send();
                    continue;
                }
                if (isWhiteSpace(char)) {
                    if (token.value[0].length) {
                        token.value.unshift('');
                    }
                    continue;
                }
                if (!isValidIDChar(char)) {
                    err(null, index - token.value[0].length);
                }
                token.value[0] += char;
                continue;
            case USE1:
                if (char === '\'') {
                    if (!token.value.length) {
                        err('Invalid command');
                    }
                    send();
                    continue;
                }
                if (!isValidIDChar(char)) {
                    if (token.value) {
                        err('Invalid command');
                    }
                    continue;
                }
                token.value += char;
                continue;
            case USE2:
                if (char === '\"') {
                    if (!token.value.length) {
                        err('Invalid command');
                    }
                    send();
                    continue;
                }
                if (!isValidIDChar(char)) {
                    if (token.value) {
                        err('Invalid command');
                    }
                    continue;
                }
                token.value += char;
                continue;
            case DATATYPE:
                if (isLinebreak(char) && token.value.length <= 1) {
                    index--;
                    err();
                }
                if (isWhiteSpace(char)) {
                    if (token.value.length > 1) {
                        const _state = token.value[0] === '@' ?
                            DATAVALUESHORT : DATAVALUELONG;
                        token.value = token.value.slice(1);
                        send();
                        state = _state;
                        token.value = [''];
                        token.type = 'DataValue';
                    } else token.start++;
                    continue;
                }
                if (char === '@' || char === ':') {
                    token.value = char;
                    continue;
                }
                if (!isValidIDChar(char)) err('Invalid statement');
                if (token.value.length) {
                    token.value += char;
                } else {
                    index--;
                    token.value = 'tapeData';
                    send();
                    state = DATAVALUESHORT;
                    token.value = [''];
                    token.type = 'DataValue';
                }
                continue;
            case DATAVALUESHORT:
                if (char === '\n' || char === '\r') {
                    if (token.value.length) {
                        if (!token.value[0].length) {
                            token.value.reverse();
                            token.value.pop();
                        } else token.value.reverse();
                        index--;
                        send();
                        continue;
                    }
                    err('Invalid statement');
                }
                if (isWhiteSpace(char)) {
                    if (token.value[0].length) {
                        token.value.unshift('');
                    }
                    continue;
                }
                if (!isValidIDChar(char)) err('Invalid statement');
                token.value[0] += char;
                continue;
            case DATAVALUELONG:
                if (char === ':') {
                    if (token.value.length) {
                        if (!token.value[0].length) {
                            token.value.reverse();
                            token.value.pop();
                        } else token.value.reverse();
                        send();
                        continue;
                    }
                    err('Invalid statement');
                }
                if (isWhiteSpace(char)) {
                    if (token.value[0].length) {
                        token.value.unshift('');
                    }
                    continue;
                }
                if (!isValidIDChar(char)) err('Invalid statement');
                token.value[0] += char;
                continue;
        }
    }
    if (state === COMMENT || state === IDENTIFIER) {
        send();
    } else if (state === DATAVALUESHORT) {
        token.value = removeEmpty(token.value.reverse());
        send();
    } else if (state !== START) err();
    return tokens;
}

function seqToRules(arr, err) {
    const des = [[], [], []];
    const types = {
        Identifier: 2,
        ListType1: 0,
        ListType2: 1
    };
    const seq = arr.map(token => {
        const type = types[token.type];
        const value = token.value;
        const pos = des[type].length;
        des[type].push(value);
        return { type, value, pos };
    });
    if (des[2].length === 5) return [des[2]];
    if (seq[0].type === 2 && seq[1].type === 2) {
        err(arr[seq.findIndex(({type}) => type !== 2)]);
    }
    if (!(seq[0].type || seq[1].type) && des[1].length) {
        err(arr[seq.findIndex(({type}) => type === 1)]);
    }
    if (!(seq[0].type !== 1 || seq[1].type !== 1) && des[0].length) {
        err(arr[seq.findIndex(({type}) => !type)]);
    }
    const indexes = seq.map(({ type, pos }) => {
        if (!type) return pos;
        pos += des[0].length;
        if (type === 1) return pos;
        return pos + des[1].length;
    });
    let prods = null;
    if (!des[0].length) prods = zip(des[1]);
    else if (!des[1].length) prods = zip(des[0]);
    else prods = product([zip(des[0]), zip(des[1])]).map(arr => arr.flat());
    return prods.map(prod =>
        getFromIndexes([...prod, ...des[2]], indexes));
}

function parse(source, tokens) {
    const ID = 'Identifier',
        COMMENT = 'Comment',
        LIST1 = 'ListType1',
        LIST2 = 'ListType2',
        USE1 = 'UseType1',
        USE2 = 'UseType2',
        DATAHEAD = 'DataType',
        DATABODY = 'DataValue';
    const lines = sourceToLines(source);
    let starting = true;
    const commands = [], statements = {}, rules = [];
    const result = { commands, statements, rules };
    const err = ({start, end}, msg) => {
        console.log(commands, statements, rules);
        if (msg == null) msg = 'Unexpected token';
        error(lines, msg, start, end);
    };
    tokens = tokens.filter(token => token.type !== COMMENT);
    for (let index = 0; index < tokens.length; index++) {
        const token = tokens[index];
        switch (token.type) {
            case COMMENT:
                continue;
            case USE1:
            case USE2:
                if (starting) {
                    commands.push(token.value);
                    continue;
                }
                err(token);
            case DATAHEAD:
                if (!(starting && index + 1 < tokens.length &&
                    tokens[index + 1].type === DATABODY)) err(token);
                if (Object.hasOwn(statements, token.value)) {
                    statements[token.value]
                        .push(...tokens[index + 1].value);
                } else
                statements[token.value] = tokens[index + 1].value;
                index += 1;
                continue;
            case DATABODY: err(token);
            case ID:
            case LIST1:
            case LIST2:
                if (starting) starting = false;
                const seq = [token];
                for (let ptr = index + 1; ptr < index + 5; ptr++) {
                    const curr = tokens[ptr];
                    if (!curr || !(curr.type === ID ||
                        curr.type === LIST1 ||
                        curr.type === LIST2)) {
                        err(curr);
                    }
                    seq.push(curr);
                }
                seqToRules(seq, err).forEach(rule => rules.push(rule));
                index += 4;
                continue;
        }
    }
    return result;
}

function compile(code) {
    const source = [...code];
    const tokens = tokenize(source);
    const res = parse(source, tokens);
    const result = new CompileResult(res);
    return result;
}

// class Compiler {
    // compile(source) {
        // const deleteEmpty = v => v;
        // source = source.replace(
            // /;.*|'use .+'|"use .+"/g, '');
        // const data = removeEmpty(
            // Array.from(source.matchAll(/^\s*:(.*)/mg),
                // v => v.slice(1)).flat().join(' ').split(/\s+/));
        // source = source.replace(/:.*/g, '');
        // const table = removeEmpty(source.split(/\s*\n\s*/));
        // const symbols = new Symbols();
        // const states = new States();
        // symbols.register(data);
        // const result = new CompileResult(symbols, states, data);
        // const set = (st, sy, sy1, mv, st1) => {
            // if (st1 === '$') st1 = st;
            // states.register([st, st1]);
            // symbols.register([sy, sy1]);
            // if (sy === '*') {
                // result.setGeneric(st, mv, sy1, st1);
                // return;
            // }
            // if (sy1 === '$') sy1 = sy;
            // result.set(st, sy, mv, sy1, st1);
        // };
        // for (const line of table) {
            // console.log(line)
            // for (const code of this.parse(line)) {
                // console.log(code)
                // set(...code);
            // }

            // // let code = line.split(/(\[.+?\])/);
            // // code = code.map(str => str.startsWith('[') && str.endsWith(']') ?
                // // [str.slice(1, -1).split(/\s+/).filter(deleteEmpty)] :
                // // str.split(/\s+/).filter(deleteEmpty).map(v => [v])).flat();
            // // if (code.length !== 5
                // // || code[0].length !== code[4].length
                // // || code[1].length !== code[2].length
                // // || code[3].length !== 1) {
                // // throw new SyntaxError('invalid line: ' + line);
            // // }
            // // const mv = TapeMove.get(code[3][0]);
            // // for (let i = 0; i < code[0].length; i++) {
                // // const st = code[0][i], st1 = code[4][i];
                // // for (let j = 0; j < code[1].length; j++) {
                    // // set(st, code[1][j], code[2][j], mv, st1);
                // // }
            // // }

            // // const [state, symbol, newSymbol, tapeMove, newState] = line;
            // // states.register([state, newState]);
            // // const moveFunc = TapeMove.get(tapeMove);
            // // if (symbol === '*') {
                // // if (newSymbol !== '$') {
                    // // symbols.register([newSymbol]);
                // // }
                // // result.setGeneric(state, moveFunc, newSymbol, newState);
                // // continue;
            // // }
            // // if (symbol.startsWith('[') && symbol.endsWith(']')) {
                // // const arr1 = symbols.slice(1, -1)
                    // // .split(',').filter(deleteEmpty);
                // // if (newSymbol.startsWith('[') && newSymbol.endsWith(']')) {
                    // // const arr2 = symbols.slice(1, -1)
                        // // .split(',').filter(deleteEmpty);
                    // // const length = Math.min(arr1.length, arr2.length);
                    // // arr1.length = arr2.length = length;
                    // // for (let i = 0; i < length; i++) {
                        // // table.set()
                    // // }
                // // }
            // // }
            // // symbols.register([symbol, newSymbol]);
            // // this.set(result, symbols, state, symbol, moveFunc, newSymbol, newState);
        // }
        // return result;
    // }
    // // set(result, symbols, ...arr) {
        // // symbols.register([arr[1], arr[3]]);
        // // result.set(...arr);
    // // }
    // parse(line) {
        // const seq = removeEmpty(line.split(/\s*(\[.+?\]|\{.+?\})\s*/))
            // .map(
            // (str, index) => {
                // if (str.startsWith('[') && str.endsWith(']')) {
                    // const arr = removeEmpty(str.slice(1, -1).split(/\s+/));
                    // arr.pattern = 0;
                    // return [arr];
                // }
                // if (str.startsWith('{') && str.endsWith('}')) {
                    // const arr = removeEmpty(str.slice(1, -1).split(/\s+/));
                    // arr.pattern = 1;
                    // return [arr];
                // }
                // return str.split(/\s+/).map(v => {
                    // const arr = [v];
                    // arr.pattern = 2;
                    // return arr;
                // });
            // }).flat();
        // if (seq.length !== 5) {
            // console.log(seq);
            // throw new SyntaxError(`invalid line: ${line}`);
        // }
        // let obj = [[], [], []], arr = [];
        // seq.forEach(v => {
            // arr.push([v.pattern, obj[v.pattern].length]);
            // obj[v.pattern].push(v);
        // });
        // obj[2] = obj[2].map(v => v[0]);
        // if (obj[2].length === 5) {
            // return [obj[2]];
        // }
        // if (arr[0][0] === 2 && arr[1][0] === 2) {
            // throw new SyntaxError(`invalid line: ${line}`);
        // }
        // arr = arr.map(([v, i]) => {
            // for (let j = 0; j < v; j++) i += obj[j].length;
            // return i;
        // });
        // let prod;
        // if (obj[0].length > 0 ^ obj[1].length > 0) {
            // prod = obj[0].length ? zip(obj[0]) : zip(obj[1]);
        // }
        // else prod = product(zip(obj[0]), zip(obj[1]));
        // console.log('obj:', obj);
        // console.log('seq:', seq);
        // console.log('prod:', prod);
        // return prod.map(p => getFromIndexes([...p, ...obj[2]], arr));
    // }
// }

export { tokenize, parse, compile };
export default compile;
