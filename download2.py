import torch
from modelscope import snapshot_download, AutoModel, AutoTokenizer
import os
#model_dir = snapshot_download('qwen/Qwen-7B-Chat', cache_dir='/root/autodl-tmp', revision='master')
#model_dir = snapshot_download('ZhipuAI/chatglm3-6b-128k', cache_dir='/root/autodl-tmp', revision='master')
#model_dir = snapshot_download('qwen/Qwen1.5-7B-Chat', cache_dir='/root/autodl-tmp', revision='master')
#model_dir = snapshot_download('Qwen/Qwen-VL', cache_dir='/home/xtang/models/', revision='master')
#model_dir = snapshot_download('BAAI/bge-large-zh-v1.5', cache_dir='/home/xtang/models/', revision='master')
model_dir = snapshot_download('Intel/bge-large-en-v1.5-rag-int8-static', cache_dir='/home/xtang/models/', revision='master')
#model_dir = snapshot_download('BAAI/bge-reranker-large', cache_dir='/home/xtang/models/', revision='master')
