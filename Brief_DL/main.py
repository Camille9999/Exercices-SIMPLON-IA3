from transformers import AutoImageProcessor, ResNetForImageClassification
from fastapi import FastAPI, File, UploadFile
from PIL import Image
import torch
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model
processor = AutoImageProcessor.from_pretrained("microsoft/resnet-50")
model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")


@app.post("/predict")
async def predict(image: UploadFile = File(...)):

    # Read the image file and convert to a PIL image object
    img = Image.open(image.file)

    # Preprocess the image
    inputs = processor(img, return_tensors="pt")

    # Make a prediction
    with torch.no_grad():
        logits = model(**inputs).logits
    predicted_label = logits.argmax(-1).item()
    label = model.config.id2label[predicted_label]

    # Return the predicted label
    return {"label": label}
