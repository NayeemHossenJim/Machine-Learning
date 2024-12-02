import numpy as nb

def Gradient_Descent(x,y):
    learningRate = 0.001
    m_curr = b_curr = 0
    iteration = 1000
    n = len(x)
    for i in range(iteration):
        y_predicted = m_curr * x + b_curr
        m_der = -(2/n)*(x*(y-y_predicted))
        b_der = -(2/n)*(y-y_predicted)
        m_curr = m_curr - learningRate * m_der
        b_der = b_der - learningRate * b_der
        print("m {},b {}, iteration{}".format(m_curr,b_curr,i))

x = nb.array([1,2,3,4,5])
y = nb.array([5,7,9,11,13])

Gradient_Descent(x,y)