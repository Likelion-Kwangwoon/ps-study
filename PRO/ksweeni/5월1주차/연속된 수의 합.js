function solution(num, total) {
    var answer = [];
    let mid = Math.ceil(total/num);
    let start = mid - Math.trunc(num/2);
    for(let i=0;i<num;i++){
        answer.push(i+start);
    }
    return answer;
}
