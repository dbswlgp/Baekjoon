N,K = map(int,input().split())

start = 1
end = 9
count = 0
while True:
  length = len(str(start))
  if N >= end:
    if count + (end-start+1)*length < K:
      count += (end-start+1)*length
      start = end+1
      end = int(str(end)+'9')
    else:
      quotient = (K - count) // length
      count += (quotient * length)
      if count == K:
        print(str(start+quotient-1)[-1])
      else:
        print(str(start+quotient)[K-count-1])
      break
  else:
    if count + ((N-start+1) * length) < K:
      print(-1)
      break
    else:
      quotient = (K - count) // length
      count += (quotient * length)
      if count == K:
        print(str(start+quotient-1)[-1])
      else:
        print(str(start+quotient)[K-count-1])
      break

