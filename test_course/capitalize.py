def capitalize(text):
    if isinstance(text, str):
        return f'{text[:1].upper()}{text[1:]}'
    return text
