from examples.data_science.statistics import correlation, standard_deviation, mean, de_mean


def predict(alpha, beta, x_i):
    return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
    """ the error from predicting beta * x_i + alpha
    when the actual value is y_i """
    return y_i - predict(alpha, beta, x_i)

def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2.
               for x_i, y_i in zip(x, y))

def least_squares_fit(x, y):
    """ given training values for x and y,
    find the least-squares values of alpha and beta """
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta

def total_sum_of_squares(y):
    """ the total squared variation of y_i's from their mean """
    return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):
    """ the fraction of variation in y captured by the model, which equals
     1 - the fraction of variation in y not captured by the model """