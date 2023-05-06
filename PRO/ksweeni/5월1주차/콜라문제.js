function solution(a, b, n) {
    // 전체 = 받은 병 + 남은 병 
    // 받은 병 = 전체/a * b
    // 남은 병 = 전체%a
    var answer = 0;
    while(n >= a){
       answer = answer + Math.floor(n/a)*b;
       n = Math.floor(n/a)*b + Math.floor(n%a);
    }
    return answer;
}