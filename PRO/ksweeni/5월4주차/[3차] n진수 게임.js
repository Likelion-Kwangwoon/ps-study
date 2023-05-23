function solution(n, t, m, p) {
    //진법 n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 
    var answer = '';
    var num = '';
    let len = t*m;
    for(let i=0;i<len;i++){
        num+=i.toString(n)
    }
    let str = num.substring(0,len)
    for(let i = p-1;i<str.length;i+=m){
        answer += str[i].toUpperCase()
    }
    return answer;
}