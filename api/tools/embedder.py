from typing import Optional

import adalflow as adal

from api.config import configs, get_embedder_type
from api.openai_client import OpenAIClient


def get_embedder(
    is_local_ollama: bool = False,
    use_google_embedder: bool = False,
    embedder_type: str = None,
    override_api_key: Optional[str] = None,
    override_base_url: Optional[str] = None,
    override_model: Optional[str] = None
) -> adal.Embedder:
    """Get embedder based on configuration or parameters.
    
    Args:
        is_local_ollama: Legacy parameter for Ollama embedder
        use_google_embedder: Legacy parameter for Google embedder  
        embedder_type: Direct specification of embedder type ('ollama', 'google', 'openai', 'custom_openai')
        override_api_key: Optional API key override for OpenAI-compatible embedders
        override_base_url: Optional base URL override for OpenAI-compatible embedders
        override_model: Optional embedding model override
    
    Returns:
        adal.Embedder: Configured embedder instance
    """
    # Determine which embedder config to use
    if embedder_type:
        if embedder_type == 'ollama':
            embedder_config = configs["embedder_ollama"]
        elif embedder_type == 'google':
            embedder_config = configs["embedder_google"]
        elif embedder_type == 'custom_openai':
            embedder_config = configs.get("embedder_custom_openai", configs["embedder"])
        else:  # default to openai
            embedder_config = configs["embedder"]
    elif is_local_ollama:
        embedder_config = configs["embedder_ollama"]
    elif use_google_embedder:
        embedder_config = configs["embedder_google"]
    else:
        # Auto-detect based on current configuration
        current_type = get_embedder_type()
        if current_type == 'ollama':
            embedder_config = configs["embedder_ollama"]
        elif current_type == 'google':
            embedder_config = configs["embedder_google"]
        elif current_type == 'custom_openai':
            embedder_config = configs.get("embedder_custom_openai", configs["embedder"])
        else:
            embedder_config = configs["embedder"]

    # --- Initialize Embedder ---
    model_client_class = embedder_config["model_client"]
    
    # Check if there are client_init_kwargs (for custom OpenAI embedders)
    client_init_kwargs = embedder_config.get("client_init_kwargs", {})
    
    model_client_kwargs = {}
    if "initialize_kwargs" in embedder_config:
        # Legacy support for initialize_kwargs
        model_client_kwargs = {**embedder_config["initialize_kwargs"]}
    elif client_init_kwargs:
        # Use client_init_kwargs for custom OpenAI embedders
        model_client_kwargs = {**client_init_kwargs}

    if model_client_class == OpenAIClient:
        if override_api_key:
            model_client_kwargs["api_key"] = override_api_key
        if override_base_url:
            model_client_kwargs["base_url"] = override_base_url

    if model_client_kwargs:
        model_client = model_client_class(**model_client_kwargs)
    else:
        model_client = model_client_class()
    
    # Create embedder with basic parameters
    model_kwargs = {**embedder_config["model_kwargs"]}
    if override_model:
        model_kwargs["model"] = override_model

    embedder_kwargs = {"model_client": model_client, "model_kwargs": model_kwargs}
    
    embedder = adal.Embedder(**embedder_kwargs)
    
    # Set batch_size as an attribute if available (not a constructor parameter)
    if "batch_size" in embedder_config:
        embedder.batch_size = embedder_config["batch_size"]
    return embedder
