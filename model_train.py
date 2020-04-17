#compile and train model

model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

history = model.fit(imtrain, labtrain, epochs=20, validation_data=(imtest, labtest))