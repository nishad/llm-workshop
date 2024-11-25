---
title: Temperature in LLMs
weight: 5
cascade:
  type: docs
sidebar:
  open: false
---

In a Large Language Model, **temperature** is a parameter that controls the randomness or creativity of the model's outputs during text generation. It influences how likely the model is to produce less probable words, thereby affecting the diversity and originality of the generated text.

#### How Temperature Works

- **Mathematical Perspective:** Temperature modifies the probability distribution of the next word (token) predicted by the model. It does this by scaling the logits (raw output scores) before applying the softmax function to obtain probabilities.
- **Impact on Output:** A lower temperature makes the distribution sharper (less random), focusing on high-probability tokens. A higher temperature flattens the distribution (more random), giving lower-probability tokens a chance to be selected.

#### Low Temperature

- **Deterministic and Conservative Outputs:** With a low temperature (e.g., 0.2), the model tends to choose the most probable next word, resulting in predictable and consistent responses.
- **Sticking to Learned Patterns:** The model adheres closely to the data it was trained on, making it suitable for tasks requiring accuracy and reliability.
- **Use Cases:**
  - Factual question-answering
  - Formal writing
  - Technical documentation

#### High Temperature

- **Varied and Creative Outputs:** A high temperature (e.g., 1.0 or above) increases randomness, allowing the model to explore less probable words and generate unique responses.
- **Potential to Stray from Context:** While creativity is enhanced, the model might produce outputs that are less coherent or deviate from the intended topic.
- **Use Cases:**
  - Creative writing and storytelling
  - Brainstorming ideas
  - Poetry and artistic expression

#### Choosing the Right Temperature

- **Balance Between Predictability and Creativity:** Adjusting the temperature helps find the sweet spot that aligns with your specific needs.
- **Experimentation is Key:** Start with a default temperature (e.g., 0.7) and adjust based on the desired output.

#### Examples

- **Low Temperature (0.2):**
  - *Prompt:* "The capital of France is"
  - *Output:* "Paris."
  - *Explanation:* The model provides a direct and factual response.

- **High Temperature (1.0):**
  - *Prompt:* "The capital of France is"
  - *Output:* "a place where art, fashion, and history intertwine."
  - *Explanation:* The model offers a more creative and less direct response.

Temperature is a powerful tool in controlling the behavior of Large Language Models. By adjusting this parameter, you can tailor the model's outputs to be more predictable or more creative, depending on the requirements of your task. Understanding how temperature affects the model allows you to optimize its performance for a wide range of applications.
