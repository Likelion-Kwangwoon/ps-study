function solution(msg) {
  const dict = [..."_ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
  const result = []

  while (msg.length) {
    let w = ''
    let idx = msg.length

    for (; idx > 0; idx--) {
      w = msg.slice(0, idx)

      if (dict.includes(w)) {
        result.push(dict.indexOf(w))
        break
      }
    }
    dict.push(w + msg[idx])
    msg = msg.slice(w.length)
  }

  return result
}