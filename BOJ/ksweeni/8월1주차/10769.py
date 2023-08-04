import sys
input = sys.stdin.readline

msg = input()
if msg.count(':-)') >  msg.count(':-(') :
  print('happy')
elif msg.count(':-)') <  msg.count(':-(') :
  print('sad')
elif msg.count(':-)') == msg.count(':-(') and msg.count(':-)') >= 1:
  print('unsure')
elif msg.count(':-)') == 0 and  msg.count(':-(') == 0 :
  print('none')