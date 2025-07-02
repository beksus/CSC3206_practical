from sklearn import datasets
import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


diabetes = datasets.load_diabetes()
dt = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
y = pd.DataFrame(diabetes.target, columns=['target'])


X_train, X_test, y_train, y_test = train_test_split(
    dt, y, test_size=0.2, random_state=42
)
def model(x, m, c):
    return m * x + c

def cost(y, yh):
    return ((y - yh) ** 2).mean() / 2

def derivatives(x, y, yh):
    n = len(y)
    dJ_dm = -((y - yh) * x).sum() / n
    dJ_dc = -(y - yh).sum() / n
    return {'m': dJ_dm, 'c': dJ_dc}


learningrate = 0.1
m = [0]
c = [0]
J = [cost(y_train['target'], X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1])))]

J_min = 0.01
del_J_min = 0.0001
max_iter = 10000

plt.ion()
plt.scatter(X_train['bmi'], y_train['target'], color='red')
plt.title('Training data')
plt.xlabel('BMI')
line = None

for i in range(max_iter):
    yh = X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
    grads = derivatives(X_train['bmi'], y_train['target'], yh)
    m_new = m[-1] - learningrate * grads['m']
    c_new = c[-1] - learningrate * grads['c']
    m.append(m_new)
    c.append(c_new)
    J_new = cost(y_train['target'], X_train['bmi'].apply(lambda x: model(x, m_new, c_new)))
    J.append(J_new)

    # Visual feedback
    if line:
        line[0].remove()
    line = plt.plot(X_train['bmi'], X_train['bmi'].apply(lambda x: model(x, m_new, c_new)), '-', color='green')
    plt.pause(0.001)

    print('.', end='')
    sys.stdout.flush()

    # Termination conditions
    if J_new < J_min:
        break
    if abs(J[-2] - J_new) / J_new < del_J_min:
        break
plt.ioff()

y_train_pred = X_train['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
y_test_pred = X_test['bmi'].apply(lambda x: model(x, m[-1], c[-1]))
print('\nAlgorithm terminated with')
print(f'  {len(J)} iterations,')
print(f'  m {m[-1]}')
print(f'  c {c[-1]}')
print(f'  training cost {J[-1]}')
testcost = cost(y_test['target'], y_test_pred)
print(f'  testing cost {testcost}')

plt.figure()
plt.scatter(X_test['bmi'], y_test['target'], color='red')
plt.plot(X_test['bmi'], X_test['bmi'].apply(lambda x: model(x, m[-1], c[-1])), '-', color='green')
plt.title('Testing data')
plt.xlabel('BMI')
plt.show()