This is a bluprint to deploy a **Mmachine Learning Model** using **FastAPI**.

**Table of content**
- [Features](#features)
- [Instruction](#instruction)
- [Docker Image](#docker-image)


# Features
- REST API
- Graceful Shout down



# Instruction
1- First step is to download the pre-trained model. It's a BERT-base-cased model that is fine tuned for sentiment detection.

2- It is a best practice to define models settings in a config file, this is usefull when your app usese diffrent models or diffrent configurations or versions of a same model.

3- To use the downloaded pre-trained model we should create a class that inherits frpm PyTorch nn.Module class. nn.Module class is the base class for all neural networks in PyTorch

# Docker Image