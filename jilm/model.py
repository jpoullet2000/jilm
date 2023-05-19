"""Defines the model for the JILM application."""
from typing import Dict, Any, Optional, List
from pydantic import Field
from functools import partial
from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from langchain.callbacks.manager import CallbackManagerForLLMRun
from jilm.settings import llm_model


def new_text_callback(text):
    print(text, end="")


class JILMLangModel(LLM):
    """JILM language model."""

    n_ctx: int = Field(512, alias="n_ctx")
    """Token context window."""

    n_parts: int = Field(-1, alias="n_parts")
    """Number of parts to split the model into.
    If -1, the number of parts is automatically determined."""

    seed: int = Field(0, alias="seed")
    """Seed. If -1, a random seed is used."""

    f16_kv: bool = Field(False, alias="f16_kv")
    """Use half-precision for key/value cache."""

    logits_all: bool = Field(False, alias="logits_all")
    """Return logits for all tokens, not just the last token."""

    vocab_only: bool = Field(False, alias="vocab_only")
    """Only load the vocabulary, no weights."""

    use_mlock: bool = Field(False, alias="use_mlock")
    """Force system to keep model in RAM."""

    embedding: bool = Field(False, alias="embedding")
    """Use embedding mode only."""

    n_threads: Optional[int] = Field(4, alias="n_threads")
    """Number of threads to use."""

    n_predict: Optional[int] = 256
    """The maximum number of tokens to generate."""

    temp: Optional[float] = 0.8
    """The temperature to use for sampling."""

    top_p: Optional[float] = 0.95
    """The top-p value to use for sampling."""

    top_k: Optional[int] = 40
    """The top-k value to use for sampling."""

    echo: Optional[bool] = False
    """Whether to echo the prompt."""

    stop: Optional[List[str]] = None
    """A list of strings to stop generation when encountered."""

    # repeat_last_n: Optional[int] = 64
    # "Last n tokens to penalize"

    # repeat_penalty: Optional[float] = 1.3
    # """The penalty to apply to repeated tokens."""

    n_batch: int = Field(1, alias="n_batch")
    """Batch size for prompt processing."""

    streaming: bool = False
    """Whether to stream the results or not."""

    client: Any = None  #: :meta private:

    def _call(self, prompt: str, stop: Optional[List[str]] = None, run_manager: Optional[CallbackManagerForLLMRun] = None) -> str:
        if run_manager:
            text_callback = partial(run_manager.on_llm_new_token, verbose=self.verbose)
            #text = self.client.generate(
            text = llm_model.generate(
                prompt,
                new_text_callback=text_callback,
                **self._default_params,
            )
        else:
            text = llm_model.generate(prompt=prompt, **self._default_params)
            # text = self.client.generate(prompt, **self._default_params)
        #if stop is not None:
        if self.stop is not None:
            print("Enforcing stop tokens:", self.stop)
            text = enforce_stop_tokens(text, self.stop)
        return text
        # return llm_model.generate(
            # prompt, n_predict=self.n_predict, new_text_callback=new_text_callback
        # )

    def _llm_type(self) -> str:
        return "GPT4j"

    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the identifying parameters."""
        return {
            "seed": self.seed,
            "n_predict": self.n_predict,
            "n_threads": self.n_threads,
            "n_batch": self.n_batch,
            # "repeat_last_n": self.repeat_last_n,
            # "repeat_penalty": self.repeat_penalty,
            "top_k": self.top_k,
            "top_p": self.top_p,
            "temp": self.temp,
        }

