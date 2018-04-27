# Iris-Flower-Data-Set
Background research into Fisher's Iris Flower Data Set - A brief summary including python code, tables and graphics supporting my findings. 

Fisher Background:
Sir Ronald Aylmer Fisher (17 February 1890 – 29 July 1962), described as, "a genius who almost single-handedly created the foundations for modern statistical science" (H. Anders, 1998); (A History of Mathematical Statistics. New York: Wiley) and "the single most important figure in 20th century statistics" (E. Bradley, 1998). "R. A. Fisher in the 21st century", Statistical Science. 
As a scholarship recipient, Fisher studied mathematics at the University of Cambridge, graduating in 1912. “Fisher taught high school mathematics and physics from 1914 until 1919 while continuing his research in statistics and genetics. Fisher had evidenced a keen interest in evolutionary theory during his student days” (Sir Ronald Aylmer Fisher | British geneticist and statistician) https://www.britannica.com/biography/Ronald-Aylmer-Fisher 
As a "British statistician and geneticist who pioneered the application of statistical procedures to the design of scientific experiments..." (Sir Ronald Aylmer Fisher | British geneticist and statistician) https://www.britannica.com/biography/Ronald-Aylmer-Fisher. Ronald portrayed an interest in evolutionary theory. “Evolution, theory in biology postulating that the various types of plants, animals, and other living things on Earth have their origin in other preexisting types and that the distinguishable differences are due to modifications in successive generations…” (Evolution | scientific theory) https://www.britannica.com/science/evolution-scientific-theory.  Fisher's love for the evolution of plants, animals and other living things led to the foundation of Analysis of Variance (ANOVA). 
“Analysis of Variance (ANOVA) is a collection of statistical models and their associated procedures (such as "variation" among and between groups) used to analyze the differences among group means” (Wikipedia, Analysis of variance) https://en.wikipedia.org/wiki/Analysis_of_variance 

Iris Data Set:
Statistician and biologist Ronald Fisher introduced the Iris flower data set in the year 1936. The Iris data set, or also known as Fisher’s Iris data set is a multivariate data set, meaning it “…is a subdivision of statistics encompassing the simultaneous observation and analysis of more the one outcome variable” (Wikipedia, Multivariate statistics) https://en.wikipedia.org/wiki/Multivariate_statistics The data set can also be consider as a linear discriminant analysis (LDA). 

The data set consists of 50 samples from each of three species/classes of Iris:
1.	Iris-Setosa
2.	Iris-Versicolor
3.	Iris-Virginica

The four features of the Iris dataset:
1.	Sepal length in cm
2.	Sepal width in cm
3.	Petal length in cm
4.	Petal width in cm


Reviewing the data set:

columnname = "petal length", "petal width", "sepal length", "sepal width", "name" 
print(columnname)

with open("data/iris.csv") as iris:
    for cmandname in iris:
        i = cmandname.split(",")
        print(i[0],i[1],i[2],i[3],i[4])
        
#Results:
5.1 3.5 1.4 0.2 Iris-setosa

4.9 3.0 1.4 0.2 Iris-setosa

4.7 3.2 1.3 0.2 Iris-setosa

4.6 3.1 1.5 0.2 Iris-setosa

5.0 3.6 1.4 0.2 Iris-setosa

5.4 3.9 1.7 0.4 Iris-setosa

4.6 3.4 1.4 0.3 Iris-setosa

5.0 3.4 1.5 0.2 Iris-setosa

4.4 2.9 1.4 0.2 Iris-setosa

4.9 3.1 1.5 0.1 Iris-setosa

5.4 3.7 1.5 0.2 Iris-setosa

4.8 3.4 1.6 0.2 Iris-setosa

4.8 3.0 1.4 0.1 Iris-setosa

4.3 3.0 1.1 0.1 Iris-setosa

5.8 4.0 1.2 0.2 Iris-setosa

5.7 4.4 1.5 0.4 Iris-setosa

5.4 3.9 1.3 0.4 Iris-setosa

5.1 3.5 1.4 0.3 Iris-setosa

