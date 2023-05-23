function solution(skill, skill_trees) {
  let result = 0
  const regex = new RegExp(`[${skill}]`, 'g')
  
  for(const skill_tree of skill_trees) {
      if(!skill_tree.match(regex) || skill.indexOf(skill_tree.match(regex).join("")) === 0)
          result++
  }
  
  return result
}