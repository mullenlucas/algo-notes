flowerbed = [0,0,1,0,0]

def canPlaceFlowers(flowerbed, n):
  s = 0
  for i in range(len(flowerbed)):
    if flowerbed[i] == 0:
      if i == len(flowerbed)-1 or flowerbed[i+1] == 0:
          if flowerbed[i-1] == 0 or i == 0:
            flowerbed[i] = 1
            s += 1
  
  print(flowerbed,s)
  return s >= n

print(canPlaceFlowers(flowerbed,1))