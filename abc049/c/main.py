s = input()
# 後ろから見ていくと被りがなくなる. 前から見たら被っている(=prefix)
# 全部反転させる
# スライスを使って反転. while Trueで文字の長さ分iを進める. フラグを2段階使う
divide = ["dream", "dreamer", "erase", "eraser"]
s = s[::-1]
divide = [d[::-1] for d in divide]

i = 0
can = True

while i < len(s):
  can2 = False
  for d in divide:
    if s[i:i+len(d)] == d:
      can2 = True
      i += len(d)
      break
    
  if not can2:
    can = False
    break
    
if can:
  print("YES")
else:
  print("NO")