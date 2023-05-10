function solution(s) {
    let zero =0;
    let count =0;
    while(s.length!==1){
        const origin = s.length;
        s=s.split('').filter(n=>n==='1').join('');
        const len = s.length;
        zero += origin-len;
        s = len.toString(2);
        count++;
    }
    return[count,zero]
}