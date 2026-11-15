---
title: Glossary
weight: 2
---

Short definitions that do not depend on any one model. Model names, sizes and speeds are on the [Model guide](/v3/resources/models).

## Core terms

**Token.** A piece of text, often a word or part of a word, that a model reads and writes. Costs and limits are counted in tokens, not characters.

**Context window.** The maximum number of tokens a model can consider at once, prompt and answer together. Text beyond it is cut off or causes an error.

**Parameters.** The learned numbers inside a model, also called weights. More parameters usually mean better quality and a larger file.

**Quantization.** Storing a model's numbers with less precision, so the file is smaller and the model runs faster. Labels such as Q4_K_M (about 4 bits) and Q8_0 (8 bits) name the method used.

**Temperature.** A setting that controls how random the output is. Low values give steadier answers, high values give more varied ones.

**Seed.** A number that fixes the random choices during generation. The same seed, prompt and settings can reproduce an answer.

**System prompt.** Instructions placed before the conversation that set the model's role and rules. The user normally does not see them.

**Tier.** On this site, either a hardware tier (a machine with 16 GB of memory or more runs the 8B model, an 8 GB machine runs the 4B) or one of the three exercise levels (GUI, Run and change, Stretch). The openness ladder in Part 1 also numbers its levels as tiers 0 to 3.

## Search and retrieval

**Embedding.** A list of numbers that represents the meaning of a text. Similar meanings give similar lists.

**Embedding model.** A model that produces embeddings instead of prose. It is separate from the chat model.

**Cosine similarity.** A score from -1 to 1 for how closely two embeddings point in the same direction. Higher means more similar.

**Vector index.** A store of embeddings that finds the nearest ones to a query quickly. A plain list searched in full also works for small collections.

**Chunk.** A piece of a longer document, cut to fit the context window. Each chunk is embedded and retrieved on its own.

**Retrieval-augmented generation (RAG).** Fetching relevant passages first and giving them to the model with the question. The answer is then based on your documents.

**Fine-tuning.** Training an existing model further on your own examples, which changes the model itself. RAG instead gives the model your documents at question time and leaves the model unchanged.

**Grounding.** Tying an answer to supplied sources instead of the model's memory. A grounded answer can be checked against those sources.

**Citation.** A pointer from a statement to the passage that supports it. In RAG it names the chunk the answer came from.

**Hallucination.** Fluent output that is wrong or invented, such as an identifier that does not exist. The protection is to check and review the output.

## Structured work

**JSON.** A plain-text format for data: named fields and their values inside curly braces. Programs read and write it directly.

**Structured output.** A model answer that must follow a fixed format, usually JSON (a plain-text data format). A program can then read the result directly.

**JSON schema.** A description of the allowed fields, types and values of a JSON document. A server can use it to force valid output.

**Grammar-enforced output.** The server restricts the model at each step to tokens that keep the output valid against the schema, so the result is always well-formed JSON. A well-formed answer can still hold a wrong value.

**Pydantic.** A Python library that defines data shapes as classes and checks data against them. The notebooks use it to validate model output.

**Validation.** Checking that output has the right shape and plausible values. Valid JSON can still contain a wrong value.

**Tool use (function calling).** The model asks the program to run a function, and the result goes back to the model. The program, not the model, performs the call.

**Human in the loop.** A person reviews or approves the model's output or actions. It is how errors are caught before they reach a catalog.

**Gold file (gold set).** A file with the known correct answers for a set of inputs. The notebooks compare the model's output with it to measure accuracy and recall.

**Fixture.** A recorded answer from a web service, saved in the notebooks repository. The tools use it when the live service cannot be reached and mark the result with `"fixture": true`; treat such results as examples, not live data.

## Library terms

**SPARQL endpoint.** A web service that answers queries written in SPARQL, the query language for linked data. Wikidata and many library services offer one.

**Authority file (GND, VIAF, LCNAF).** A maintained list of unique identifiers for people, places, organizations and subjects. GND is German, LCNAF is the Library of Congress name file, and VIAF links authority files from many countries.

**Controlled vocabulary.** An agreed list of terms used to describe things consistently. Thesauri and subject heading lists are controlled vocabularies.

**SKOS.** A web standard for publishing thesauri and vocabularies as linked data. It defines preferred labels, alternative labels and broader and narrower relations.

**Reconciliation.** Matching a piece of text, such as a name, to the identifier of the right entity in an authority file. Tools usually propose candidates and a person confirms.

## Openness and licensing

**Open weights.** The trained parameters can be downloaded and run. The license may still restrict use, and data and code may be closed.

**Open source (OSI).** Software or a model whose license meets the Open Source Initiative's definition. That definition says anyone must be free to use, study, modify and share the work. Open weights alone do not meet it.

**Fully open.** The weights, the training code and the training data (or a way to rebuild it) are all available. So are intermediate checkpoints (versions of the model saved during training). Others can inspect and reproduce the work. On the [openness ladder](/v3/part1/02-open-models/openness-ladder) this is tier 3.

**License.** The legal terms that say what you may do with a model or dataset. Read it before reuse.

**Acceptable use policy.** Rules about permitted uses that come with a model in addition to its license. They can apply to people who pass the model on, as well as to those who use it.

**Training data.** The text a model learned from. Its sources and licenses affect trust and legal risk.

**Provenance.** The documented origin of data or a model, including where it came from and what changed. Libraries already record it for their own collections.

**Reproducibility.** The ability to get the same result again from the same inputs and settings. Releasing data, code and checkpoints makes it possible.

**Model card.** A document that describes a model's purpose, training, limits and license. Read it before relying on a model.

## Software and formats

**GGUF.** A single-file format for quantized models used by llama.cpp and tools built on it. It holds the weights and metadata.

**Hugging Face.** A website that hosts models, datasets and their documentation. Most open models are published there first.

**Runtime.** The program that loads a model file and runs it on your computer. Ollama and LM Studio are the two runtimes used in this workshop; both use llama.cpp underneath.

**Ollama.** A program that downloads and runs models locally, with a command line and a local server. Part 2 uses it.

**Model tag.** The name you give Ollama to download or run a model, for example `thalhath/apertus:8b`: the publisher, the model name and, after the colon, the size or version. Always use the full tag.

**LM Studio.** A graphical desktop application for running models locally. It can also run a local server, so that other programs on your computer can use the models.

**llama.cpp.** An open C++ engine for running quantized models on ordinary hardware. Ollama and LM Studio are built on it.

**MLX.** Apple's machine learning framework for Apple Silicon. Some programs that run models use it instead of llama.cpp.

**KV cache.** Memory that stores intermediate results for every token in the context. It grows with the context window and adds to the memory that the model file already uses.

**`num_ctx`.** The Ollama setting for the context window size in tokens. A larger value uses more memory.

**Thinking model.** A model that writes out reasoning steps before its answer. It is slower, and you may need to switch that mode off for structured output.

**Digest.** A hash (a code computed from the model's contents) that identifies the exact model you downloaded; `ollama list` shows its first 12 characters. Two tags with the same digest are the same model.

## Units

| Unit | Meaning |
|---|---|
| B | Billions of parameters, as in 8B |
| GB | Gigabytes; file sizes and memory |
| k | Thousand, as in a 4k context window of about 4,000 tokens; strictly 4,096 |
| KiB, GiB | Binary units used for context memory; 1 GiB is about 1.07 GB |
| ms | Milliseconds; one thousandth of a second |
| Tokens per second | Generation speed; higher is faster |
