FROM vllm/vllm-openai:nightly-316c8492bf4d5fca8f9f8ea6f8ef1d76a0cb940f

RUN mkdir -p /models /code

# Set working directory
WORKDIR /code

# Copy application files
COPY run.sh /code/run.sh
COPY client.py /code/client.py

# Make run script executable
RUN chmod +x /code/run.sh

# Expose port for vLLM server
EXPOSE 8000

COPY download.py ./

# 在构建阶段下载模型
RUN python3 download.py

RUN apt-get update && apt-get install -y git curl wget

RUN pip install git+https://github.com/huggingface/transformers@82a06db03535c49aa987719ed0746a76093b1ec4

RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64/cuda-compat-12-9_575.57.08-0ubuntu1_amd64.deb && dpkg -i cuda-compat-12-9_575.57.08-0ubuntu1_amd64.deb && rm cuda-compat-12-9_575.57.08-0ubuntu1_amd64.deb

# Set default command
ENTRYPOINT ["/code/run.sh"]
