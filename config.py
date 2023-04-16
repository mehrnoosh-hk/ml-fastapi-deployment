"""This model reads and classify the configuration"""

import yaml
from pydantic import BaseModel
from typing import Union
import pathlib


def get_config(file_path: Union[str, pathlib.Path]) -> dict:
    with open(file=file_path, mode="r", encoding="UTF-8") as f:
        config = yaml.safe_load(f)
    return config


class BERTModelConfig(BaseModel):
    """
    Represent basic configuration of BERT model
    """
    BERT_MODEL: str
    PRE_TRAINED_MODEL: str
    CLASS_NAMES: list[str]
    MAX_SEQUENCE_LEN: int


def load_to_object(cls: type,  config: dict):
    cls_name = cls.__name__
    cls_dict = config[cls_name]
    p = cls(**cls_dict)
    return p


print(load_to_object(BERTModelConfig, get_config("config.yml")))
