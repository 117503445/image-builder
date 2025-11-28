import os
os.environ["CUDA_VISIBLE_DEVICES"] = ""

# 使用huggingface_hub下载模型
from huggingface_hub import snapshot_download

print("开始下载模型...")
model_name = "tencent/HunyuanOCR"
local_dir = "/models/HunyuanOCR"

print(f"下载模型到 {local_dir}...")
snapshot_download(
    repo_id=model_name,
    local_dir=local_dir,
    local_dir_use_symlinks=False
)

print("模型下载完成！")