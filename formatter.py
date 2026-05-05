def format_output(emotions):
    if not emotions:
        return {"error": "Invalid input"}

    dominant = max(emotions, key=emotions.get)

    return {
        "emotions": emotions,
        "dominant_emotion": dominant
    }