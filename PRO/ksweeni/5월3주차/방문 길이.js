function solution(dirs) {
    const move = { U: [0, 1], D: [0, -1], R: [1, 0], L: [-1, 0] };
    let now = [0,0]
    const roadset = new Set();
    
    for (const d of dirs) {
        const X = now[0] + move[d][0];
        const Y = now[1] + move[d][1];
        
        if(X >5 || Y > 5 || X <-5 || Y < -5) continue;
        roadset.add(`${now[0]}${now[1]}${X}${Y}`);
        roadset.add(`${X}${Y}${now[0]}${now[1]}`);
        now = [X, Y];
    }
    return roadset.size/2;
}