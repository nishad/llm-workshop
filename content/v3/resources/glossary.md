---
title: Glossary
weight: 2
---

Short, model-agnostic definitions. Model names, sizes and speeds are on the [Model guide](/v3/resources/models).

## Core terms

**Token.** A piece of text, often a word or part of a word, that a model reads and writes. Costs and limits are counted in tokens, not characters.

**Context window.** The maximum number of tokens a model can consider at once, prompt and answer together. Text beyond it is cut off or causes an error.

**Parameters.** The learned numbers inside a model. More parameters usually mean better quality and a larger file.

**Quantization.** Storing a model's numbers at lower precision to shrink the file and speed it up. Labels such as Q4_K_M (about 4 bits) and Q8_0 (8 bits) name the scheme.

**Temperature.** A setting that controls how random the output is. Low values give steadier answers, high values give more varied ones.

**Seed.** A number that fixes the random choices during generation. The same seed, prompt and settings can reproduce an answer.

**System prompt.** Instructions placed before the conversation that set the model's role and rules. The user normally does not see them.

## Search and retrieval

**Embedding.** A list of numbers that represents the meaning of a text. Similar meanings give similar lists.

**Embedding model.** A model that produces embeddings instead of prose. It is separate from the chat model.

**Cosine similarity.** A score from -1 to 1 for how closely two embeddings point in the same direction. Higher means more similar.

**Vector index.** A store of embeddings that finds the nearest ones to a query quickly. A plain list searched in full also works for small collections.

**Chunk.** A piece of a longer document, cut to fit the context window. Each chunk is embedded and retrieved on its own.

**Retrieval-augmented generation (RAG).** Fetching relevant passages first and giving them to the model with the question. The answer is then based on your documents.

**Grounding.** Tying an answer to supplied sources instead of the model's memory. A grounded answer can be checked against those sources.

**Citation.** A pointer from a statement to the passage that supports it. In RAG it names the chunk the answer came from.

**Hallucination.** Fluent output that is wrong or invented, such as an identifier that does not exist. Checking and review are the defense.

## Structured work

**Structured output.** A model answer constrained to a fixed format, usually JSON. It makes results machine-readable.

**JSON schema.** A description of the allowed fields, types and values of a JSON document. A server can use it to force valid output.

**Pydantic.** A Python library that defines data shapes as classes and checks data against them. The notebooks use it to validate model output.

**Validation.** Checking that output has the right shape and plausible values. Valid JSON can still contain a wrong value.

**Tool use (function calling).** The model asks the program to run a function, and the result goes back to the model. The program, not the model, performs the call.

**Human in the loop.** A person reviews or approves the model's output or actions. It is how errors are caught before they reach a catalog.

## Library terms

**SPARQL endpoint.** A web service that answers queries written in SPARQL against linked data. Wikidata and many library services offer one.

**Authority file (GND, VIAF, LCNAF).** A maintained list of unique identifiers for people, places, organizations and subjects. GND is German, LCNAF is the Library of Congress name file, and VIAF links authority files from many countries.

**Controlled vocabulary.** An agreed list of terms used to describe things consistently. Thesauri and subject heading lists are controlled vocabularies.

**SKOS.** A web standard for publishing thesauri and vocabularies as linked data. It defines preferred labels, alternative labels and broader and narrower relations.

**Reconciliation.** Matching a string such as a name to the identifier of the right entity in an authority file. Tools usually propose candidates and a person confirms.

## Openness and licensing

**Open weights.** The trained parameters can be downloaded and run. The license may still restrict use, and data and code may be closed.

**Open source (OSI).** Software or a model whose license meets the Open Source Initiative's definition, which grants the freedom to use, study, modify and share it. Open weights alone do not meet it.

**Fully open.** Weights, training code, and the training data or a way to rebuild it are all available, along with intermediate checkpoints. Others can inspect and reproduce the work.

**License.** The legal terms that say what you may do with a model or dataset. Read it before reuse.

**Acceptable use policy.** Rules about permitted uses that come with a model in addition to its license. They can bind redistributors as well as users.

**Training data.** The text a model learned from. Its sources and licenses affect trust and legal risk.

**Provenance.** The documented origin of data or a model, including where it came from and what changed. Libraries already record it for their own collections.

**Reproducibility.** The ability to get the same result again from the same inputs and settings. Releasing data, code and checkpoints makes it possible.

**Model card.** A document that describes a model's purpose, training, limits and license. Read it before relying on a model.

## Software and formats

**GGUF.** A single-file format for quantized models used by llama.cpp and tools built on it. It holds the weights and metadata.

**Hugging Face.** A website that hosts models, datasets and their documentation. Most open models are published there first.

**Ollama.** A program that downloads and runs models locally, with a command line and a local server. Part 2 uses it.

**LM Studio.** A graphical desktop application for running models locally. It can also serve them over a local API.

**llama.cpp.** An open C++ engine for running quantized models on ordinary hardware. Ollama and LM Studio are built on it.

**MLX.** Apple's machine learning framework for Apple Silicon. Some runtimes use it instead of llama.cpp.

**KV cache.** Memory that stores intermediate results for every token in the context. It grows with the context window and takes RAM beyond the model file.

**`num_ctx`.** The Ollama setting for the context window size in tokens. A larger value uses more memory.

**Thinking model.** A model that writes out reasoning steps before its answer. It is slower and may need that mode switched off for structured output.

**Digest.** A hash that identifies the exact contents of a downloaded model; `ollama list` shows its first 12 characters. Two tags with the same digest are the same model.

## Units

| Unit | Meaning |
|---|---|
| B | Billions of parameters, as in 8B |
| GB | Gigabytes; file sizes and memory |
| k | Thousand, as in a 4k context window of about 4,000 tokens; strictly 4,096 |
| KiB, GiB | Binary units used for context memory; 1 GiB is about 1.07 GB |
| ms | Milliseconds; one thousandth of a second |
| Tokens per second | Generation speed; higher is faster |
