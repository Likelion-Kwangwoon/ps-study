function solution(record) {
  const nicknameList = new Map()
  const result = []
  
  for(const m of record) {
      const [state, id, nickname] = m.split(" ")
      if(state === "Enter" || state === "Change")
          nicknameList.set(id, nickname)
  }
  
  for(const m of record) {
      const [state, id] = m.split(" ")
      
      if(state === "Enter")
          result.push(nicknameList.get(id)+"님이 들어왔습니다.")
      else if(state === "Leave")
          result.push(nicknameList.get(id)+"님이 나갔습니다.")
  }
  
  return result
}