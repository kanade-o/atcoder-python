s1 = input()
s2 = input()
s3 = input()

contests = ['ABC', 'ARC', 'AGC', 'AHC']
def match_delete(s):
  if s in contests:
    contests.remove(s)

match_delete(s1)
match_delete(s2)
match_delete(s3)

print("".join(contests))