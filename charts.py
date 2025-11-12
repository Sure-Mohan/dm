import matplotlib.pyplot as plt
import numpy as np
data=[23,4556,78,33,45,7,89,90,34]
plt.hist(data,bins=5,color='skyblue')
plt.title("Histogram")
plt.show()

plt.boxplot(data)
plt.title("Box Plot")
plt.show()

categories=['A','B','C','D']
values=[10,20,15,30]
plt.bar(categories, values,color='orange')
plt.title('Bar Chart')
plt.show()

plt.pie(values, labels=categories, autopct='orange')
plt.title('Pie Chart')
plt.show()
