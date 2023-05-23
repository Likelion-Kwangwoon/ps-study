function solution(land) {
    var answer = [[...land[0]]];
    const len = land.length;
    
    for(let i = 1; i < len; i++){
        answer.push([0, 0, 0, 0]);
        
        for(let j = 0; j < 4; j++){
            for(let k = 0; k < 4; k++){
                if(j !== k){
                    answer[i][j] = answer[i][j] < land[i][j] + answer[i - 1][k] ? land[i][j] + answer[i - 1][k] : answer[i][j];
                }
            }
        }
    }

    return Math.max(...answer[len - 1]);
}