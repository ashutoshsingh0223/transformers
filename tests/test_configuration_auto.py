# coding=utf-8
# Copyright 2019-present, the HuggingFace Inc. team.
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

import os
import unittest

from transformers.configuration_auto import AutoConfig
from transformers.configuration_bert import BertConfig
from transformers.configuration_roberta import RobertaConfig


SAMPLE_ROBERTA_CONFIG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures/dummy-config.json")


class AutoConfigTest(unittest.TestCase):
    def test_config_from_model_shortcut(self):
        config = AutoConfig.from_pretrained("bert-base-uncased")
        self.assertIsInstance(config, BertConfig)

    def test_config_from_model_type(self):
        config = AutoConfig.from_pretrained(SAMPLE_ROBERTA_CONFIG)
        self.assertIsInstance(config, RobertaConfig)

    def test_config_for_model_str(self):
        config = AutoConfig.for_model("roberta")
        self.assertIsInstance(config, RobertaConfig)