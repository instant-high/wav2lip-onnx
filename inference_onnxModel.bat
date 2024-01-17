@echo on
call C:\users\insta\Anaconda3\Scripts\activate.bat
call conda activate w2lonnx
cd c:\tutorial\wav2lip_onnx_min
python -W ignore inference_onnxModel.py --checkpoint_path "checkpoints\wav2lip_gan.onnx" --face "D:\360.mp4" --audio "D:\putindictator.wav" --outfile "D:\!!onnx.mp4" --nosmooth  --pads 0 10 0 0 --fps 29.97
pause
call conda deactivate
