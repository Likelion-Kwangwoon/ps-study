import sys
import re
 
s = sys.stdin.readline().strip()

sen = re.sub('pi|ka|chu', '', s)
 
if not sen: print('YES')
else:print('NO')