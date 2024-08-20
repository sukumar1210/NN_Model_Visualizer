currently working with model being an object of <class 'keras.src.models.sequential.Sequential'>.
```
class transformerVisualizer:
	DataMembers:
	- model
	- trainingData
	- transformInputFunction
	- layerWeights
	

	Methods:
	setModel():
		- job: setting the model as class attribute
	
	getLayerWeights():
		- need: visualize layers.output into different charts
		- job: extract the tensors for the weights of each layer and make it avaiable such that when the frontend makes a refresh call, these tensors may be sent to the front-end.
	
	def setTransformInputFunction():
		job: this will be used in the user's code itself in order to prepare/export the model according to our needs

	def getOutputs():
		inputFunction is an optional function that can be used to transform the input if needed before it is passed to the model
		need: to get the output of each layer for a given input
		job: extract the output of each layer for a given input and store it such that it might be visualised on front end
		dependency: self.model

	setTrainingData(trainingData):
		- takes training data and stores it for later use
	
	getTrainingData():
		- need: to visualize the training dataset in some form
		- Job: extract and prepare the data such that it might be visualised on front end
		- dependency: setTrainingData(trainingData)
		
	compareInput(trainingData, input):
		- job: takes an input and fetches similar data from training data and visualises the model.run output for different layers (stores in order to later be sent to the frontend).
		- dependency: setTrainingData(trainingData)
	
	run():
		- job: start the flask server and call all the relevent functions.
```