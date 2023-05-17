function solution(number, limit, power) {
    const num = [];
    var answer=0
    
    for (let cur = 1; cur <= number; cur++) {
        let count =0;
        for (let i = 1; i <= cur / 2; i++) {
            if (cur % i === 0) {
                count += 1;
            }
        }
        num.push(count + 1);
    }
    num.forEach(n => {
        answer += ( n > limit) ? power : n;
    })
   return answer;
}