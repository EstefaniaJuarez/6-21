#Rx=Q*b
def back_sub(R,b):
  x=b
  m=len(b)
  for i in reversed(range(m)):
    for j in range(len(i+1,m)):
      x+=-(R*x)
  
  x=x/R

  return x

  b=[4,-1,2]
  R=[[1,-2,1],[0,1,6],[0,0,1]]
  print(back_sub(R,b))
