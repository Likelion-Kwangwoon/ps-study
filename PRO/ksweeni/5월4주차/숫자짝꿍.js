function solution(X, Y) {
    let answer ='';
    X = X.split('');
    Y = Y.split('');
    for(let i=0;i<10;i++){
        let xcount = X.filter(x => Number(x) === i).length; 
        let ycount = Y.filter(y => Number(y) === i).length; 
        answer += i.toString().repeat(Math.min(xcount, ycount)); 
    }
    if(!answer) return '-1';
    answer = answer.split('').sort().reverse().join('');
    
    if(answer[0] === '0') return '0';
    else return answer; 
}