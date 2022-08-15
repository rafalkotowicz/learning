def transform(legacy_data: dict) -> dict:
    transformed_data = dict()

    for k in legacy_data:
        for val in legacy_data[k]:
            transformed_data[val.lower()] = k

    return transformed_data
