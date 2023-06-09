function solution(n) {
    let answer = Array.from({ length: n }, (_, index) => Array(index + 1).fill(0));
    let x = -1;
    let y = 0;
    let count = 0;
   
    while(n>0){
        for(let i =0;i<n;i++){
            answer[++x][y] = ++count;
        }
        for(let i =0;i<n-1;i++){
            answer[x][++y] = ++count;
        }
        for(let i =0;i<n-2;i++){
            answer[--x][--y] = ++count;
        }
        
        n-=3;
}
    return answer.flatMap(v => v);
}