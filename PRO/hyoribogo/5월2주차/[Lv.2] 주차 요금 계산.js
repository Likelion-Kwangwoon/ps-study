function solution(fees, records) {
  const accRecord = new Map()
  const answer = new Map()
  
  for(const record of records) {
      const [time, carNum] = record.split(" ")
      if(accRecord.has(carNum)) {
          let [h1, m1] = accRecord.get(carNum).split(":")
          let [h2, m2] = time.split(":");
          [h1, m1, h2, m2] = [+h1, +m1, +h2, +m2]
          if(m2 < m1) {
              m2 += 60
              h2--
          }
          answer.set(carNum, (answer.get(carNum) || 0) + (h2 - h1) * 60 + m2 - m1)
          accRecord.delete(carNum)
      }
      else
          accRecord.set(carNum, time)
  }
  
  // 출차 처리 안된 차 검사
  if(accRecord.size)
      accRecord.forEach((time, carNum) => {
          const [h, m] = time.split(":")
          answer.set(carNum, (answer.get(carNum) || 0) + (23 - +h) * 60 + 59 - +m)
      })
  
  // 총 주차요금 계산
  answer.forEach((time, carNum) => {
      if(time <= fees[0])
          answer.set(carNum, fees[1])
      else
          answer.set(carNum, fees[1] + Math.ceil((time - fees[0])/fees[2]) * fees[3])
  })
  
  return [...answer].sort((a, b) => a[0] - b[0]).map(i => i[1])
}
