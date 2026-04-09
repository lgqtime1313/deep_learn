def main():
    print("Hello from lvgq-d2l-zh!")


if __name__ == "__main__":
    main()

'''
nvidia-smi  查看GPU
创建环境 conda create -n torch_env python=3.11 -y
激活环境 
conda init bash
source ~/.bashrc
conda activate torch_env  
安装环境 ... GPU版本
激活内核 python -m ipykernel install --user --name=torch_env --display-name="Python (torch_env)"
jupyterlab重启内核
'''
# # 1. 创建一个专门跑 pytorch 的环境（名字叫 torch_env）
# conda create -n torch_env python=3.11 -y
#  conda init bash
#  source ~/.bashrc
# # 2. 激活环境
# conda activate torch_env
#
# # 3. 安装 pytorch + torchvision（你要的 0.19.0 版本）
# conda install pytorch==2.4.0 torchvision==0.19.0 cpuonly -c pytorch -c conda-forge -y
# pip install d2l


# # 1. 卸载旧的 CPU 版 PyTorch
# conda remove -y pytorch torchvision torchaudio cpuonly
#
# # 2. 安装 GPU 版（CUDA 11.8，兼容性最强，99%服务器都能用）
# conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=11.8 -c pytorch -c nvidia -y

# 安装内核库
# conda install ipykernel -y
# python -m ipykernel install --user --name=torch_env --display-name="Python (torch_env)" 注册内核

'''
# 1. 卸载旧的 CPU 版 PyTorch
conda remove -y pytorch torchvision torchaudio cpuonly

# 2. 安装 GPU 版（CUDA 11.8，兼容性最强，99%服务器都能用）
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 
'''
'''
import torch
from d2l import torch as d2l

print("GPU 可用：", torch.cuda.is_available())
print("torch 版本：", torch.__version__)
print("torchvision 版本：", torchvision.__version__)
print("✅ 环境完全正常！")
'''