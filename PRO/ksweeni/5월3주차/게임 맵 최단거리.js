function solution(maps) {
    const yLen = maps.length;
    const xLen = maps[0].length;

    const goalY = yLen - 1;
    const goalX = xLen - 1;
    
    const dy = [0, 0, 1, -1];
    const dx = [-1, 1, 0, 0];
    
    const queue = [];
    queue.push([0, 0, 1]);
    
    while(queue.length) {
        const [cur_Y, cur_X, step] = queue.shift();
        if(cur_Y === goalY && cur_X === goalX) return step;
        
        for(let i = 0; i < 4; i++) { // 좌우상하
            const n_y = cur_Y + dy[i];
            const n_x = cur_X + dx[i];
            if(n_y >= 0 && n_y < yLen && n_x >= 0 && n_x < xLen && maps[n_y][n_x] === 1) {
                queue.push([n_y, n_x, step + 1]);
                maps[n_y][n_x] = 0;
            }
        }
    }
    
    return -1;
}