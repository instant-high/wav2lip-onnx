# wav2lip-onnx
This is my modified minimum wav2lip version.

No torch required.

Inference is quite fast running on CPU using the converted wav2lip onnx models and antelope face detection.

(Running on GPU possible but some changes required)

No additional functions like face enhancement, face alignment.
Just same functions as the original repository

(Modified)Face detection is taken from simswap

Installation:
Clone this repository and read Setup.txt

Face detection checkpoint already in insightface_func/models/antelope

Converted wav2lip / wav2lip_gan checkpoints can be downloaded here: 
https://drive.google.com/file/d/1_l4QC2RJ9nXapSQRD61-Q4KbSApc53HM/view?usp=sharing.

Unzip to checkpoints folder

If you want to convert the wav2lip checkpoints yourself (folder convert2onnx/makeonnx.py) you have to run the script in the root of an original wav2lip installation.

Original wav2lip - https://github.com/Rudrabha/Wav2Lip

SimSwap - https://github.com/neuralchen/SimSwap
