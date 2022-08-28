import Timer from "./Timer";
import Palindrome from "./Palindrome";

const num = "196";

Timer.create()
    .do(() => {
        Palindrome.create(num, 10000).compute().print();
    })
    .end();
