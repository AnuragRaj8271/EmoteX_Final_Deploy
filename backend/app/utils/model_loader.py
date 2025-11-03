import os
from pathlib import Path
def ensure_models(hf_repo=None, cache_dir="backend/app/models_cache"):
    Path(cache_dir).mkdir(parents=True, exist_ok=True)
    if not hf_repo:
        return {"status":"no-op","cache_dir":cache_dir}
    return {"status":"would-download","hf_repo":hf_repo,"cache_dir":cache_dir}
