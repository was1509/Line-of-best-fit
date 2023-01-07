import numpy as np
from matplotlib import pyplot as plt
from statistics import mean

y_new = []
outlier_x = []
not_outliers_x = []
outliers = []
not_outliers = []
count = 0
c = -1

x = str(input("X: "))
y = str(input("Y: "))

x_one = list(map(float , x.split()))
y_one = list(map(float , y.split()))

x_list = np.array(x_one , dtype=np.float64)
y_list = np.array(y_one , dtype=np.float64)

gradient = ((mean(x_list) * mean(y_list)) - (mean(x_list * y_list))) / ((mean(x_list) * mean(x_list) - (mean(x_list * x_list))))
            
constant = (mean(y_one)) - (gradient * mean(x_one))

for i in x_one:
    y_new.append((gradient * i) + constant)

mean_y = mean(y_one)
for j in y_one:
    count += (j - mean_y)**2

standard_deviation = (count / (len(y_one))) ** 0.5

for a in y_one:
    c += 1
    if a < (mean_y - standard_deviation) or a > (mean_y + standard_deviation):
        outliers.append(a)
        outlier_x.append(x_one[c])
    else:
        not_outliers.append(a)
        not_outliers_x.append(x_one[c])
        
plt.plot(not_outliers_x, not_outliers , "o")
plt.plot(outlier_x , outliers , "x", color = "red")
plt.plot(x_one , y_new)
plt.ylabel("Y Axis")
plt.xlabel("X Axis")
plt.grid()