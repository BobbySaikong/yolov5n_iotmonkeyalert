import torch
model = torch.load('yolov5n.pt')
torch.onnx.export(model, dummy_input, 'yolov5n.onnx', export_params=True)
