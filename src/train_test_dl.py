#%%
import numpy as np
from lr_utils import load_dataset
from ttutils.TTLogging import tt_logger

# Loading the data (cat/non-cat)
def data_preparation():
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
    # %%
    m_train = train_set_x_orig.shape[0]
    m_test =  test_set_x_orig.shape[0]
    num_px = train_set_x_orig.shape[1]

    tt_logger.info ("Number of training examples: m_train = " + str(m_train))
    tt_logger.info ("Number of testing examples: m_test = " + str(m_test))
    tt_logger.info ("Height/Width of each image: num_px = " + str(num_px))
    tt_logger.info ("Each image is of size: (" + str(num_px) + ", " + str(num_px) + ", 3)")
    tt_logger.info ("train_set_x shape: " + str(train_set_x_orig.shape))
    tt_logger.info ("train_set_y shape: " + str(train_set_y.shape))
    tt_logger.info ("test_set_x shape: " + str(test_set_x_orig.shape))
    tt_logger.info ("test_set_y shape: " + str(test_set_y.shape))
    # %%
    # Reshape the training and test examples

    train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[1]*train_set_x_orig.shape[2]*train_set_x_orig.shape[3],train_set_x_orig.shape[0])
    test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[1]*test_set_x_orig.shape[2]*test_set_x_orig.shape[3],test_set_x_orig.shape[0])

    tt_logger.info ("train_set_x_flatten shape: " + str(train_set_x_flatten.shape))
    tt_logger.info ("train_set_y shape: " + str(train_set_y.shape))
    tt_logger.info ("test_set_x_flatten shape: " + str(test_set_x_flatten.shape))
    tt_logger.info ("test_set_y shape: " + str(test_set_y.shape))
    tt_logger.info ("sanity check after reshaping: " + str(train_set_x_flatten[0:5,0]))

    train_set_x = train_set_x_flatten/255.
    test_set_x = test_set_x_flatten/255.
    return train_set_x, train_set_y, test_set_x, test_set_y, classes


def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    z -- A scalar or numpy array of any size.

    Return:
    s -- sigmoid(z)
    """
   
    s = 1/(1+np.exp(-z))   
    
    return s


def initialize_with_zeros(dim):
    """
    This function creates a vector of zeros of shape (dim, 1) for w and initializes b to 0.
    
    Argument:
    dim -- size of the w vector we want (or number of parameters in this case)
    
    Returns:
    w -- initialized vector of shape (dim, 1)
    b -- initialized scalar (corresponds to the bias)
    """    
    
    w = np.zeros((dim,1))
    b = 0  
    
    return w, b


def propagate(w, b, X, Y):
    """
    Implement the cost function and its gradient for the propagation explained above

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat) of size (1, number of examples)

    Return:
    cost -- negative log-likelihood cost for logistic regression
    dw -- gradient of the loss with respect to w, thus same shape as w
    db -- gradient of the loss with respect to b, thus same shape as b    
   
    """
    
    m = X.shape[1]
    A = sigmoid(np.dot(w.T,X) + b)              # compute activation
    cost = np.sum(((- np.log(A))*Y + (-np.log(1-A))*(1-Y)))/m  # compute cost
    
    dw = (np.dot(X,(A-Y).T))/m
    db = (np.sum(A-Y))/m
    
    cost = np.squeeze(cost)
    
    grads = {"dw": dw,
             "db": db}
    
    return grads, cost


def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost = False):
    """
    This function optimizes w and b by running a gradient descent algorithm
    
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of shape (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat), of shape (1, number of examples)
    num_iterations -- number of iterations of the optimization loop
    learning_rate -- learning rate of the gradient descent update rule
    tt_logger.info_cost -- True to tt_logger.info the loss every 100 steps
    
    Returns:
    params -- dictionary containing the weights w and bias b
    grads -- dictionary containing the gradients of the weights and bias with respect to the cost function
    costs -- list of all the costs computed during the optimization, this will be used to plot the learning curve.    
   
    """
    
    costs = []
    
    for i in range(num_iterations):       
        
        
        grads, cost = propagate(w, b, X, Y)        
        dw = grads["dw"]
        db = grads["db"]
        w = w - (learning_rate*dw)
        b = b - (learning_rate*db)
        if i % 100 == 0:
            costs.append(cost)        
       
        if print_cost and i % 100 == 0:
            tt_logger.info ("Cost after iteration %i: %f" %(i, cost))
    
    params = {"w": w,
              "b": b}
    
    grads = {"dw": dw,
             "db": db}
    
    return params, grads, costs

def predict(w, b, X):
    '''
    Predict whether the label is 0 or 1 using learned logistic regression parameters (w, b)
    
    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    
    Returns:
    Y_prediction -- a numpy array (vector) containing all predictions (0/1) for the examples in X
    '''
    
    m = X.shape[1]
    Y_prediction = np.zeros((1,m))
    w = w.reshape(X.shape[0], 1)    
       
    A = sigmoid(np.dot(w.T,X) + b)           # Dimentions = (1, m)
    tt_logger.info(f"A: {A}")
    Y_prediction = (A >= 0.5) * 1.0
    return Y_prediction

def model(X_train, Y_train, X_test, Y_test, num_iterations = 2000, learning_rate = 0.5, print_cost = False):
    """
    Builds the logistic regression model by calling the function you've implemented previously
    
    Arguments:
    X_train -- training set represented by a numpy array of shape (num_px * num_px * 3, m_train)
    Y_train -- training labels represented by a numpy array (vector) of shape (1, m_train)
    X_test -- test set represented by a numpy array of shape (num_px * num_px * 3, m_test)
    Y_test -- test labels represented by a numpy array (vector) of shape (1, m_test)
    num_iterations -- hyperparameter representing the number of iterations to optimize the parameters
    learning_rate -- hyperparameter representing the learning rate used in the update rule of optimize()
    tt_logger.info_cost -- Set to true to tt_logger.info the cost every 100 iterations
    
    Returns:
    d -- dictionary containing information about the model.
    """  
    
    # initialize parameters with zeros (≈ 1 line of code)
    w, b = initialize_with_zeros(X_train.shape[0])

    # Gradient descent (≈ 1 line of code)
    parameters, grads, costs = optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)
    
    # Retrieve parameters w and b from dictionary "parameters"
    w = parameters["w"]
    b = parameters["b"] 

    # Predict test/train set examples (≈ 2 lines of code)
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)

    # tt_logger.info train/test Errors
    tt_logger.info("train accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    tt_logger.info("test accuracy: {} %".format(100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))

    
    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test, 
         "Y_prediction_train" : Y_prediction_train, 
         "w" : w, 
         "b" : b,
         "learning_rate" : learning_rate,
         "num_iterations": num_iterations}
    
    return d
