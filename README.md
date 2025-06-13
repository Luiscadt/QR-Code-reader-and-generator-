# AI-Powered Animal Counter

This repository provides a simple command line tool to count animals in an image using a pretrained object detection model from **torchvision**.

The script `animal_counter.py` loads `fasterrcnn_resnet50_fpn` and reports the number of detected animals in the provided image.

## Usage

```bash
python animal_counter.py path/to/image.jpg
```

The script prints the count of each detected animal class. It expects PyTorch, torchvision and Pillow to be installed. Downloading model weights requires an internet connection on first run.

## Notes

The previous QR code utilities have been removed in favor of this new functionality.
