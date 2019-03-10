# import keras as k
# from keras.models import Sequential
# from keras.layers import Dense, Activation
# from keras.optimizers import Adam
import numpy as np
import pandas as pd
from random import *

class evaluate:
    def __init__(self):
        print("yay")
        pd.options.display.max_rows = 10
        pd.options.display.float_format = '{:.1f}'.format

    def getResults(self, epworth, stopBang, weights):
        epScore = self.getEpworth(epworth)
        sbScore = self.getStopBang(stopBang)
        hrScore = self.getHeartRate()
        brScore = self.getBreathing()
        egScore = self.getEeg()

        totalScore = int(((epScore * weights['epworth']) + 
                    (sbScore * weights['stopBang']) + 
                    (hrScore * weights['heartRate']) + 
                    (brScore * weights['breathing']) + 
                    (egScore * weights['eeg'])))
        
        return ({
            'score': totalScore,
            'heartRate': hrScore,
            'breathing': brScore,
            'eeg': egScore,
            'epworth': epScore,
            'stopBang': sbScore
            })

    def getEpworth(self, data):
        total = (data['ans1'] + data['ans2'] + data['ans3'] + data['ans4']
                + data['ans5'] + data['ans6'] + data['ans7'] + data['ans8'])
        return ((total / 24) * 100)

    def getStopBang(self, data):
        total = (data['ans1'] + data['ans2'] + data['ans3'] + data['ans4']
                + data['ans5'] + data['ans6'] + data['ans7'] + data['ans8'])
        return ((total / 8) * 100)

    def getHeartRate(self):
        result = randint(1, 10)
        return result

    def getBreathing(self):
        result = randint(5, 20)
        return result
    
    def getEeg(self):
        result = randint(10, 30)
        return result
    
    def setupNetwork(self):
        pd.options.display.max_rows = 10
        pd.options.display.float_format = '{:.1f}'.format

        self.trainingData = pd.read_csv("assets/old/Muse.csv", sep=",")
        self.testData = pd.read_csv("assets/new/Muse*", sep=",")

        print(self.trainingData.describe())
        print(self.testData.describe())

        #
        # get and prepare data
        #
        california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
        california_housing_dataframe = california_housing_dataframe.reindex(np.random.permutation(california_housing_dataframe.index))

        print(california_housing_dataframe.describe())

        data=california_housing_dataframe.values

        x_all=data[:,0:8]
        y_all=data[:,8:9]/1000.0

        # training set
        x_train=x_all[0:13600,:]
        y_train=y_all[0:13600,:]
        # validation set
        x_validate=x_all[13600:15300,:]
        y_validate=y_all[13600:15300,:]
        # test set
        x_test=x_all[15300:,:]
        y_test=y_all[15300:,:]

        #
        # Training
        #

        model = Sequential()

        model.add(Dense(10, activation='relu', input_dim = 8, kernel_initializer='normal'))
        model.add(Dense(10, activation='relu', kernel_initializer='normal'))
        model.add(Dense(1, kernel_initializer='normal'))
        # model.add(Dense(1, activation='linear'))
        adam=Adam(lr=0.01)
        model.compile(loss='mean_squared_error', optimizer=adam)

        custom_batch_size=100
        model.fit(x_train, y_train, epochs=100000, batch_size=custom_batch_size)

        # model.summary()
        # print(model.get_weights())

        #
        # Evaluation
        #
        print("Evaluation")
        score_train = model.evaluate(x_train, y_train, batch_size=custom_batch_size)
        print("Evaluation train set: ",score_train,np.sqrt(score_train))
        score_validate = model.evaluate(x_validate, y_validate, batch_size=custom_batch_size)
        print("Evaluation validation set: ",score_validate,np.sqrt(score_validate))
        score_test = model.evaluate(x_test, y_test, batch_size=custom_batch_size)
        print("Evaluation test set: ",score_test,np.sqrt(score_test))

        # manual investigation
        y_predict=model.predict(x_test)
        for i in range(20):
            print(y_test[i],"=>",y_predict[i])
        