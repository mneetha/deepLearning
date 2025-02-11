import warnings
import numpy as np
import matplotlib.pyplot as plt
import os
import math
import shutil
import random
from keras.layers import Conv2D, MaxPool2D, Dropout, Flatten, Dense, BatchNormalization, GlobalAvgPool2D
from keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import keras
from keras.callbacks import ModelCheckpoint, EarlyStopping
h5 = model.fit(train_images, train_labels, epochs=10, batch_size=32, validation_data=(val_images, val_labels), callbacks=cd) #Example: 10 epochs


ROOT_DIR = "/path_to/brain_tumor_dataset"
no_images = {}
for dir in os.listdir(ROOT_DIR):
  no_images[dir] = len(os.listdir(os.path.join(ROOT_DIR, dir)))
no_images.items()
warnings.filterwarnings("ignore")

def split_data(root_dir, train_ratio=0.7, val_ratio=0.15, test_ratio=0.15):
    if train_ratio + val_ratio + test_ratio != 1.0:
        raise ValueError("Ratios must sum to 1.0")

    train_data = []
    val_data = []
    test_data = []

    for dir_name in os.listdir(root_dir):
        dir_path = os.path.join(root_dir, dir_name)
        if os.path.isdir(dir_path):
            file_names = os.listdir(dir_path)
            random.shuffle(file_names)  # Shuffle files for random split
            num_files = len(file_names)

            train_split = int(math.floor(train_ratio * num_files))
            val_split = int(math.floor((train_ratio + val_ratio) * num_files))

            train_data.extend([(os.path.join(dir_path, file_name), dir_name) for file_name in file_names[:train_split]])
            val_data.extend([(os.path.join(dir_path, file_name), dir_name) for file_name in file_names[train_split:val_split]])
            test_data.extend([(os.path.join(dir_path, file_name), dir_name) for file_name in file_names[val_split:]])

    return train_data, val_data, test_data


#Preparing our data using Data Generator
def preprocessImages(data, image_data=None):
  if image_data is None:
    image_data = ImageDataGenerator(rescale=1./255)
  images = []
  labels = []
  for img_path, label in data:
      img = load_img(img_path, target_size=(224, 224))
      img_array = img_to_array(img)
      img_array = img_array / 255.0 # Rescale here as well
      images.append(img_array)
      labels.append(1 if label == 'yes' else 0)  # Assuming 'yes' is the positive class

  # Convert lists to numpy arrays
  images = np.array(images)
  labels = np.array(labels)

  return images, labels

# Example usage:
train_set, val_set, test_set = split_data(ROOT_DIR)

print("Training set size:", len(train_set))
print("Validation set size:", len(val_set))
print("Testing set size:", len(test_set))

#CNN model

model = Sequential()
model.add(Conv2D(filters=16, kernel_size=(3, 3), activation='relu', input_shape=(224, 224, 3)))

model.add(Conv2D(filters=36, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Conv2D(filters=128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Dropout(rate=0.25))

model.add(Flatten())
model.add(Dense(units=64, activation='relu'))

model.add(Dropout(rate=0.25))

model.add(Dense(units=1, activation='sigmoid'))
# model.summary()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Example usage (replace with your actual data)
test_image_data = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)
train_images, train_labels = preprocessImages(train_set, image_data=test_image_data)
test_images, test_labels = preprocessImages(test_set)
val_images, val_labels = preprocessImages(val_set)



es = EarlyStopping(monitor='val_accuracy', min_delta=0.01, patience=3, verbose=1, mode='auto')
mc = ModelCheckpoint(filepath ='bestmodel.h5', monitor='val_accuracy', verbose=1, save_best_only=True, save_weights_only=False, mode='auto', save_freq=1)

cd = [es, mc]