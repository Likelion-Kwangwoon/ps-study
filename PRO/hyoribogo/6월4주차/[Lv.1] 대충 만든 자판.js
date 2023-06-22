function solution(keymap, targets) {
  const keyCnt = new Map();
  keymap.forEach((key) => {
    [...key].forEach((item, index) => {
      keyCnt.set(item, keyCnt.has(item) ? Math.min(keyCnt.get(item), index + 1) : index + 1)
    })
  })

  const answer = targets
    .map(target => {
      target = [...target].reduce((cnt, key) => cnt + keyCnt.get(key), 0)
      return target ? target : -1
    })

  return answer
}