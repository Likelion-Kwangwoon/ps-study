function solution(num, total) {
    const result = []
    const mid = ~~(total / num)
    const gap = ~~(num / 2)

    if (num % 2) {
        for (let i = mid - gap; i <= mid + gap; i++)
            result.push(i)
        return result
    }
    for (let i = mid - gap + 1; i <= mid + gap; i++)
        result.push(i)
    return result
}



function solution(num, total) {
    var min = Math.ceil(total / num - Math.floor(num / 2));
    var max = Math.floor(total / num + Math.floor(num / 2));

    return new Array(max - min + 1).fill(0).map((el, i) => { return i + min; });
}
