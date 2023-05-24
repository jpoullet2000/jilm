# JILM

![JILM](images/jilm-logo.png)

Jilm enhances your AI capabilities.

## Installation

TO BE DONE

## Get started

First download a GPTj model, for instance `ggml-gpt4all-j-v1.3-groovy.bin` that can be installed [here](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin) for instance.

Then copy the `.env.template` file into `.env` and modify it.
Only the line with the model path should be modified:

```
JILM_LLM_MODEL_PATH="/path/to/ggml-gpt4all-j-v1.3-groovy.bin"
```

Start using JILM

```python
doc = DocumentLoader.load_single_document(data_folder / "paul_graham_essays_worked.txt")
splitter = TextSplitter()
docs = splitter.split([doc])
res = DocQuery("What does the author describe as good work?", docs=docs)
answer, docs = res.run()
```

The displayed result:
```
Question: What does the author describe as good work?
Helpful Answer: The author does not explicitly describe what constitutes good work in the given context. However, it can be inferred that good work is related to the core of the work, as it involves a significant contribution to the overall project. The author suggests that good work should at least be something close to the core of the work. The lack of specific examples in the given context may suggest that it is a difficult or subjective matter.<|endoftext|>
```
