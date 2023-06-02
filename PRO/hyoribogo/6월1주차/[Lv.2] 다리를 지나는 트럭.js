function solution(bridge_length, weight, truck_weights) {
  let time = 0 , currentWeightSum = 0
  const queue = [[0, 0]]

  while (queue.length > 0 || truck_weights.length > 0) {
    if (queue[0][1] === time)
        currentWeightSum -= queue.shift()[0]

    if (currentWeightSum + truck_weights[0] <= weight) {
      currentWeightSum += truck_weights[0]
      queue.push([truck_weights.shift(), time + bridge_length])
    }
      
    else if (queue[0])
        time = queue[0][1] - 1
      
    time++
  }
    
  return time
}