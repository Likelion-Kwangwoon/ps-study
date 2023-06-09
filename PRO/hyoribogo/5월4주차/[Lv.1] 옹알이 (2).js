function solution(babbling) {
    const words = ["aya", "ye", "woo", "ma"]
    let result = 0
    
    for(let b of babbling) {
        for(const word of words) {
            if(b.includes(word + word)) break
            b = b.replaceAll(word, " ")
        }
        
        if(!b.trim())
            result++
    }
    return result
}