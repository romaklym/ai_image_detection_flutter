# server.py
import io
from typing import Dict

import torch
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image as PILImage
from transformers import AutoImageProcessor, SiglipForImageClassification

MODEL_IDENTIFIER = "Ateeqq/ai-vs-human-image-detector"

# Device: Use GPU if available, otherwise CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

print(f"Loading processor from: {MODEL_IDENTIFIER}")
processor = AutoImageProcessor.from_pretrained(MODEL_IDENTIFIER)

print(f"Loading model from: {MODEL_IDENTIFIER}")
model = SiglipForImageClassification.from_pretrained(MODEL_IDENTIFIER)
model.to(device)
model.eval()
print("Model and processor loaded successfully.")

app = FastAPI()

# No browser CORS in mobile apps, but this helps for testing from web clients
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def classify_image(image: PILImage.Image) -> Dict:
    inputs = processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    probabilities = torch.softmax(logits, dim=-1)[0]
    predicted_class_idx = logits.argmax(-1).item()
    predicted_label = model.config.id2label[predicted_class_idx]
    predicted_prob = probabilities[predicted_class_idx].item()

    # Build dict of all class probs
    all_scores = {
        model.config.id2label[i]: float(probabilities[i].item())
        for i in range(len(probabilities))
    }

    return {
        "label": predicted_label,       # 'ai' or 'hum' (or similar)
        "confidence": float(predicted_prob),
        "scores": all_scores,
    }


@app.post("/classify")
async def classify(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = PILImage.open(io.BytesIO(contents)).convert("RGB")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid image: {e}")

    result = classify_image(image)

    # Server can also decide allow/deny:
    # allow if label == 'hum' and confidence >= 0.9
    label = result["label"]
    conf = result["confidence"]
    allow = (label == "hum") and (conf >= 0.9)

    return {
        "label": label,
        "confidence": conf,
        "allow": allow,
        "scores": result["scores"],
    }
