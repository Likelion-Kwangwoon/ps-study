function solution(new_id) {
    const res = new_id
      .toLowerCase() 
      .replace(/[^\w-_.]/g, "") 
      .replace(/\.+/g, ".")
      .replace(/^\.|\.$/g, "") 
      .replace(/^$/, "a") 
      .slice(0, 15)
      .replace(/\.$/, ""); 
    const len = res.length;
    return len > 2 ? res : res + res.charAt(len - 1).repeat(3 - len);
  }