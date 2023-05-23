function solution(n, s) {
    
    let start = Math.trunc(s/n);
    if (start === 0) return [-1]
    let res = s % n
    var answer = new Array(n).fill(start);
    // 재 분배
    for (let i=0;i<res;i++){
        answer[answer.length -1-i ]++
    }
    return answer;
}