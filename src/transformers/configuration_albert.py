# coding=utf-8
# Copyright 2018 The Google AI Language Team Authors and The HuggingFace Inc. team.
# Copyright (c) 2018, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" ALBERT model configuration """

from .configuration_utils import PretrainedConfig


ALBERT_PRETRAINED_CONFIG_ARCHIVE_MAP = {
    "albert-base-v1": "https://s3.amazonaws.com/models.huggingface.co/bert/albert-base-config.json",
    "albert-large-v1": "https://s3.amazonaws.com/models.huggingface.co/bert/albert-large-config.json",
    "albert-xlarge-v1": "https://s3.amazonaws.com/models.huggingface.co/bert/albert-xlarge-config.json",
    "albert-xxlarge-v1": "https://s3.amazonaws.com/models.huggingface.co/bert/albert-xxlarge-config.json",
    "albert-base-v2": "https://s3.amazonaws.com/models.huggingface.co/bert/albert-base-v2-config.json",
    "albert-large-v2": "https://s3.amazonaws.com/models.huggingface.co/bert/albert-large-v2-config.json",
    "albert-xlarge-v2": "https://s3.amazonaws.com/models.huggingface.co/bert/albert-xlarge-v2-config.json",
    "albert-xxlarge-v2": "https://s3.amazonaws.com/models.huggingface.co/bert/albert-xxlarge-v2-config.json",
}


class AlbertConfig(PretrainedConfig):
    r"""
        This is the configuration class to store the configuration of an :class:`~transformers.AlbertModel`.
        It is used to instantiate an ALBERT model according to the specified arguments, defining the model
        architecture. Instantiating a configuration with the defaults will yield a similar configuration to that of
        the ALBERT xxlarge architecture.

        Configuration objects inherit from  :class:`~transformers.PretrainedConfig` and can be used
        to control the model outputs. Read the documentation from  :class:`~transformers.PretrainedConfig`
        for more information.


        Args:
            vocab_size (:obj:`int`, optional, defaults to 30000):
                Vocabulary size of the ALBERT model. Defines the different tokens that
                can be represented by the `inputs_ids` passed to the forward method of :class:`~transformers.AlbertModel`.
            embedding_size (:obj:`int`, optional, defaults to 128):
                Size of vocabulary embeddings.
            hidden_size (:obj:`int`, optional, defaults to 4096):
                Size of the encoder layers and the pooler layer.
            num_hidden_layers (:obj:`int`, optional, defaults to 12):
                Number of hidden layers in the Transformer encoder.
            num_hidden_groups (:obj:`int`, optional, defaults to 1):
                Number of groups for the hidden layers, parameters in the same group are shared.
            num_attention_heads (:obj:`int`, optional, defaults to 64):
                Number of attention heads for each attention layer in the Transformer encoder.
            intermediate_size (:obj:`int`, optional, defaults to 16384):
                The size of the "intermediate" (i.e., feed-forward) layer in the Transformer encoder.
            inner_group_num (:obj:`int`, optional, defaults to 1):
                The number of inner repetition of attention and ffn.
            hidden_act (:obj:`str` or :obj:`function`, optional, defaults to "gelu_new"):
                The non-linear activation function (function or string) in the encoder and pooler.
                If string, "gelu", "relu", "swish" and "gelu_new" are supported.
            hidden_dropout_prob (:obj:`float`, optional, defaults to 0):
                The dropout probability for all fully connected layers in the embeddings, encoder, and pooler.
            attention_probs_dropout_prob (:obj:`float`, optional, defaults to 0):
                The dropout ratio for the attention probabilities.
            max_position_embeddings (:obj:`int`, optional, defaults to 512):
                The maximum sequence length that this model might ever be used with. Typically set this to something
                large (e.g., 512 or 1024 or 2048).
            type_vocab_size (:obj:`int`, optional, defaults to 2):
                The vocabulary size of the `token_type_ids` passed into :class:`~transformers.AlbertModel`.
            initializer_range (:obj:`float`, optional, defaults to 0.02):
                The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
            layer_norm_eps (:obj:`float`, optional, defaults to 1e-12):
                The epsilon used by the layer normalization layers.

        Example::

            # Initializing an ALBERT-xxlarge style configuration
            albert_xxlarge_configuration = AlbertConfig()

            # Initializing an ALBERT-base style configuration
            albert_base_configuration = AlbertConfig(
                hidden_size=768,
                num_attention_heads=12,
                intermediate_size=3072,
            )

            # Initializing a model from the ALBERT-base style configuration
            model = AlbertModel(bert_base_configuration)

            # Accessing the model configuration
            configuration = model.config

        Attributes:
            pretrained_config_archive_map (Dict[str, str]):
                A dictionary containing all the available pre-trained checkpoints.
    """

    pretrained_config_archive_map = ALBERT_PRETRAINED_CONFIG_ARCHIVE_MAP

    def __init__(
        self,
        vocab_size_or_config_json_file=30000,
        embedding_size=128,
        hidden_size=4096,
        num_hidden_layers=12,
        num_hidden_groups=1,
        num_attention_heads=64,
        intermediate_size=16384,
        inner_group_num=1,
        hidden_act="gelu_new",
        hidden_dropout_prob=0,
        attention_probs_dropout_prob=0,
        max_position_embeddings=512,
        type_vocab_size=2,
        initializer_range=0.02,
        layer_norm_eps=1e-12,
        **kwargs
    ):
        super(AlbertConfig, self).__init__(**kwargs)

        self.vocab_size = vocab_size_or_config_json_file
        self.embedding_size = embedding_size
        self.hidden_size = hidden_size
        self.num_hidden_layers = num_hidden_layers
        self.num_hidden_groups = num_hidden_groups
        self.num_attention_heads = num_attention_heads
        self.inner_group_num = inner_group_num
        self.hidden_act = hidden_act
        self.intermediate_size = intermediate_size
        self.hidden_dropout_prob = hidden_dropout_prob
        self.attention_probs_dropout_prob = attention_probs_dropout_prob
        self.max_position_embeddings = max_position_embeddings
        self.type_vocab_size = type_vocab_size
        self.initializer_range = initializer_range
        self.layer_norm_eps = layer_norm_eps
