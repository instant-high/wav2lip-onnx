import torch
import torch.onnx
from models import Wav2Lip
import sys

model = Wav2Lip()
checkpoint_path = "checkpoints/wav2lip_gan.pth"
#checkpoint_path = "checkpoints/wav2lip.pth"


modelz = torch.load(checkpoint_path)

device="cpu"
s = modelz["state_dict"]
new_s = {}
for k, v in s.items():
    new_s[k.replace('module.', '')] = v


model.load_state_dict(new_s)
model = model.to(device)

model.eval()

input_shape1 = (1, 1, 80, 16)
input_shape2 = (1, 6, 96, 96)

dynamic_axes = {'mel_spectrogram': {0: 'batch_size'}, 'video_frames': {0: 'batch_size'}}

# or "checkpoints/wav2lip.onnx" 
torch.onnx.export(model,
                  (torch.randn(input_shape1, device=device), torch.randn(input_shape2, device=device)),
                  "checkpoints/wav2lip_gan.onnx",
                  export_params=True,
                  opset_version=10,
                  input_names=["mel_spectrogram", "video_frames"],
                  output_names=["predicted_frames"],
                  dynamic_axes=dynamic_axes,
                  verbose=False)
print("Done !!")