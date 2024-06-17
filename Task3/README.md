### I used the flower classification dataset for Transfer Learning and ResNet-10
```
flower_dataset_url = "http://download.tensorflow.org/example_images/flower_photos.tgz"
resnet_model = "https://www.kaggle.com/models/google/resnet-v2/TensorFlow2/101-classification/2"
```


#### Error in Jupyter Notebook

##### feature extraction

```
feature_extractor_layer = hub.KerasLayer(
    resnet_model,
    input_shape=(224, 224, 3),
    trainable=False)
```
##### model creation

```
model = tf.keras.Sequential([
  feature_extractor_layer,
  layers.Dense(class_num)
])
```


###### I encountered an error in Jupyter Notebook when I executed the model creation code which I could not resolve in time. 
###### It had something to do with outdated version of Tensorflow_hub
###### But when I tried to execute the notebook file in Google Colab everything was working just fine but training the model was taking so long.

```
ValueError: Only instances of `keras.Layer` can be added to a Sequential model.
Received: <tensorflow_hub.keras_layer.KerasLayer object at 0x7f4e00437280> (of type <class 'tensorflow_hub.keras_layer.KerasLayer'>)
```
###### Due to the error I was unable to execute the file on Jupyter Notebook. But on Colab, it was taking too much time to train the model for 6 epochs.
