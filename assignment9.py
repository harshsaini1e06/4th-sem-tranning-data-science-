# question 1 :-
class Calculate_area:
    r = int (input("enter the radious of circle : "))
    area = (3.14*r*r)
print(Calculate_area.area)


# question 2
class Discount:
    p = int(input("enter the price if the product : "))
    d = int(input("enter the percent of discount to be given on the product : "))
    price = p
    final_price = p - (p*(d/100))
print ("final price is : ",Discount.final_price)


