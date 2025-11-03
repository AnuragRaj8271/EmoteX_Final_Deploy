def query_assistant(prompt, api_key=None):
    if api_key:
        return {'text':'call to OpenAI would happen here'}
    return {'text':'fallback assistant response'}
