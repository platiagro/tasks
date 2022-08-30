def mock_log_metric(key, value, **kwargs):
    if not isinstance(value, float):
        raise ValueError(f"Can't pickle {key}")
