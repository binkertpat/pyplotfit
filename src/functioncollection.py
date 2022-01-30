import numpy as np


def doublegaussianwithlinearunderground(x, c1, mu1, sigma1, c2, mu2, sigma2, a, b):
    """ input follow params: c1, mu1, sigma1, c2, mu2, sigma2, a, b """
    return c1 * np.exp(- (x - mu1) ** 2.0 / (2.0 * sigma1 ** 2.0)) + c2 * np.exp(
        - (x - mu2) ** 2.0 / (2.0 * sigma2 ** 2.0)) + (a * x + b)


def gaussianwithlinearunderground(x, c1, mu1, sigma1, a, b):
    """ input follow params: c1, mu1, sigma1, a, b """
    return c1 * np.exp(- (x - mu1) ** 2.0 / (2.0 * sigma1 ** 2.0)) + (a * x + b)


def linear(x, a, b):
    """ input follow params: a, b """
    return a * x + b


def exp(x, a, b):
    return a/(x**b)


def explabel():
    return "Exp.-Fit: $f(x) = \\frac{a}{x^b}$"


def doublegaussianwithlinearundergroundlabel():
    return "Gauß-Fit: $f(x) = c_1 e^{(-(x-\\mu_1)^2/(2\\sigma_1^2))} + c_2 e^{(-(x-\\mu_2)^2/(2\\sigma_2^2))} + a*x+b$"


def linearlabel():
    return "linearer Fit: $f(x) = a*x+b$"


def gaussianwithlinearundergroundlabel():
    return "Gauß-Fit: $f(x) = c_1 e^{(-(x-\\mu_1)^2/(2\\sigma_1^2))} + a*x+b$"

