# wav2lip-onnx
This is my modified minimum wav2lip version.

No torch required.

Inference is quite fast running on CPU using the converted wav2lip onnx models and antelope face detection.
Can be run on Nvidia GPU, tested on RTX3060
Update: tested on GTX1050

No additional functions like face enhancement, face alignment.
Just same functions as the original repository

(Modified)Face detection is taken from simswap

Installation:
Clone this repository and read Setup.txt

Don't forget to install ffmpeg and set path variable.



Face detection checkpoint already in insightface_func/models/antelope

Converted wav2lip / wav2lip_gan checkpoints can be downloaded here: 
https://drive.google.com/file/d/1_l4QC2RJ9nXapSQRD61-Q4KbSApc53HM/view?usp=sharing.

Unzip to checkpoints folder

If you want to convert the wav2lip checkpoints yourself (folder convert2onnx/makeonnx.py) you have to run the script in the root of an original wav2lip installation.

Original wav2lip - https://github.com/Rudrabha/Wav2Lip

SimSwap - https://github.com/neuralchen/SimSwap


Some of my older, not yet public, projects you can find here:
https://www.youtube.com/playlist?list=PLvwlV1S1SYHBjPjwY49KF5d-z59a32v8C
