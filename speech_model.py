# %load_ext autoreload
# %autoreload 2

from preprocess import *
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.models import load_model


# Second dimension of the feature is dim2
feature_dim_2 = 11

# # Save data to array file first
# save_data_to_array(max_len=feature_dim_2)

# # # Loading train set and test set
# X_train, X_test, y_train, y_test = get_train_test()

# # Feature dimension
feature_dim_1 = 20
channel = 1
epochs = 70
batch_size = 100
verbose = 1
num_classes = 10

# Reshaping to perform 2D convolution
# X_train = X_train.reshape(X_train.shape[0], feature_dim_1, feature_dim_2, channel)
# X_test = X_test.reshape(X_test.shape[0], feature_dim_1, feature_dim_2, channel)

# y_train_hot = to_categorical(y_train)
# y_test_hot = to_categorical(y_test)


def get_model():
    model = Sequential()
    model.add(Conv2D(32, kernel_size=(2, 2), activation='relu', input_shape=(feature_dim_1, feature_dim_2, channel)))
    model.add(Conv2D(48, kernel_size=(2, 2), activation='relu'))
    model.add(Conv2D(120, kernel_size=(2, 2), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.4))
    model.add(Dense(num_classes, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])
    return model

# Predicts one sample
def predict(filepath, model):
    sample = wav2mfcc(filepath)
    sample_reshaped = sample.reshape(1, feature_dim_1, feature_dim_2, channel)
    return get_labels()[0][
            np.argmax(model.predict(sample_reshaped))
    ]

# model = get_model()
# model.fit(X_train, y_train_hot, batch_size=batch_size, epochs=epochs, verbose=verbose, validation_data=(X_test, y_test_hot))

# model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
# # del model  # deletes the existing model

# returns a compiled model
# identical to the previous one
model = load_model('my_model.h5')

print(predict('./data/forward/0a2b400e_nohash_2.wav', model=model))