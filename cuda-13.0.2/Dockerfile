FROM nvidia/cuda:13.0.2-cudnn-devel-ubuntu24.04

RUN apt-get update && apt-get install -y --no-install-recommends vim tmux curl wget && apt-get clean

RUN curl -LsSf https://astral.sh/uv/install.sh | sh