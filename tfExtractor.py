import tensorflow as tf
from tensorflow import keras
from vis.utils import utils


def fromModel(date, model, layer_names):
  index = [utils.find_layer_idx(model, name) for name in layer_names]
  _outputs = [model.layers[i] for i in index]
  _outputs.append(model.layers[-1])
  extractor = keras.Model(inputs=model.inputs, outputs=_outputs)
  return extractor(date, training=False)
