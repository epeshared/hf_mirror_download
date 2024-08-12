import os
# 设置环境变量
os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
# 下载模型
#os.system('huggingface-cli download --resume-download sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2 --local-dir /home/xtang/models/embedding_model')
#os.system('huggingface-cli download --resume-download BAAI/bge-large-zh-v1.5 --local-dir /home/xtang/models/BAAI/bge-large-zh-v1.5')
#os.system('huggingface-cli download --resume-download BAAI/bge-reranker-large --local-dir /home/xtang/models/BAAI/bge-reranker-large')
os.system('huggingface-cli download --resume-download BAAI/bge-large-en-v1.5 --local-dir /home/xtang/models/BAAI/bge-large-en-v1.5')
