import numpy as np
import time
import glob
import os
import csv
import pickle

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix  

class knn:
    def __init__(self):
        self.knclassifier = KNeighborsClassifier(n_neighbors=3)
        
    def train(self, x_train, y_train):
        self.knclassifier.fit(x_train, y_train)

    def evaluate(self, x_test, y_test):
        y_pred = self.knclassifier.predict(x_test)

        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

        # with open('performance.csv', mode='a') as per_file:
        #     per_writer = csv.writer(per_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #     per_writer.writerow([self.NODES_IN_INPUT, 
        #         self.NODES_IN_HIDDEN, 
        #         self.EPOCHS, 
        #         self.BATCH_SIZE, 
        #         self.HIDDEN_LAYERS,
        #         int(time.time()),
        #         loss_and_metrics[0], 
        #         loss_and_metrics[1]])
            
    def save(self):
        filename = "../../models/knn" + str(int(time.time()))
        pickle.dump(self.knclassifier, open(filename, 'wb'))

    def load(self):
        list_of_files = glob.glob('../../models/knn*') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print(latest_file)
        # self.model = load_model("../models/ann")
        # self.model = load_model(latest_file)

        self.knclassifier = pickle.load(open(latest_file, 'rb'))

    def predict(self, data):
        # self.model.predict()
        return self.knclassifier.predict(data)