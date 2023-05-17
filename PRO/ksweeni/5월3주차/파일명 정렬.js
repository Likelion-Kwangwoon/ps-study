function solution(files) {
    const pattern = /(\D+)(\d{1,5})/;
    return files.sort((a,b)=>{
        let [HA, numa] = a.match(pattern).slice(1, 3);
        let [HB, numb] = b.match(pattern).slice(1, 3);
        HA = HA.toLowerCase();
        HB = HB.toLowerCase();
        if (HA === HB && numa === numb) return 0;
		if (HA === HB) return numa - numb;
		if (HA > HB) return 1;
		else return -1;
    })
}