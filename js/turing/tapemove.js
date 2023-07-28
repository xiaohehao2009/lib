class TapeMove {
    static R = tape => tape.R();
    static L = tape => tape.L();
    static S = () => null;

    static get(pattern) {
        switch (pattern) {
            case 'R': case 'r':
                return TapeMove.R;
            case 'L': case 'l':
                return TapeMove.L;
            case 'S': case 's':
                return TapeMove.S;
            default:
                throw new Error('Invalid tapemove: ' + pattern);
        }
    }
}

export default TapeMove;
