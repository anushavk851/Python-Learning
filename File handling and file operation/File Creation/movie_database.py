# Fields
# MovieID,Title,Language,Year,Rating,Collection
# Questions
#1 Print all Tamil movies.
#2 Print movies released in 2023.
#3 Print movies with rating above 8.5.
#4 Print movies whose collection exceeds 500 crores.
#5 Count movies by language.
#6 Count movies by year.
#7 Count movies by rating group:
    # Below 8
    # 8–8.5
    # Above 8.5
#8 Count movies by collection group:
    # Below 500
    # 500–1000
    # Above 1000
#9 Find the highest-grossing movie.
#10 Find the lowest-grossing movie.
#11 Find the average rating.
#12 Find the average collection.
#13 Find the language with the maximum number of movies.
#14 Print movie titles with ratings between 8.0 and 8.5.
#15 Find the movie with the best rating.

with open(r"C:\Users\ACCURATE\Desktop\movies.txt","r") as f:
    data=f.readline()
    movies=[]
    while data:
        MovieID,Title,Language,Year,Rating,Collection=data.strip().split(",")
        movies.append([int(MovieID),Title,Language,int(Year),float(Rating),int(Collection)])
        data=f.readline()
#1
    print()
    for m in movies:
        if m[2]=="Tamil":
            print(m)
#2
    print()
    for m in movies:
        if m[3]==2023:
            print(m[1])
#3
    print()
    for m in movies:
        if m[4]>8.5:
            print(m[1],m[4])
#4
    print()
    for m in movies:
        if m[5]>500:
            print(m)
#5
    print()
    lang={}
    for m in movies:
        if m[2] in lang:
            lang[m[2]]+=1
        else:
            lang[m[2]]=1
    print(lang)
#6
    print()
    year={}
    for m in movies:
        if m[3] in year:
            year[m[3]]+=1
        else:
            year[m[3]]=1
    print(year)
#7
    print()
    rating_gp={
        "Below 8":0,
        "8-8.5":0,
        "above 8.5":0}
    for m in movies:
        if m[4]<8:
            rating_gp["Below 8"]+=1
        elif m[4]>8.5:
            rating_gp["above 8.5"]+=1
        else:
            rating_gp["8-8.5"]+=1
    print(rating_gp)
#8
    print()
    collect_gp={
        "Below 500":0,
        "500-1000":0,
        "Above 1000":0
    }
    for m in movies:
        if m[5]<500:
            collect_gp["Below 500"]+=1
        elif m[5]>1000:
            collect_gp["Above 1000"]+=1
        else:
            collect_gp["500-1000"]+=1
    print(collect_gp)
#9
    print()
    highest=movies[0][5]
    for m in movies:
        if m[5]>highest:
            highest=m[5]
    for m in movies:
        if m[5]==highest:
            print(m)
#10
    print()
    lowest=movies[0][5]
    for m in movies:
        if m[5]<lowest:
            lowest=m[5]
    for m in movies:
        if m[5]==lowest:
            print(m)
#11
    print()
    total_rating=0
    count=0
    for m in movies:
        total_rating=total_rating+m[4]
        count=count+1
    print("average rating is: ",total_rating/count)
#12
    print()
    total_coll=0
    count=0
    for m in movies:
        total_coll+=m[5]
        count+=1
    print("average collection of movies is: ",total_coll/count)
#13
    print()
    language={}
    for m in movies:
        if m[2] in language:
            language[m[2]]+=1
        else:
            language[m[2]]=1
    max_lan=""
    max_count=0
    for m in language:
        if language[m]>max_count:
            max_count= language[m]
            max_lan=m
    print("language with maximum number of movies: ",max_lan)
    print("total number: ",max_count)
#14
    print()
    for m in movies:
        if 8<m[4]<8.5:
            print(m[1])
#15
    print()
    highest=movies[0][4]
    for m in movies:
        if m[4]>highest:
            highest=m[4]
    for m in movies:
        if m[4]==highest:
            print(m[1])
