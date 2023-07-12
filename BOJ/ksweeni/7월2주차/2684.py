for _ in range(int(input())):
    dic = {"TTT": 0, "TTH": 0, "THT": 0, "THH": 0, "HTT": 0, "HTH": 0, "HHT": 0, "HHH": 0}
    s = input()
    for i in range(38):
        dic[s[i:i+3]] += 1
    for k, v in dic.items():
        print(v, end=' ')
