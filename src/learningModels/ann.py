import numpy as np

from keras.models import Sequential
from keras.layers import Dense, Activation

class ann:
    def __init__(self):
        self.model = Sequential()
        # Hyper params:
        self.NODES_IN_HIDDEN = 3
        self.EPOCHS = 50
        self.BATCH_SIZE = 16

    def createNetowrk(self):
        # Input Layer
        self.model.add(Dense(3, input_dim=2, activation='relu'))
        # Hidden Layer
        self.model.add(Dense(self.NODES_IN_HIDDEN, activation='relu'))
        # Output Layer
        self.model.add(Dense(1, activation="softmax"))
        self.model.compile(loss='mean_squared_error', optimizer='adam')

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train, epochs=self.EPOCHS,batch_size=self.BATCH_SIZE)

    def evaluate(self, x_test, y_test):
        loss_and_metrics = self.model.evaluate(x_test, y_test, 
                                                batch_size=self.BATCH_SIZE)

        print(loss_and_metrics)

    def save(self):
        pass

    def load(self):
        pass

    def predict(self):
        pass