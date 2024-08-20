# NN_Model_Visualizer
This is a Python Package (Frontend TBC) that visualizes different parameters like the layer weights and layer-wise output for an input for a Neural Network.

## Basic Usage
- Import the `NN_Visualizer` as a package
- Instantiate the `NN_Visualizer` Class and set the model either using the constructor or the `.setModel(model)` method.
> Model needs to be an instance of tf.keras.Model
- Set an input tranform function using `.transformInputFunction(function)` to be used to transform the input provided before passing on to the model for generating outputs.
- Use `.run()` to start a backend that can be used to fetch different parameter of the model by a front-end library. OR use the class methods to retrieve the same within the python file and use something like Matplotlib.

For Class Structure Visit [ClassStructure.md](./NN_Visualizer/classStructure.md)