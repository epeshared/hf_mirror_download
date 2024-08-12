import os

def download_model(model_name, local_dir):
    # 设置环境变量
    os.environ['HF_ENDPOINT'] = 'https://hf-mirror.com'
    
    # 下载模型
    command = f'huggingface-cli download --resume-download {model_name} --local-dir {local_dir}'
    os.system(command)

def download_models_from_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            model_name, local_dir = line.strip().split()
            download_model(model_name, local_dir)

if __name__ == "__main__":
    # 假设文件名为 models_to_download.txt
    file_path = 'models_to_download.txt'
    download_models_from_file(file_path)
