# Calculating min & max petal width per species of iris data set
# Darren Keenan - finalized 2018-04-29

columnname = "Petal Width", "Species/Class"     # naming two columns
print(columnname)                               # printing named columns

with open("data/iris.csv") as iris:             # opening file iris.csv saved on computer
    for cmandname in iris:                     
        i = cmandname.split(",")                # aligning data
        print(i[1],i[4])                        # listing column 2 in file, petal width & column 5, spcies/class of iris

listset = (3.5,3,3.2,3.1,3.6,3.9,3.4,3.4,2.9,3.1,3.7,3.4,3,3,4,4.4,3.9,3.5,3.8,3.8,3.4,3.7,3.6,3.3,3.4,3,3.4,3.5,3.4,3.2,3.1,3.4,4.1,4.2,3.1,3.2,3.5,3.1,3,3.4,3.5,2.3,3.2,3.5,3.8,3,3.8,3.2,3.7,3.3)
print("Min Iris-Setosa Petal Width is:", min(listset))      # printing minimum value of listset
# Min Iris-Setosa Petal Width is: 2.3

listset = (3.5,3,3.2,3.1,3.6,3.9,3.4,3.4,2.9,3.1,3.7,3.4,3,3,4,4.4,3.9,3.5,3.8,3.8,3.4,3.7,3.6,3.3,3.4,3,3.4,3.5,3.4,3.2,3.1,3.4,4.1,4.2,3.1,3.2,3.5,3.1,3,3.4,3.5,2.3,3.2,3.5,3.8,3,3.8,3.2,3.7,3.3)
print("Max Iris-Setosa Petal Width is:", max(listset))      # printing maximum value of listset
# Max Iris-Setosa Petal Width is: 4.4

listset = (3.2,3.2,3.1,2.3,2.8,2.8,3.3,2.4,2.9,2.7,2,3,2.2,2.9,2.9,3.1,3,2.7,2.2,2.5,3.2,2.8,2.5,2.8,2.9,3,2.8,3,2.9,2.6,2.4,2.4,2.7,2.7,3,3.4,3.1,2.3,3,2.5,2.6,3,2.6,2.3,2.7,3,2.9,2.9,2.5,2.8)
print("Min Iris-Versicolor Petal Width is:", min(listset))  # printing minimum value of listset
# Min Iris-Versicolor Petal Width is: 2

listset = (3.2,3.2,3.1,2.3,2.8,2.8,3.3,2.4,2.9,2.7,2,3,2.2,2.9,2.9,3.1,3,2.7,2.2,2.5,3.2,2.8,2.5,2.8,2.9,3,2.8,3,2.9,2.6,2.4,2.4,2.7,2.7,3,3.4,3.1,2.3,3,2.5,2.6,3,2.6,2.3,2.7,3,2.9,2.9,2.5,2.8)
print("Max Iris-Versicolor Petal Width is:", max(listset))  # printing maximum value of listset
# Max Iris-Versicolor Petal Width is: 3.4

listset = (3.3,2.7,3,2.9,3,3,2.5,2.9,2.5,3.6,3.2,2.7,3,2.5,2.8,3.2,3,3.8,2.6,2.2,3.2,2.8,2.8,2.7,3.3,3.2,2.8,3,2.8,3,2.8,3.8,2.8,2.8,2.6,3,3.4,3.1,3,3.1,3.1,3.1,2.7,3.2,3.3,3,2.5,3,3.4)
print("Min Iris-Virginica Petal Width is:", min(listset))   # printing minimum value of listset
# Min Iris-Virginica Petal Width is: 2.2

listset = (3.3,2.7,3,2.9,3,3,2.5,2.9,2.5,3.6,3.2,2.7,3,2.5,2.8,3.2,3,3.8,2.6,2.2,3.2,2.8,2.8,2.7,3.3,3.2,2.8,3,2.8,3,2.8,3.8,2.8,2.8,2.6,3,3.4,3.1,3,3.1,3.1,3.1,2.7,3.2,3.3,3,2.5,3,3.4)
print("Max Iris-Virginica Petal Width is:", max(listset))   # printing maximum value of listset
# Max Iris-Virginica Petal Width is: 3.8
