#4. Movie Details
 #[Movie ID, Name, Hero, Language, Year, Rating]
 #Problems:
  #1. Print movies released after 2020.
  #2. Print Malayalam movies.
  #3. Print movies with rating above 8.
  #4. Find the highest-rated movie.
  #5. Count Telugu movies.
  #6. Print movie names starring a particular hero.
  #7. Print movies released before 2015.
  #8. Find the average rating.
  #9. Print movies with rating between 7 and 9.
  #10. Print the latest movie details.

movie=[[1,"Drishyam","mohanlal","malayalam",2023,8.6],[2,"3 Idiots","aamir khan","hindi",2009,6.3],
       [3,"sholay","amitabh bachan","hindi",1975,8],[4,"nayakan","kamal haasan","tamil",1987,8],
       [5,"manichitrathazhu","mohanlal","malayalam",1993,9],[6,"baahubali","prabas","telugu",2015,8.7],
       [7,"RRR","ramcharan","telugu",2022,7.6],[8,"CID moosa","dileep","malayalam",2003,8]]
for m in movie:
    if m[4]>2020:
        print(m[1])
print()#2
for m in movie:
    if m[3]=="malayalam":
        print(m[1])
print()#3
for m in movie:
    if m[5]>8:
        print(m[1])
print()#4
top_rate=movie[0][5]
for m in movie:
    if m[5]>top_rate:
        top_rate=m[5]
for m in movie:
    if m[5]==top_rate:
        print("top rated movie is:",m[1])
print()#5
count=0
for m in movie:
    if m[3]=="telugu":
        count=count+1
print("total telugu movies is: ",count)
print()#6
for m in movie:
    if m[2]=="mohanlal":
        print(m[1])
print()#7
for m in movie:
    if m[4]<2015:
        print(m[1])
print()#8
count=0
total=0
for m in movie:
    count=count+1
    total=total+m[5]
print("average movie rating is: ",total/count)
print()#9
for m in movie:
    if 7<m[5]<9:
        print(m[1])
print()#10
latest=movie[0][4]
for m in movie:
    if latest<m[4]:
        latest=m[4]
for m in movie:
    if m[4]==latest:
        print(m[:])
