from keras.utils.vis_utils import plot_model

def plot_model_graph(model):
    plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)