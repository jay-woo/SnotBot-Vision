import numpy as np
from random import shuffle

def svm_loss_naive(W, X, y, reg):
  """
  Structured SVM loss function, naive implementation (with loops)
  Inputs:
  - W: C x D array of weights
  - X: D x N array of data. Data are D-dimensional columns
  - y: 1-dimensional array of length N with labels 0...K-1, for K classes
  - reg: (float) regularization strength
  Returns:
  a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  dW = np.zeros(W.shape) # initialize the gradient as zero
  dLoss = np.zeros(W.shape)
  epsilon = 0.00001

  # compute the loss and the gradient
  num_classes = W.shape[0]
  num_train = X.shape[1]
  num_weights = W.shape[1]
  loss = 0.0
  for k in xrange(num_weights):
    dLoss1 = 0.0
    dLoss2 = 0.0
    for i in xrange(num_train):
      scores = W.dot(X[:, i])
      correct_class_score = scores[y[i]]
      for j in xrange(num_classes):
        W_new1 = W
        W_new2 = W
        W_new1[j][k] += epsilon
        W_new2[j][k] -= epsilon
        dScores1 = W_new1.dot(X[:, i])
        dScores2 = W_new2.dot(X[:, i])
        if j == y[i]:
          continue
        margin = scores[j] - correct_class_score + 1 # note delta = 1
        dMargin1 = dScores1[j] - correct_class_score + 1
        dMargin2 = dScores2[j] - correct_class_score + 1

        if margin > 0:
          loss += margin
          dLoss1 += dMargin1
          dLoss2 += dMargin2
        dLoss1 /= num_train
        dLoss1 += 0.5 * reg * np.sum(W_new1 * W_new1)
        dLoss2 /= num_train
        dLoss2 += 0.5 * reg * np.sum(W_new2 * W_new2)
        dW[j][k] = (dLoss1 - dLoss2) / (2 * epsilon)

  # Right now the loss is a sum over all training examples, but we want it
  # to be an average instead so we divide by num_train.
  loss /= num_train

  # Add regularization to the loss.
  loss += 0.5 * reg * np.sum(W * W)

  #############################################################################
  # TODO:                                                                     #
  # Compute the gradient of the loss function and store it dW.                #
  # Rather that first computing the loss and then computing the derivative,   #
  # it may be simpler to compute the derivative at the same time that the     #
  # loss is being computed. As a result you may need to modify some of the    #
  # code above to compute the gradient.                                       #
  #############################################################################


  return loss, dW


def svm_loss_vectorized(W, X, y, reg):
  """
  Structured SVM loss function, vectorized implementation.

  Inputs and outputs are the same as svm_loss_naive.
  """
  loss = 0.0
  dW = np.zeros(W.shape) # initialize the gradient as zero

  num_classes = W.shape[0]
  num_train = X.shape[1]
  num_weights = W.shape[1]

  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the structured SVM loss, storing the    #
  # result in loss.                                                           #
  #############################################################################
  scores = W.dot(X)
  margin = scores - y + 1
  loss = 0.0
  for i in xrange(len(margin)):
      for j in xrange(len(margin[0])):
          if i != y[j] and margin[i][j] > 0:
              loss += margin[i][j]

  loss /= num_train
  loss += 0.5 * reg * np.sum(W * W)
  print loss
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################


  #############################################################################
  # TODO:                                                                     #
  # Implement a vectorized version of the gradient for the structured SVM     #
  # loss, storing the result in dW.                                           #
  #                                                                           #
  # Hint: Instead of computing the gradient from scratch, it may be easier    #
  # to reuse some of the intermediate values that you used to compute the     #
  # loss.                                                                     #
  #############################################################################
  pass
  #############################################################################
  #                             END OF YOUR CODE                              #
  #############################################################################

  return loss, dW
