from sklearn.datasets import load_boston
import matplotlib.pyplot as plt
import random
dataset = load_boston()
#dataset
x,y=dataset['data'],dataset['target']
dataset.feature_names
dataset['DESCR']
X_rm = x[:,5]
# Gradient descent
#Assume that the target funciton is a linear function:𝑦=𝑘∗𝑟𝑚+𝑏
#define target function
def price(rm, k, b):
    return k * rm + b
# define loss function 
def loss(y,y_hat):
    return sum((y_i - y_hat_i)**2 for y_i, y_hat_i in zip(list(y),list(y_hat)))/len(list(y))
# define partial derivative 
def partial_derivative_k(x, y, y_hat): 
    n = len(y)
    gradient = 0
    for x_i, y_i, y_hat_i in zip(list(x),list(y),list(y_hat)):
        gradient += (y_i-y_hat_i) * x_i
    return -2/n * gradient
def partial_derivative_b(y, y_hat):
    n = len(y)
    gradient = 0
    for y_i, y_hat_i in zip(list(y),list(y_hat)):
        gradient += (y_i-y_hat_i)
    return -2 / n * gradient
#initialized parameters
k = random.random() * 200 - 100  # -100 100
b = random.random() * 200 - 100  # -100 100
learning_rate = 1e-3
iteration_num = 200 
losses = []
for i in range(iteration_num):
    
    price_use_current_parameters = [price(r, k, b) for r in X_rm]  # \hat{y}
    
    current_loss = loss(y, price_use_current_parameters)
    losses.append(current_loss)
    print("Iteration {}, the loss is {}, parameters k is {} and b is {}".format(i,current_loss,k,b))
    
    k_gradient = partial_derivative_k(X_rm, y, price_use_current_parameters)
    b_gradient = partial_derivative_b(y, price_use_current_parameters)
    
    k = k + (-1 * k_gradient) * learning_rate
    b = b + (-1 * b_gradient) * learning_rate
best_k = k
best_b = b
# plot the relation between loss function and iteration
plt.plot(list(range(iteration_num)),losses)
plt.xlabel('Iteration')
plt.ylabel('The value of loss function')
plt.title('Gradient descent process')
plt.show()
# Regress the price function use best parameters and plot it
price_use_best_parameters = [price(r, best_k, best_b) for r in X_rm]
plt.xlabel('The average number of rooms in a house (RM)')
plt.ylabel('House price (Price)')
plt.title('The relationship between the average number \nof rooms and house price in linear regression')

plt.scatter(X_rm,y)
plt.scatter(X_rm,price_use_current_parameters)
plt.show()

# fig = plt.figure()
# ax1 = fig.add_subplot(2,1,1) # 画2行1列个图形的第1个
# ax2 = fig.add_subplot(2,1,2) # 画2行1列个图形的第2个
# ax1.plot(x, frequiences)
# # print(plt.plot(x, np.log(frequiences)))
# ax2.plot(x, np.log(frequiences))
# plt.show()