const solution = (n, lost, reserve) => {
  const students = new Array(n).fill(1)
  lost.forEach(i => students[i - 1]--)
  reserve.forEach(i => students[i - 1]++)
  
  for (let i = 0; i < students.length; i++) {
      if(!students[i] && students[i - 1] === 2) {
          students[i]++
      }
      if(!students[i] && students[i + 1] === 2) {
          students[i + 1]--
          students[i]++
      }
  }
  
  return students.filter(i => i).length
}