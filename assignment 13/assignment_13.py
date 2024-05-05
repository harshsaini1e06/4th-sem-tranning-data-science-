# question 1 :-

import pandas as pd
df = pd.read_csv("Used_Bikes.csv")
print (df)
c = df[(df['city']=="Jaipur")&(df['bike_name'].nunique())]
print (c)
lowest_price = c['price'].min()
print(lowest_price)


# question 2 :-

c = df[(df['city']=="Jaipur")&(df['bike_name'].nunique())]
c = df[(df['city']=="Delhi")&(df['owner']=="First Owner")]
print (c)
lowest_age = c['age'].min()
print (lowest_age)
highest_age = c['age'].max()
print (highest_age)





# question 3 :-




# d = pd.read_excel("HR_Employee_Data.xlsx") 

#[[[[# this is throwing error(d = pd.read_excel("HR_Employee_Data.xlsx")
#         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Program Files\Python311\Lib\site-packages\pandas\io\excel\_base.py", line 495, in read_excel  
#     io = ExcelFile(
#          ^^^^^^^^^^
#   File "C:\Program Files\Python311\Lib\site-packages\pandas\io\excel\_base.py", line 1567, in __init__   
#     self._reader = self._engines[engine](
#                    ^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Program Files\Python311\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 552, in __init__
#     import_optional_dependency("openpyxl")
#   File "C:\Program Files\Python311\Lib\site-packages\pandas\compat\_optional.py", line 138, in import_optional_dependency
#     raise ImportError(msg)
# ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.)]]]]
