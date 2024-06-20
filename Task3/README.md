### Flower Classification dataset and RESNET-10
```
flower_dataset_url = "http://download.tensorflow.org/example_images/flower_photos.tgz"
resnet_model = "https://www.kaggle.com/models/google/resnet-v2/TensorFlow2/101-classification/2"
```

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


##### ERROR ENCOUNTERED
```
ValueError: Only instances of `keras.Layer` can be added to a Sequential model.
Received: <tensorflow_hub.keras_layer.KerasLayer object at 0x7f4e00437280> (of type <class 'tensorflow_hub.keras_layer.KerasLayer'>)
```

