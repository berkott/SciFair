import numpy as np
import time
import glob
import os
import csv

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.models import load_model

class ann:
    def __init__(self, nii, nih, e, bs, hl):
        self.model = Sequential()
        # Hyper params:
        self.NODES_IN_INPUT = nii
        self.NODES_IN_HIDDEN = nih
        self.EPOCHS = e
        self.BATCH_SIZE = bs
        self.HIDDEN_LAYERS = hl

    def createNetwork(self, inputDimensions):
        # Input Layer
        self.model.add(Dense(3, input_dim=inputDimensions, activation='relu'))
        # Hidden Layer
        for i in range(self.HIDDEN_LAYERS):
            self.model.add(Dense(self.NODES_IN_HIDDEN, activation='relu'))
        # Output Layer
        self.model.add(Dense(1, activation="sigmoid"))
        self.model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

    def train(self, x_train, y_train):
        self.model.fit(x_train, y_train, epochs=self.EPOCHS,batch_size=self.BATCH_SIZE)

    def evaluate(self, x_test, y_test):
        loss_and_metrics = self.model.evaluate(x_test, y_test, batch_size=self.BATCH_SIZE)
        
        print(loss_and_metrics)
        
        with open('performance.csv', mode='a') as per_file:
            per_writer = csv.writer(per_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            per_writer.writerow([self.NODES_IN_INPUT, 
                self.NODES_IN_HIDDEN, 
                self.EPOCHS, 
                self.BATCH_SIZE, 
                self.HIDDEN_LAYERS,
                int(time.time()),
                loss_and_metrics[0], 
                loss_and_metrics[1]])
            
    def save(self):
        self.model.save("../models/ann" + str(int(time.time())) + ".h5")

    def load(self):
        list_of_files = glob.glob('../models/ann*') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
        # self.model = load_model("../models/ann")
        self.model = load_model(latest_file)

    def predict(self, data):
        # self.model.predict()
        pass
