# Fields
  # BookID,Title,Author,Category,Price,Stock
# Questions
#1 Print all Programming books with their title and price.
#2 Print books whose price is above 600.
#3 Print books with stock less than 10.
#4 Print all Data Science books with author names.
#5 Count the number of books in each category.
#6 Count books in each stock group:
    # Below 10
    # 10–15
    # Above 15
#7 Count books in each price group:
    # Below 500
    # 500–700
    # Above 700
#8 Find the book with the highest price.
#9 Find the book with the lowest price.
#10 Find the average price of all books.
#11 Find the average stock of all books.
#12 Print the titles of books whose price is between 400 and 700.
#13 Find the category having the maximum number of books.
#14 Find the total value of all books in stock (Price × Stock).
#15 Print the details of the book with the minimum stock.

with open(r"C:\Users\ACCURATE\Desktop\library.txt","r") as f:
    data=f.readline()
    library=[]
    while data:
        bookid, Title, Author, Category, Price, Stock=data.strip().split(",")
        library.append([int(bookid), Title, Author, Category,int(Price), int(Stock)])
        data=f.readline()
#1
    for book in library:
        if book[3]=="Programming":
            print(book[1],book[3],book[4])
#2  
    print()
    for book in library:
        if book[4]>600:
            print(book[1])
#3
    print()
    for book in library:
        if book[5]<10:
            print(book[1])
#4
    print()
    for book in library:
        if book[3]=="Data Science":
            print(book[1:3])
#5
    print()
    count={}
    for book in library:
        if book[3] in count:
            count[book[3]]+=1
        else:
            count[book[3]]=1
    print("number of book in each category: ",count)
#6
    print()
    stock_count={
        "below 10":0,
        "10-15":0,
        "Above 15":0
    }
    for book in library:
        if book[5]<10:
            stock_count["below 10"]+=1
        elif 10<= book[5]<=15:
            stock_count["10-15"]+=1
        else:
            stock_count["Above 15"]+=1
    print("Stock count: ",stock_count)
#7
    print()
    price_group={
        "below 500":0,
        "500-700":0,
        "above 700":0
    }
    for book in library:
        if book[4]<500:
            price_group["below 500"]+=1
        elif 500<=book[4]<=700:
            price_group["500-700"]+=1
        else:
            price_group["above 700"]+=1
    print(price_group)
#8
    print()
    highest=library[0][4]
    for book in library:
        if book[4]>highest:
            highest=book[4]
    for book in library:
        if highest==book[4]:
            print("book having the highest price is: ",book[1])
#9
    print()
    lowest=library[0][4]
    for book in library:
        if book[4]<lowest:
            lowest=book[4]
    for book in library:
        if lowest==book[4]:
            print("book having the lowest price is: ",book[1])
#10
    print()
    total_price=0
    count=0
    for book in library:
        total_price=total_price+book[4]
        count=count+1
    print("average price of all book is: ",total_price/count)
#11
    print()
    total_stock=0
    count=0
    for book in library:
        total_stock=total_stock+book[5]
        count=count+1
    print("average stock of all books: ",total_stock/count)
#12
    print()
    for book in library:
        if 400<book[4]<700:
            print(book[1])
#13
    print()
    category_count={}
    for book in library:
        if book[3] in category_count:
            category_count[book[3]]+=1
        else:
            category_count[book[3]]=1
    max_cat=""
    max_count=0
    for book in category_count:
        if category_count[book]>max_count:
            max_count=category_count[book]
            max_cat=book
    print("category having maximum number of books: ",max_cat)
    print("number of books: ",max_count)

#14
    print()
    value=0
    for book in library:
        value=value+(book[4]*book[5])
    print("total value of books: ",value)
#15
    print()
    min_stock=library[0][5]
    for book in library:
        if book[5]<min_stock:
            min_stock=book[5]
    for book in library:
        if min_stock==book[5]:
            print("book with minimum stock is: ",book)
