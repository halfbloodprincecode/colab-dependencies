import tensorflow as tf
from tensorflow import keras
from vis.utils import utils

def fromModel(date, model, layer_names, inputs=None, final_output=False):
  index = [utils.find_layer_idx(model, name) for name in layer_names]
  outputs = [model.layers[i].output for i in index]
  if final_output:
    outputs.append(model.layers[-1].output)
  if inputs == None:
    inputs = model.inputs
  extractor = keras.Model(inputs=inputs, outputs=outputs)
  return extractor(date, training=False)

def midpoint(data, model, inputs):
  return fromModel(data, model, layer_names=[], inputs=[model.layers[utils.find_layer_idx(model, input_name)].input for input_name in inputs], final_output=True)
