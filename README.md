 
# Performance of ToyNeuralNet on various Platforms:
ToyNeuralNet is Neuralnet implemented from scratch without using any ML library. The goal of the project is to measure the performance of the  ToyNeuralNet on various platforms like python list vs Numpy, cpu vs gpu, neural network size,batch size, training vs inference..etc

Following are different performance experiments of ToyNeuralnet used for Training purposes:

- ToyNeuralNet using different versions of Python:
    - using python List : very slow (260sec)
    - using numpy library: Best of all the three (95sec) 
    - Summary: Numpy is the best of all(python list and numpy). Reason: Numpy Array are implemented natively, due to this matrix multiplication is faster.
    - using GPU : better than numpy when the layer contain large number of neurons
- ToyNeuralNet using CPU versus GPU with python:
    - Small number of neurons vs large number of neurons per layer:
      -  CPU as better latency when compared to GPU for small number of neurons, for large neurons GPU is better. The reason is overhead in submitting the job to GPU, overhead of CPU and GPU communication is large for small neuralnets when compare to large neural net.
    - Workload: Training vs predict:  
      -  GPU provides better latency in Training  when compare to Predict. Reason: Predict contain mXn by mX1 multiplication, but Training need mXn by mXn mulitplication , and also update of weights.
    -  Batch vs Without Batch: 
    	 - Batch is good for GPU and CPU. As batch level increases, the efficiency of cpu parallelism goes up.  


# Test Setup 

- Data Set : Iris flower Dataset.
- Large-NeuralNet:  with large number of neurons: Network size: [4,1600,2600,1600,2500,1]
- Small-NeuralNet:  with small number of neurons: Network size: [4,3,4,5,1]
- Test script: test_NN.py

 




