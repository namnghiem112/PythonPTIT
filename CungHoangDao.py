t=int(input())
while(t):
  t-=1
  date,month=[int(x) for x in input().split()]
  if(date>=21 and date<=31 and month==3) or (date>=1 and date<=19 and month==4): print("Bach Duong")
  elif (date>=20 and date<=30 and month==4) or (date>=1 and date<=20 and month==5): print("Kim Nguu")
  elif (date>=21 and date<=31 and month==5) or (date>=1 and date<=20 and month==6): print("Song Tu") 
  elif (date>=21 and date<=30 and month==6) or (date>=1 and date<=22 and month==7): print("Cu Giai")    
  elif (date>=23 and date<=31 and month==7) or (date>=1 and date<=22 and month==8): print("Su Tu")
  elif (date>=23 and date<=31 and month==8) or (date>=1 and date<=22 and month==9): print("Xu Nu")
  elif (date>=23 and date<=30 and month==9) or (date>=1 and date<=22 and month==10): print("Thien Binh")
  elif (date>=23 and date<=31 and month==10) or (date>=1 and date<=22 and month==11): print("Thien Yet")
  elif (date>=23 and date<=30 and month==11) or (date>=1 and date<=21 and month==12): print("Nhan Ma")
  elif (date>=22 and date<=31 and month==12) or (date>=1 and date<=19 and month==1): print("Ma Ket")
  elif (date>=20 and date<=31 and month==1) or (date>=1 and date<=18 and month==2): print("Bao Binh")
  else: print("Song Ngu")  