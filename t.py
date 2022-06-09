'''
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 *   t.py
 *   Author: Charan Reddy Nareddula  (charan9331@gmail.com)
 '''
from neuralnetv3test import *
import cProfile
import sys
import time
def train():

    iteration=0
    nn.debug=False
    training_start = time.time()
    start = time.time()
    while iteration< 5000 :
        i=0
        if iteration%100 == 0:
            print(iteration,"Predict Error Percentage: ",nn.error_percentage)
            end = time.time()
            print("Time taken: ",(end-start))
            
            nn.data_count =0
            nn.cumulative_error =0
            #nn.debug=True
        
        while i< datalen :
            if types[i] == 2:
                types[i] = 0.5
            nn.predict([sepallength[i],sepalwidth[i],petallength[i],petalwidth[i]],[types[i]],i)
            nn.train([sepallength[i],sepalwidth[i],petallength[i],petalwidth[i]],[types[i]],1)
            i=i+1

        iteration=iteration+1
    training_end = time.time()
    print("Total time taken",(end-start))
    nn.saveNeuralNet()

def inference():
    i =0
    iteration =0
    nn.loadNeuralNet()
    while i< datalen :
        if types[i] == 2:
            types[i] = 0.5
        nn.predict([sepallength[i],sepalwidth[i],petallength[i],petalwidth[i]],[types[i]],i)
        i = i+1
    print(iteration,"Predict Error Percentage: ",nn.error_percentage)
        
pr = cProfile.Profile()
pr.enable()

batch = False
batch_len=10
#nn = NeuralNet([4,16,26,16,25,1])
nn = NeuralNet([4,8,5,1])
#,gpu_enabled=False,name="testsmall",load=False,batch_size=batch_len,learning_rate=0.005)
#nn = NeuralNet([4,5600,5600,5600,5500,1],gpu_enabled=True,name="testLarge",load=False,batch_size=batch_len)
#nn = NeuralNet([4,3,4,5,1],gpu_enabled=False,name="testsmall",load=False,batch_size=batch_len)
#nn = NeuralNet([4,3,4,5,1],False)
data = pd.read_csv("/Users/charanreddy/Downloads/iris_training.txt")
#print (data)
sepallength = data.SepalLength.values.tolist()
sepalwidth = data.SepalWidth.values.tolist()
petallength = data.PetalLength.values.tolist()
petalwidth = data.PetalWidth.values.tolist()
types = data.types.values.tolist()

datalen = len(sepallength)
'''i=0
while i< datalen :
    if types[i] == 2:
        types[i] = 0.5
    print ("following is of type",types[i])
    nn.train([sepallength[i],sepalwidth[i],petallength[i],petalwidth[i]],[types[i]],1)
    i=i+1'''

#inference()
train()


#nn.bulk_print()
#sys.exit()
#print("slots: ",nn.__dict__)

    



#pr.print_stats()
