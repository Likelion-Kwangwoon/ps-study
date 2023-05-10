function solution(common) {
  if(common[1] - common[0] === common[2] - common[1])
      return (2 * common.at(-1)) - common.at(-2)
  return common.at(-1) ** 2 / common.at(-2)
}