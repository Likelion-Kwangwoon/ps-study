function solution(msg) {
    var answer = [];
    var dic =[];
    for (let i = 65; i < 91; i++) { // 사전 초기화
        dic.push(String.fromCharCode(i));
    }
    while(msg.length !== 0) {
      
        for ( var i = 0; i< msg.length; i ++) {
            var w = msg.slice(0, i);
            var wc = msg.slice(0, i+1);
            if (dic.indexOf(wc) === -1){ 
                answer.push(dic.indexOf(w)+1); 
                break;
            }
            if (i === msg.length -1 ){ 
                answer.push(dic.indexOf(wc)+1); 
            }
        }
      
        dic.push(wc); 
        msg = msg.slice(i); 
    }
    return answer;
}