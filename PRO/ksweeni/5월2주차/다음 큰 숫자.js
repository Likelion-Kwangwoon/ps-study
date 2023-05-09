function solution(n) {
    const one = n.toString(2).split("1").length;
    while(true){
        n++;
        if(n.toString(2).split("1").length===one){
            return n;
        }
    }
}