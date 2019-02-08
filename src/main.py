import pandas as pd
import numpy as np
import time
# importing the other files
import client
import getMuse
import evaluate


mongoClient = client.client()

while(True):
    if(mongoClient.checkNewData()):
        # museData = getMuse.getMuse()

        evaluater = evaluate.evaluate()
        results = evaluater.getResults(mongoClient.getNewData("Epworth"), mongoClient.getNewData("stopBang"), mongoClient.getNewData("weights"))

        mongoClient.sendData(results)

        print("eyy")

    time.sleep(5)
