function solution(begin, target, words) {
    var answer = 0; 
    const visited = Array.from({ length: words.length }, () => false); // 방문여부
    let store = [];
    if(!words.includes(target)) return 0;

    store.push([begin, answer]);
    
    while(store.length!=0){
        let [b, depth] = store.shift();
        if(b === target) return depth;
        words.forEach((w => {
            let diff = 0;
            if(visited.includes(w)) return;
            for(let i=0;i<w.length;i++){
                if(b[i] !== w[i]) diff++;
            }
            if(diff === 1)
                {
                    store.push([w, depth+1]);
                    visited.push(w);
                }
        }))
    }
    return answer;
}