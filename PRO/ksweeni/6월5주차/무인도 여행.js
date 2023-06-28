function solution(maps) {
    var answer = [];
    const mapp = maps.map((n) => n.split(''));
    
    const dx = [1,0,-1,0];
    const dy = [0,1,0,-1];
    
    function dfs(x,y,n){
        let total = Number(n);
        for(let i = 0; i<4; i++){
            const nx = x + dx[i];
            const ny = y + dy[i];
            
            if(nx>=0 && ny>=0 && nx < mapp.length && ny < mapp[0].length){
                if(mapp[nx][ny] !== 'X'){
                    let food = mapp[nx][ny];
                    mapp[nx][ny] = 'X';
                    total += dfs(nx,ny,food);
                }
            }
        }
        return total;
    }
    
    for(let i =0;i<mapp.length;i++){
        for(let j = 0; j < mapp[0].length;j++){
            if(mapp[i][j]!=='X'){
                let begin = mapp[i][j];
                mapp[i][j]='X';
                answer.push(dfs(i,j,begin));
                
            }
        }
    }
  
    return answer.length ? answer.sort((a,b) => a -b) : [-1];
}