import os
import argparse

def download_model(model_name, local_dir):
    # 设置环境变量
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
    
    # 下载模型
    command = f'huggingface-cli download --resume-download {model_name} --local-dir {local_dir}'
    os.system(command)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download models from Hugging Face.')
    parser.add_argument('model_name', type=str, help='The name of the model to download, e.g., BAAI/bge-large-zh-v1.5')
    parser.add_argument('local_dir', type=str, help='The local directory where the model should be saved.')

    args = parser.parse_args()
    download_model(args.model_name, args.local_dir)

