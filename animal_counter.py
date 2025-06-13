import sys
from typing import Dict

try:
    import torch
    from torchvision import transforms
    from torchvision.models.detection import fasterrcnn_resnet50_fpn
    from PIL import Image
except ImportError as exc:
    print("Required libraries are not installed: {}".format(exc))
    sys.exit(1)

ANIMAL_CLASSES = {
    15: 'cat',
    16: 'dog',
    17: 'horse',
    18: 'sheep',
    19: 'cow',
    20: 'elephant',
    21: 'bear',
    22: 'zebra',
    23: 'giraffe',
    24: 'backpack',  # not animal but leftover from COCO numbering
}

# Remove non-animal classes if mis-specified
ANIMAL_CLASSES = {k: v for k, v in ANIMAL_CLASSES.items() if v not in {'backpack'}}


def load_model():
    model = fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()
    return model


def count_animals(model, image_path: str) -> Dict[str, int]:
    img = Image.open(image_path).convert('RGB')
    transform = transforms.Compose([transforms.ToTensor()])
    img_tensor = transform(img)
    with torch.no_grad():
        outputs = model([img_tensor])[0]

    counts: Dict[str, int] = {}
    for label, score in zip(outputs['labels'], outputs['scores']):
        if score < 0.5:
            continue
        label_idx = label.item()
        name = ANIMAL_CLASSES.get(label_idx)
        if name is not None:
            counts[name] = counts.get(name, 0) + 1
    return counts


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python animal_counter.py <image_path>")
        sys.exit(1)
    image_path = sys.argv[1]
    model = load_model()
    counts = count_animals(model, image_path)
    if counts:
        print("Animal counts:")
        for animal, count in counts.items():
            print(f"{animal}: {count}")
    else:
        print("No animals detected.")
