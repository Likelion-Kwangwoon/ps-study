function solution(n, s) {
    if(n > s) return [-1]
    const bestSet = []
    
    for(let i = n; i > 0; i--) {
        const bestNum = ~~(s / i)
        bestSet.push(bestNum)
        s -= bestNum
    }
    
    return bestSet.sort((a,b) => a-b)
}