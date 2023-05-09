function solution(common) {
    let one = common[1]-common[0];
    let two = common [2] - common[1];
    if(one === two) return (common[common.length-1] + one);
    else return common[common.length-1]*(two/one);
}