5.7 3.8 1.7 0.3 Iris-setosa

5.1 3.8 1.5 0.3 Iris-setosa

5.4 3.4 1.7 0.2 Iris-setosa

5.1 3.7 1.5 0.4 Iris-setosa

4.6 3.6 1.0 0.2 Iris-setosa

5.1 3.3 1.7 0.5 Iris-setosa

4.8 3.4 1.9 0.2 Iris-setosa

5.0 3.0 1.6 0.2 Iris-setosa

5.0 3.4 1.6 0.4 Iris-setosa

5.2 3.5 1.5 0.2 Iris-setosa

5.2 3.4 1.4 0.2 Iris-setosa

4.7 3.2 1.6 0.2 Iris-setosa

4.8 3.1 1.6 0.2 Iris-setosa

5.4 3.4 1.5 0.4 Iris-setosa

5.2 4.1 1.5 0.1 Iris-setosa

5.5 4.2 1.4 0.2 Iris-setosa

4.9 3.1 1.5 0.1 Iris-setosa

5.0 3.2 1.2 0.2 Iris-setosa

5.5 3.5 1.3 0.2 Iris-setosa

4.9 3.1 1.5 0.1 Iris-setosa

4.4 3.0 1.3 0.2 Iris-setosa

5.1 3.4 1.5 0.2 Iris-setosa

5.0 3.5 1.3 0.3 Iris-setosa

4.5 2.3 1.3 0.3 Iris-setosa

4.4 3.2 1.3 0.2 Iris-setosa

5.0 3.5 1.6 0.6 Iris-setosa

5.1 3.8 1.9 0.4 Iris-setosa

4.8 3.0 1.4 0.3 Iris-setosa

5.1 3.8 1.6 0.2 Iris-setosa

4.6 3.2 1.4 0.2 Iris-setosa

5.3 3.7 1.5 0.2 Iris-setosa

5.0 3.3 1.4 0.2 Iris-setosa

7.0 3.2 4.7 1.4 Iris-versicolor

6.4 3.2 4.5 1.5 Iris-versicolor

6.9 3.1 4.9 1.5 Iris-versicolor

5.5 2.3 4.0 1.3 Iris-versicolor

6.5 2.8 4.6 1.5 Iris-versicolor

5.7 2.8 4.5 1.3 Iris-versicolor

6.3 3.3 4.7 1.6 Iris-versicolor

4.9 2.4 3.3 1.0 Iris-versicolor

6.6 2.9 4.6 1.3 Iris-versicolor

5.2 2.7 3.9 1.4 Iris-versicolor

5.0 2.0 3.5 1.0 Iris-versicolor

5.9 3.0 4.2 1.5 Iris-versicolor

6.0 2.2 4.0 1.0 Iris-versicolor

6.1 2.9 4.7 1.4 Iris-versicolor

5.6 2.9 3.6 1.3 Iris-versicolor

6.7 3.1 4.4 1.4 Iris-versicolor

5.6 3.0 4.5 1.5 Iris-versicolor

5.8 2.7 4.1 1.0 Iris-versicolor

6.2 2.2 4.5 1.5 Iris-versicolor

5.6 2.5 3.9 1.1 Iris-versicolor

5.9 3.2 4.8 1.8 Iris-versicolor

6.1 2.8 4.0 1.3 Iris-versicolor

6.3 2.5 4.9 1.5 Iris-versicolor

6.1 2.8 4.7 1.2 Iris-versicolor

6.4 2.9 4.3 1.3 Iris-versicolor

6.6 3.0 4.4 1.4 Iris-versicolor

6.8 2.8 4.8 1.4 Iris-versicolor

6.7 3.0 5.0 1.7 Iris-versicolor

6.0 2.9 4.5 1.5 Iris-versicolor

5.7 2.6 3.5 1.0 Iris-versicolor

5.5 2.4 3.8 1.1 Iris-versicolor

5.5 2.4 3.7 1.0 Iris-versicolor

5.8 2.7 3.9 1.2 Iris-versicolor

6.0 2.7 5.1 1.6 Iris-versicolor

