from ultralytics import YOLO


class Inference:
    def __init__(self, model_path, treshold=0.7):
        self.model_path = model_path
        self.treshold = treshold
        self.model = YOLO(model_path)
        
        
    def predict(self, img_path):
        results = self.model(img_path)
        boxes = results[0].boxes.xyxy.cpu().numpy()
        probs = list(results[0].boxes.conf.cpu().numpy())
        return [[*list(bbox), prob] for bbox, prob in zip(boxes, probs) if prob > self.treshold]
