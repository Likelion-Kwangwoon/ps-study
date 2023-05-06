function solution(k, m, score) {
    // m은 사과의 수
    // k는 최대점수
    // 반환값은 최소점수 곱하기 사과개수
    score = score.sort().reverse();
    let s=[];
    for (let i = 0; i < score.length; i+=m) {
        s.push(score.slice(i, i+m))
  }
    s = s.filter((a) => a.length === m);
    s = s.map(a => Math.min(...a)*m).reduce((a,b) => a+b, 0)
    return s;
}