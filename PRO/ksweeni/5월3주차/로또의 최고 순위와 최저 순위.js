function solution(lottos, win_nums) {
    let zero = lottos.filter(element => 0 === element).length;
    let count = (lottos.filter(x => win_nums.includes(x))).length;
    let min = 7-count >= 6 ? 6 : 7-count;
    let max = min-zero < 1 ? 1 : min-zero;
    return [max, min]
}