import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam
# Example dataset: normalized sensor or log data (X_train normal)
X_train = normal_behavior_data
input_dim = X_train.shape[1]
# Autoencoder network
input_layer = Input(shape=(input_dim,))
encoded = Dense(32, activation='relu')(input_layer)
encoded = Dense(16, activation='relu')(encoded)
decoded = Dense(32, activation='relu')(encoded)
output_layer = Dense(input_dim, activation='sigmoid')(decoded)
autoencoder = Model(inputs=input_layer, outputs=output_layer)
autoencoder.compile(optimizer=Adam(), loss='mse')
# Train autoencoder on normal data
autoencoder.fit(X_train, X_train, epochs=50, batch_size=64, validation_split=0.1)
# Compute reconstruction error on test data
X_test = test_data
reconstructions = autoencoder.predict(X_test)
mse = np.mean(np.power(X_test - reconstructions, 2), axis=1)
# Threshold for anomaly detection
threshold = np.percentile(mse, 95)
anomalies = mse > threshold
print(f"Detected {np.sum(anomalies)} anomalies out of {len(anomalies)} samples.")
