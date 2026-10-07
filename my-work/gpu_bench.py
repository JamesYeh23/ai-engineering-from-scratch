import time
import torch

size = 5000
a = torch.randn(size, size)
b = torch.randn(size, size)

start = time.time()
c = a @ b                      # @ means matrix multiply
cpu_time = time.time() - start
print(f"CPU: {cpu_time:.3f}s")

device = "mps"                # 1. which device name for your Mac?
a_gpu = a.to(device)           #    copy the grids over to the GPU
b_gpu = b.to(device)
torch.mps.synchronize()       # 2. wait until the copy has finished

c_gpu = a_gpu @ b_gpu
torch.mps.synchronize()  
start = time.time()
c_gpu = a_gpu @ b_gpu            # 3. multiply which two grids?
torch.mps.synchronize()       # 4. (same as 2)
gpu_time = time.time() - start
print(f"GPU: {gpu_time:.3f}s")
print(f"Speedup: {cpu_time / gpu_time:.1f}x")