#!/bin/bash

vllm serve /models/HunyuanOCR \
    --host 0.0.0.0 \
    --port 8000 \
    --no-enable-prefix-caching \
    --mm-processor-cache-gb 0