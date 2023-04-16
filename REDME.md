This is a tutorial to deploy a machine learning algorithm using FastAPI.

1- First step is to download the pre-trained model 

2- It is a best practice to define models settings in a config file, this is usefull when your app usese diffrent models or diffrent configurations or versions of a same model.

3- To use the downloaded pre-trained model we should create a class that inherits frpm PyTorch nn.Module class. nn.Module class is the base class for all neural networks in PyTorch