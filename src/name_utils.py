def make_unique_names(base_names):
    """Ensure names are unique by adding _1, _2, etc. when needed."""
    name_counts = {}
    final_names = []
    for name in base_names:
        count = name_counts.get(name, 0)
        final_name = f"{name}_{count}" if count > 0 else name
        name_counts[name] = count + 1
        final_names.append(final_name)
    return final_names