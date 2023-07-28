function solution(ingredient) {
    var answer = 0;
    let st = [];
    ingredient.forEach((v) => {
        st.push(v);
        let st_len = st.length;
        if(st[st_len-4] === 1 && st[st_len-3] === 2 && st[st_len-2] === 3 && st[st_len-1] === 1){
            for(let i=0;i<4;i++){
                st.pop()
            }
            answer++
        }
    })
    return answer;
}