from NN_Visualizer import *
import tensorflow as tf
# import VizLayers.VizLayersClassModule

try:
  model=tf.keras.models.load_model("model.keras")
  # Initializing the Class Object
  vl = VizLayersClass(model=model)
  
  # fetching a sample image from the dataset
  _, (x_test,_)=tf.keras.datasets.mnist.load_data()
  x_test=x_test/255.
  index=np.random.choice(x_test.shape[0])
  image=x_test[index, :, :]
  
  # setting required parameters
  fn = lambda input: np.reshape(input,(1,784))
  vl.setTransformInputFunction(fn)
  print('getting predicted outputs for the image:')
  print(vl.getOutputs(image), end='\n\n\n')
  
  print('getting the [weights, bias] of the layers:')
  print(vl.getLayerWeights())
  
  vl.run(port=5050)
except Exception as e:
  print("error")
  print(e)
  exit(0)