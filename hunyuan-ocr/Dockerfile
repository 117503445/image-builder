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

# Set default command
ENTRYPOINT ["/code/run.sh"]
