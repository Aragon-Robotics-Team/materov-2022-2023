import tensorflow as tf 
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
 
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt

iris = load_iris()
x, y = iris.data(), iris.target

x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=123)
# datasets.cifar10.load_data() cifar10 dataset load

trainImages, testImages = x_train, x_test / 255.0, y_train, y_test / 255.0

model = models.Sequential()
model.add(layers.Conv2D(64,(3,3), activation = 'relu', input_shape =(64,64)))
model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Conv2D(128, (3,3), activation = 'relu'))
model.add(layers.MaxPooling2D(pool_size=(2,2)))
model.add(layers.Conv2D(128, (3,3), activation = 'relu'))

model.add(layers.Flatten())
model.add(layers.Dense(64, activation = 'relu'))
model.add(layers.Dense(3))

model.compile(optimizer = 'adam',
            loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics = ['accuracy'])
model.fit(x_train, y_train)

history = model.fit(trainImages, trainLabels, epochs = 2,
                    validation_data=(testImages, testLabels))

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()

testLoss, testAcc = model.evaluate(testImages,  testLabels, verbose=2)

print(testAcc)