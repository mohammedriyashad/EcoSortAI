def retrieve_answer(query: str, kb_text: str):
    query_lower = query.lower()
    lines = kb_text.split("\n")
    matched = []

    for line in lines:
        if any(word in line.lower() for word in query_lower.split()):
            matched.append(line)

    if not matched:
        return "Sorry, I could not find specific rules. Please contact local municipal guidelines."
    return "\n".join(matched[:10])