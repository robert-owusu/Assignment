from pandas import *
options.display.width=0
set_option('display.max_rows',3000)
set_option('display.max_columns',3000)


#Importing the Data
cars=read_csv("cars 2.csv")

#Question_3.A_Printing First and Last 5 rows
print(cars.head())
print(cars.tail())

#Question3B_Cleaning_and_Updating_CSV
#Cleaning
#Changing NAN values to 0
cars1=cars.fillna(0)
#print(cars1)

#Identifying Duplicates
cars_duplicate=cars1.duplicated()
#print(cars_duplicate)

#Renaming_Column_Heads
cars2=cars1.rename({'wheel-base':'wheel_base','engine-type':'engine_type','num-of-cylinders':'num_of_cylinders','egine_capacity':'engine_capacity','average-km':'average_km'}, axis=1)
#print(cars2)

#Updating_to_CSV_file
cars2.to_csv("cars 2.csv")

#Question3C_Most_Expensive_Car_Company
print(cars2[['company','price']].max(axis=0))

#Question3D_Kantaka_Cars_Details
print(cars2.loc[cars2.company=='Kantaka', :])

#QUestion3E_Total_Cars_per_Company
print(cars2['company'].value_counts())



#Question_3H_Sorting_by_price
print(cars2.sort_values('price'))

#Question_3H(i)_Concatenating_2_Frames
#Dictionary1
GhanaCars = {
    'Company': ['KANTAKA', 'VW', 'BMV', 'NEOPLAN'],
    'Price': [23845, 171995, 135925 , 71400]
}
GhanaCar = DataFrame(GhanaCars,index=(range(1,5)))

#Dictionary2
JapaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '],
                'Price': [29995, 23600, 61500 , 58900]
}
JapaneseCar = DataFrame(JapaneseCars,index=(range(1,5)))

#Concatenation
print(concat([GhanaCar,JapaneseCar]))
























