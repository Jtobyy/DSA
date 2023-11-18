def solution(S):
  res = ''
  track = {}
  
  start = 9
  for s in S:
      if s not in track:
        track[s] = start
        start -= 1
   
  for s in S:
    res += str(track[s])
    
  print(res)


solution('XYYZZZ')
solution('BABBC')
