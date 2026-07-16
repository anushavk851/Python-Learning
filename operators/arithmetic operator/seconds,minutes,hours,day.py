#convert seconds(34567) into days,hours,minutes and seconds 
  seconds=345678
  day= seconds//(60*60*24)
  remain= seconds%(60*60*24)
  hours= remain//(60*60)
  remain= remain%(60*60)
  minutes= remain//(60)
  remain_second=remain%60
  print("day : hour : minutes : seconds = ",day,":",hours,":",minutes,":",remain_second)
