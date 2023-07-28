function solution(gems){
  var germVariety = new Set(gems).size; 
  var gemMap = new Map();
  var list = []; 
    
  gems.forEach((gem, i)=> {
    gemMap.delete(gem)
    gemMap.set(gem, i)
    if(gemMap.size === germVariety){
      list.push([gemMap.values().next().value + 1, i+1])
    }
  })
  
  list.sort((a,b)=> {
    if(a[1]-a[0] === b[1]-b[0]){
      return a[1]-b[1];}
    return (a[1]-a[0])-(b[1]-b[0]);
  })
  return list[0]
}
