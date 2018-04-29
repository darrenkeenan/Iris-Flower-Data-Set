# Calculating min & max petal length per species of iris data set
# Darren Keenan - finalized 2018-04-29

columnname = "Petal Length", "Species/Class"                    # naming two columns
print(columnname)                                               # printing named columns

with open("data/iris.csv") as iris:                             # opening file iris.csv saved on computer
    for cmandname in iris:
        i = cmandname.split(",")                                # aligning data
        print(i[0],i[4])                                        # listing column 1 in file, petal length & column 5, spcies/class of iris

listset = (5.1,4.9,4.7,4.6,5,5.4,4.6,5,4.4,4.9,5.4,4.8,4.8,4.3,5.8,5.7,5.4,5.1,5.7,5.1,5.4,5.1,4.6,5.1,4.8,5,5,5.2,5.2,4.7,4.8,5.4,5.2,5.5,4.9,5,5.5,4.9,4.4,5.1,5,4.5,4.4,5,5.1,4.8,5.1,4.6,5.3,5)
print("Min Iris-Setosa Petal Length is:", min(listset))         # printing minimum value of listset
# Min Iris-Setosa Petal Length is: 4.3

listset = (5.1,4.9,4.7,4.6,5,5.4,4.6,5,4.4,4.9,5.4,4.8,4.8,4.3,5.8,5.7,5.4,5.1,5.7,5.1,5.4,5.1,4.6,5.1,4.8,5,5,5.2,5.2,4.7,4.8,5.4,5.2,5.5,4.9,5,5.5,4.9,4.4,5.1,5,4.5,4.4,5,5.1,4.8,5.1,4.6,5.3,5)
print("Max Iris-Setosa Petal Length is:", max(listset))         # printing maximum value of listset
# Max Iris-Setosa Petal Length is: 5.8

listset = (7,6.4,6.9,5.5,6.5,5.7,6.3,4.9,6.6,5.2,5,5.9,6,6.1,5.6,6.7,5.6,5.8,6.2,5.6,5.9,6.1,6.3,6.1,6.4,6.6,6.8,6.7,6,5.7,5.5,5.5,5.8,6,5.4,6,6.7,6.3,5.6,5.5,5.5,6.1,5.8,5,5.6,5.7,5.7,6.2,5.1,5.7)
print("Min Iris-Versicolor Petal Length is:", min(listset))     # printing minimum value of listset
# Min Iris-Versicolor Petal Length is: 4.9

listset = (7,6.4,6.9,5.5,6.5,5.7,6.3,4.9,6.6,5.2,5,5.9,6,6.1,5.6,6.7,5.6,5.8,6.2,5.6,5.9,6.1,6.3,6.1,6.4,6.6,6.8,6.7,6,5.7,5.5,5.5,5.8,6,5.4,6,6.7,6.3,5.6,5.5,5.5,6.1,5.8,5,5.6,5.7,5.7,6.2,5.1,5.7)
print("Max Iris-Versicolor Petal Length is:", max(listset))     # printing maximum value of listset
# Max Iris-Versicolor Petal Length is: 7

listset = (6.3,5.8,7.1,6.3,6.5,7.6,4.9,7.3,6.7,7.2,6.5,6.4,6.8,5.7,5.8,6.4,6.5,7.7,7.7,6,6.9,5.6,7.7,6.3,6.7,7.2,6.2,6.1,6.4,7.2,7.4,7.9,6.4,6.3,6.1,7.7,6.3,6.4,6,6.9,6.7,6.9,5.8,6.8,6.7,6.7,6.3,6.5,6.2,5.9)
print("Min Iris-Virginica Petal Length is:", min(listset))      # printing minimum value of listset
# Min Iris-Virginica Petal Length is: 4.9

listset = (6.3,5.8,7.1,6.3,6.5,7.6,4.9,7.3,6.7,7.2,6.5,6.4,6.8,5.7,5.8,6.4,6.5,7.7,7.7,6,6.9,5.6,7.7,6.3,6.7,7.2,6.2,6.1,6.4,7.2,7.4,7.9,6.4,6.3,6.1,7.7,6.3,6.4,6,6.9,6.7,6.9,5.8,6.8,6.7,6.7,6.3,6.5,6.2,5.9)
print("Max Iris-Virginica Petal Length is:", max(listset))      # printing maximum value of listset
# Max Iris-Virginica Petal Length is: 7.9
