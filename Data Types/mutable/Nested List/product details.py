#3. Product Details
 # [Product ID, Name, Category, Price, Stock]
 #Problems:
  #1. Print products costing above ₹1000.
  #2. Print products with stock less than 10.
  #3. Print electronic products details.
  #4. Find the most expensive product.
  #5. Find the cheapest product.
  #6. Find the total stock.
  #7. Print products whose names start with "S".
  #8. Count products in the "Electronics" category.
  #9. Print products name with price between ₹500 and ₹2000.
  #10. Find the total value of inventory (Price × Stock).
product=[[1,"phone","electronic",35000,15],[2,"watch","electronic",1200,9],
         [3,"table","furniture",5999,6],[4,"sofa","furniture",12000,11],
         [5,"shower","steel",350,20],[6,"soap","cosmetics",100,25],
         [7,"lipstick","cosmetics",350,17],[8,"sunscreen","cosmetics",501,15],
         [9,"kettle","electronic",1000,10],[10,"pipe","steel",200,5]]
#1
for item in product:
    if item[3]>1000:
        print(item[1])
print()#2
for item in product:
    if item[4]<10:
        print(item[1])
print()#3
for item in product:
    if item[2]=="electronic":
        print(item[:])
print()#4
expensive=product[0][3]
for item in product:
    if item[3]>expensive:
        expensive=item[3]
for item in product:
    if item[3]==expensive:
        print("the expensive product detail: ",item)
print()#5
cheapest=product[0][3]
for item in product:
    if item[3]<cheapest:
        cheapest=item[3]
for item in product:
    if item[3]==cheapest:
        print("the cheapest product detail: ",item)
print()#6
total=0
for item in product:
     total=total+item[4]
print("Total stock of all product is: ",total)
print()#7
for item in product:
    if item[1].startswith("s"):
        print(item)
print()#8
count=0
for item in product:
    if item[2]=="electronic":
        count=count+1
print("count of electronic product: ",count)
print()#9
for item in product:
    if 500<item[3]<2000:
        print(item[1])
print()#10
inventory=0
for item in product:
      inventory=inventory+(item[3]*item[4])
print("total inventory is: ",inventory)
