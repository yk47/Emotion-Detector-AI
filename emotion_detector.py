from transformers import pipeline

# Load model once
classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)

def analyze_emotion(text):
    if not text:
        return None

    results = classifier(text)

    emotions = {}

    try:
        # Case 1: expected format (list of list of dicts)
        for item in results[0]:
            emotions[item['label'].lower()] = round(item['score'], 3)

    except Exception:
        # Case 2: fallback (simple output)
        label = results[0]['label'] if isinstance(results[0], dict) else str(results[0])
        
        emotions = {
            "joy": 0,
            "sadness": 0,
            "anger": 0,
            "fear": 0,
            "disgust": 0
        }

        emotions[label.lower()] = 1.0

    return emotions
