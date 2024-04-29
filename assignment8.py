# # question 1 :-
a = int(input("enter the number :"))
if(a>1):
    print(a*(a+1))
else:
    print("give number bigger than 1.")

# sir! question number 2 try kyaa prr deek se huaa he nahi koee be logicsamaj nahi aa rhaa tha 😭

# question 3 :-
def find(num):
    n1 = num[0]  
    n2 = num[0]  
    for n in num:
        if (n > n1):
            n1 = n  
        elif (n < n2):
            n2 = n
    return n1, n2
num = [1234,34,1234,34,53,3456,456,567,65,78,6,79,68,7890]
n1, n2 = find(num)
print("Maximum number :", n1)
print("Minimum number :", n2)



# question 4 :-
def find(words):
    longest = words[0]
    for w in words:
        if len(w) > len(longest):
            longest = w
    return longest
words = ["asdfghjkrtyu","awesrtrxc67tyubnijk","ffasfsihlivluhnfb","hgfuyfbgbndcbfugv"]
longest = find(words)
print("Longest word :", longest)
