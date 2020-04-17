#data loader and normalizer


(imtrain, labtrain), (imtest, labtest) = datasets.cifar10.load_data()
#normalize pixel values
imtrain, imtest = imtrain / 255.0, imtest / 255.0

#labels do not inherently map to names, so we pre-define them to match a label vector
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer',
               'dog', 'frog', 'horse', 'ship', 'truck']

#check to see if GPU is available
print(tf.config.list_physical_devices('GPU'))