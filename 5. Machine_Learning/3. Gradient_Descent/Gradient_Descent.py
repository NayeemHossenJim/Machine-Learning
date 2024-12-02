import numpy as nb

def Gradient_Descent(x,y):
    learningRate = 0.08
    m_curr = b_curr = 0
    iteration = 10000
    n = len(x)
    for i in range(iteration):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        m_der = -(2/n)*sum(x*(y-y_predicted))
        b_der = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learningRate * m_der
        b_curr = b_curr - learningRate * b_der
        print("m {},b {},cost {} iteration{}".format(m_curr,b_curr,cost,i))

x = nb.array([1,2,3,4,5])
y = nb.array([5,7,9,11,13])

Gradient_Descent(x,y)