5.4 3.0 4.5 1.5 Iris-versicolor

6.0 3.4 4.5 1.6 Iris-versicolor

6.7 3.1 4.7 1.5 Iris-versicolor

6.3 2.3 4.4 1.3 Iris-versicolor

5.6 3.0 4.1 1.3 Iris-versicolor

5.5 2.5 4.0 1.3 Iris-versicolor

5.5 2.6 4.4 1.2 Iris-versicolor

6.1 3.0 4.6 1.4 Iris-versicolor

5.8 2.6 4.0 1.2 Iris-versicolor

5.0 2.3 3.3 1.0 Iris-versicolor

5.6 2.7 4.2 1.3 Iris-versicolor

5.7 3.0 4.2 1.2 Iris-versicolor

5.7 2.9 4.2 1.3 Iris-versicolor

6.2 2.9 4.3 1.3 Iris-versicolor

5.1 2.5 3.0 1.1 Iris-versicolor

5.7 2.8 4.1 1.3 Iris-versicolor

6.3 3.3 6.0 2.5 Iris-virginica

5.8 2.7 5.1 1.9 Iris-virginica

7.1 3.0 5.9 2.1 Iris-virginica

6.3 2.9 5.6 1.8 Iris-virginica

6.5 3.0 5.8 2.2 Iris-virginica

7.6 3.0 6.6 2.1 Iris-virginica

4.9 2.5 4.5 1.7 Iris-virginica

7.3 2.9 6.3 1.8 Iris-virginica

6.7 2.5 5.8 1.8 Iris-virginica

7.2 3.6 6.1 2.5 Iris-virginica

6.5 3.2 5.1 2.0 Iris-virginica

6.4 2.7 5.3 1.9 Iris-virginica

6.8 3.0 5.5 2.1 Iris-virginica

5.7 2.5 5.0 2.0 Iris-virginica

5.8 2.8 5.1 2.4 Iris-virginica

6.4 3.2 5.3 2.3 Iris-virginica

6.5 3.0 5.5 1.8 Iris-virginica

7.7 3.8 6.7 2.2 Iris-virginica

7.7 2.6 6.9 2.3 Iris-virginica

6.0 2.2 5.0 1.5 Iris-virginica

6.9 3.2 5.7 2.3 Iris-virginica

5.6 2.8 4.9 2.0 Iris-virginica

7.7 2.8 6.7 2.0 Iris-virginica

6.3 2.7 4.9 1.8 Iris-virginica

6.7 3.3 5.7 2.1 Iris-virginica

7.2 3.2 6.0 1.8 Iris-virginica

6.2 2.8 4.8 1.8 Iris-virginica

6.1 3.0 4.9 1.8 Iris-virginica

6.4 2.8 5.6 2.1 Iris-virginica

7.2 3.0 5.8 1.6 Iris-virginica

7.4 2.8 6.1 1.9 Iris-virginica

7.9 3.8 6.4 2.0 Iris-virginica

6.4 2.8 5.6 2.2 Iris-virginica

6.3 2.8 5.1 1.5 Iris-virginica

6.1 2.6 5.6 1.4 Iris-virginica

7.7 3.0 6.1 2.3 Iris-virginica

6.3 3.4 5.6 2.4 Iris-virginica

6.4 3.1 5.5 1.8 Iris-virginica

6.0 3.0 4.8 1.8 Iris-virginica

6.9 3.1 5.4 2.1 Iris-virginica

6.7 3.1 5.6 2.4 Iris-virginica

6.9 3.1 5.1 2.3 Iris-virginica

5.8 2.7 5.1 1.9 Iris-virginica

6.8 3.2 5.9 2.3 Iris-virginica

6.7 3.3 5.7 2.5 Iris-virginica

6.7 3.0 5.2 2.3 Iris-virginica

6.3 2.5 5.0 1.9 Iris-virginica

6.5 3.0 5.2 2.0 Iris-virginica

6.2 3.4 5.4 2.3 Iris-virginica

5.9 3.0 5.1 1.8 Iris-virginica
