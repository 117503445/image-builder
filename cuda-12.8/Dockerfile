FROM docker.io/nvidia/cuda:12.8.0-cudnn-devel-ubuntu24.04

RUN apt-get update && apt-get install -y --no-install-recommends vim tmux curl && apt-get clean

COPY ustc.ubuntu24.sources.list /etc/apt/sources.list