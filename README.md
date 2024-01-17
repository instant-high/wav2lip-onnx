# wav2lip-onnx
This is my modified minimum wav2lip version.

No torch required.

Inference is quite fast running on CPU using the converted wav2lip onnx models and antelope face detection.

(Running on GPU possible but some changes needed)

No additional modifications like face enhancement, face alignment.
Just same functions as the original repo: https://github.com/Rudrabha/Wav2Lip

(Modified)Face detection is taken from
https://github.com/neuralchen/SimSwap

Installation:
Clone this repository and read Setup.txt

Face detection checkpoint already in insightface_func/models/antelope

Converted wav2lip / wav2lip_gan checkpoints can be downloaded here: 
https://drive.google.com/file/d/1_l4QC2RJ9nXapSQRD61-Q4KbSApc53HM/view?usp=sharing.

Unzip to checkpoints folder

If you want to convert the wav2lip checkpoints (folder convert2onnx) you have to run the script makeonnx.py in the root of an original wav2lip installation.
