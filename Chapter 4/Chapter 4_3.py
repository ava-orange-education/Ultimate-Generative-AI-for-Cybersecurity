import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense

X_train = np.random.rand(1000, 20)  # normal behavior data

input_layer = Input(shape=(20,))
encoded = Dense(10, activation='relu')(input_layer)
decoded = Dense(20, activation='sigmoid')(encoded)

autoencoder = Model(input_layer, decoded)
autoencoder.compile(optimizer='adam', loss='mse')
autoencoder.fit(X_train, X_train, epochs=20, batch_size=32)

X_test = np.random.rand(10, 20)  # test data
reconstruction = autoencoder.predict(X_test)
mse = np.mean(np.power(X_test - reconstruction, 2), axis=1)
print("Anomaly scores:", mse)
