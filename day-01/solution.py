def filter_gifts(gifts):
  
  finalGifts = []
  
  for i in range(0,len(gifts),1):
      if "#" not in gifts[i]:
          finalGifts.append(gifts[i])
  
  return finalGifts

gifts1 = ["car", "doll#arm", "ball", "#train"]
good1 = filter_gifts(gifts1)
print(good1)
