# Example vLLM deployment command

python -m vllm.entrypoints.openai.api_server \
  --model Qwen/Qwen2.5-7B-Instruct \
  --dtype float16 \
  --gpu-memory-utilization 0.9 \
  --host 0.0.0.0 \
  --port 32000
