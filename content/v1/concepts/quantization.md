---
title: Model Quantization
weight: 3
cascade:
  type: docs
sidebar:
  open: false
---

**Quantization in Large Language Models**

In machine learning and large language models (LLMs), quantization is the process of reducing the precision of the numbers (weights and activations) that a model uses during computations. This technique helps in making models smaller, faster, and more efficient, enabling them to run on devices with limited computational resources without significantly compromising performance.

**Think of it this way**

- Just as you might compress a high-resolution image to a smaller size for quicker loading times while retaining most of its visual quality, quantization compresses a model’s numerical precision to make it lighter and faster.

- Imagine working with large numbers and rounding them to the nearest whole number to simplify calculations. Quantization similarly simplifies the numbers in a model to speed up processing.

## Key Points about Quantization

1.	Reduced Model Size:
  - Quantization lowers the number of bits required to represent each parameter (e.g., from 32-bit floating-point to 8-bit integer).
	- This reduction leads to smaller model files, saving storage space and memory usage.
2.	Increased Computational Efficiency:
	- Lower-precision computations require less processing power.
	- Models run faster, making them more suitable for real-time applications.
3.	Minimal Impact on Performance:
	- Properly applied quantization maintains most of the model’s accuracy.
	- Advanced techniques aim to minimize the loss in performance due to reduced precision.
4.	Types of Quantization:
	- Uniform Quantization: Applies the same scale across all weights and activations.
	- Non-uniform Quantization: Uses different scales for different layers or parameters to preserve important details.
5.	Quantization Methods:
	- Post-Training Quantization: Quantize the model after it’s fully trained.
	- Quantization-Aware Training: Train the model with quantization in mind, allowing it to adjust and retain accuracy.

## Why Is Quantization Important in LLMs?

- Resource Constraints: LLMs can be enormous, making them difficult to deploy on devices with limited resources like smartphones or embedded systems.
- Energy Efficiency: Smaller models consume less power, which is crucial for battery-powered devices and large-scale data centers.
- Cost Reduction: Efficient models reduce computational costs, which is beneficial for both developers and users.

> Quantization is like simplifying a recipe by using measurements that are easier to work with (like cups instead of ounces) without changing how the final dish tastes. It makes the model’s calculations simpler and faster by using smaller numbers, helping it run efficiently on various devices.


Quantization plays a crucial role in making large language models more accessible and practical for everyday use. By reducing the precision of numerical representations within the model, we achieve a balance between efficiency and performance, enabling advanced AI applications to run smoothly even in resource-limited environments.

## Quantization labels in Ollama Models

These are some of the quantization labels used in Ollama models [^1]:

```yaml
- Q2_K: smallest, extreme quality loss - not recommended
- Q3_K: alias for Q3_K_M
- Q3_K_S: very small, very high quality loss
- Q3_K_M: very small, very high quality loss
- Q3_K_L: small, substantial quality loss
- Q4_K: alias for Q4_K_M
- Q4_K_S: small, significant quality loss
- Q4_K_M: medium, balanced quality - recommended
- Q5_K: alias for Q5_K_M
- Q5_K_S: large, low quality loss - recommended
- Q5_K_M: large, very low quality loss - recommended
- Q6_K: very large, extremely low quality loss
- Q8_0: very large, extremely low quality loss - not recommended
- F16: extremely large, virtually no quality loss - not recommended
- F32: absolutely huge, lossless - not recommended
```

[^1]: https://github.com/ollama/ollama/issues/1388#issuecomment-1841890505
