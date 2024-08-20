import numpy as np
import json
import tensorflow as tf
from flask import Flask, request, jsonify
import threading
 
class VizLayersClass:
    def __init__(self, model=None, trainingData=None, transformInputFunction=None):
        # Attributes
        # model
        if model:
            self.model=tf.keras.models.Model(
                model.inputs,
                [layer.output for layer in model.layers]
            )
            print("Model Set")
        else:
            self.model = None
        
        # Training Data 
        if trainingData:
            self.trainingData = trainingData
        else:
            self.trainingData = None
        
        # Transform Input Function (used in case the input needs to be transformed before being passed to the model for prediction)
        if transformInputFunction:
            self.transformInputFunction = transformInputFunction
        else:
            self.transformInputFunction = lambda input: input

        self.layerWeights = None
        # layerOutputs
        # self.layerBias = {}

    # Methods
    def setModel(self, model):
        # setting the model as class attribute
        self.model=tf.keras.models.Model(
            model.inputs,
            [layer.output for layer in model.layers]
        )

    def setTransformInputFunction(self, transformInputFunction):
        # job: this will be used in the user's code itself in order to prepare/export the model according to our needs
        self.transformInputFunction = transformInputFunction

    def getLayerWeights(self):
        # need: visualize layers.output into different charts
        # job: extract the tensors for the weights of each layer and make it avaiable such that when the frontend makes a refresh call, these tensors may be sent to the front-end.
        # dependency: self.model
        if not self.model:
            raise Exception("Model Not set")
        
        tempWeights = []
        for layer in self.model.layers:
            temp = layer.get_weights()
            for i in range(len(temp)):
                temp[i] = temp[i].tolist()
            tempWeights.append(temp)
        self.layerWeights = tempWeights
        return self.layerWeights

    def getOutputs(self, input, transformInputFunction=None):
        # inputFunction is an optional function that can be used to transform the input if needed before it is passed to the model
        # need: to get the output of each layer for a given input
        # job: extract the output of each layer for a given input and store it such that it might be visualised on front end
        # dependency: self.model
        if not self.model:
            raise Exception("Model Not set")
        
        print("Getting Outputs")
        if not transformInputFunction:
            transformInputFunction = self.transformInputFunction
        response = self.model.predict(transformInputFunction(input))
        return response

    def setTrainingData(self, trainingData):
        # takes training data and stores it for later use
        self.trainingData = trainingData
        print("Training Data Set")

    def getTrainingData(self):
        # need: to visualize the training dataset in some form
        # Job: extract and prepare the data such that it might be visualised on front end
        # dependency: setTrainingData(trainingData)
        print("Visualizing Training Data")
        # TBC
     
    def compareInput(trainingData, input):
        # job: takes an input and fetches similar data from training data and visualises the model.run output for different layers (stores in order to later be sent to the frontend).
        # dependency: setTrainingData(trainingData)
        print("Comparing Input")
        # TBC


    def run(self, port=5000):
        # job: start the flask server and call all the relevent functions.
        
        if not self.model:
            raise Exception("Model Not set")
        
        app = Flask(__name__)
        
        @app.route('/getLayerWeights', methods=['POST'])
        def getLayerWeights():
            self.getLayerWeights()
            return jsonify({'layerWeights': self.layerWeights})
        
        @app.route('/getLayerOutputs', methods=['POST'])
        def getLayerOutputs():
            input = json.loads(request.form['input'])
            response = self.getOutputs(input)
            for i in range((len(response))):
                response[i] = response[i].tolist()
                
            return response
        
        flask_server_thread = threading.Thread(target=app.run(port=port))
        print('Server Started')
        
        # available endpoints
        print("Available Endpoints:")
        print("1. /getLayerWeights")
        print("2. /getLayerOutputs")