import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r, p, std_err)

# r (Correlation Coefficient): This is the Pearson correlation coefficient of the linear regression. The correlation coefficient, r, measures the strength and direction of the linear relationship between the two variables x and y. Its value ranges from -1 to 1:

# r = 1 indicates a perfect positive linear relationship.( x increases y increaes)
# r = -1 indicates a perfect negative linear relationship. ( x increases y decreases)
# r = 0 indicates no linear relationship.
# p (P-value): This is the two-sided p-value for a hypothesis test whose null hypothesis is that the slope of the regression line is zero. The p-value helps you determine the statistical significance of your results:

# A small p-value (typically ≤ 0.05) indicates strong evidence against the null hypothesis, suggesting that the slope is not zero and there is a significant linear relationship between x and y.
# A large p-value (> 0.05) suggests weak evidence against the null hypothesis, indicating that the slope might be zero, and there may not be a significant linear relationship between x and y


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

speed = myfunc(10)  # predict the speed of 10 year old car
print(speed)

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
