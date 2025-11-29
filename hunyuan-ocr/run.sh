#!/bin/bash
export LD_LIBRARY_PATH=/usr/local/cuda-12.9/compat:$LD_LIBRARY_PATH
vllm serve /models/HunyuanOCR \
    --host 0.0.0.0 \
    --port 8000 \
    --no-enable-prefix-caching \
    --mm-processor-cache-gb 0