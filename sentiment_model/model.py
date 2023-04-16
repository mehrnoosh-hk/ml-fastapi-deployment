from transformers import BertModel, BertTokenizer
import torch.nn as nn
from config import bert_model_config


class SentimentAnalyzer(nn.Module):
    def __init__(self, n_classes: int):
        super().__init__()
        self.model: BertModel = BertModel.from_pretrained(
            bert_model_config.BERT_MODEL)
        # define dropout layer with a probability of 0.3 to prevent overfitting
        self.drop = nn.Dropout(p=0.3)
        # define a linear (fully connected) layer. This layer is used to produce the final output of the model, which is the sentiment class probabilities.
        self.out = nn.Linear(self.model.config.hidden_size, n_classes)

    def forward(self):
        pass
