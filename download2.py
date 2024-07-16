import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
import os
#model_dir = snapshot_download('qwen/Qwen-7B-Chat', cache_dir='/root/autodl-tmp', revision='master')
#model_dir = snapshot_download('ZhipuAI/chatglm3-6b-128k', cache_dir='/root/autodl-tmp', revision='master')
model_dir = snapshot_download('qwen/Qwen1.5-7B-Chat', cache_dir='/root/autodl-tmp', revision='master')
