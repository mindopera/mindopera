apt-get update
apt-get upgrade
apt-get -y install git-lfs
apt -y install git-lfs
wget -O /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_lineart.pth https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.pth
wget -O /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_openpose.pth https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.pth
wget -O /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11f1e_sd15_tile.pth https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth
wget -O /workspace/stable-diffusion-webui/models/Stable-diffusion/RevAnimated.safetensors https://civitai.com/api/download/models/46846
wget -O /workspace/stable-diffusion-webui/models/Stable-diffusion/realisticvision5.safetensors https://civitai.com/api/download/models/130072
wget -O /workspace/stable-diffusion-webui/embeddings/negative-embedding-realisticvision2.pt https://civitai.com/api/download/models/42247
wget -O /workspace/stable-diffusion-webui/embeddings/easynegative.pt https://civitai.com/api/download/models/9208
wget -O /workspace/stable-diffusion-webui/embeddings/fastnegative.pt https://civitai.com/api/download/models/94057
wget -O /workspace/stable-diffusion-webui/models/ESRGAN/4x-UltraSharp.pth https://huggingface.co/datasets/Kizi-Art/Upscale/resolve/main/4x-UltraSharp.pth
git clone https://github.com/pharmapsychotic/clip-interrogator-ext ./stable-diffusion-webui/extensions/clip-interrogator/
git clone https://github.com/Zyin055/Config-Presets ./stable-diffusion-webui/extensions/Config-Presets/
git clone https://github.com/AlUlkesh/stable-diffusion-webui-images-browser ./stable-diffusion-webui/extensions/image-browser/
git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete ./stable-diffusion-webui/extensions/tag-complete/
git clone https://github.com/LEv145/--sd-webui-ar-plus ./stable-diffusion-webui/extensions/ar-helper/
git clone https://github.com/vladmandic/sd-extension-system-info ./stable-diffusion-webui/extensions/systems-info/
git clone https://github.com/huchenlei/sd-webui-openpose-editor ./stable-diffusion-webui/extensions/open-pose-editor/
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards ./stable-diffusion-webui/extensions/wildcards/
git clone https://github.com/numz/sd-wav2lip-uhq ./stable-diffusion-webui/extensions/wav2lip/
git clone https://github.com/OpenTalker/SadTalker ./stable-diffusion-webui/extensions/SadTalker/
git clone https://github.com/kabachuha/sd-webui-text2video ./stable-diffusion-webui/extensions/text2video/
git clone https://github.com/Bing-su/adetailer ./stable-diffusion-webui/extensions/adetailer/
git clone https://github.com/CiaraStrawberry/TemporalKit ./stable-diffusion-webui/extensions/temporalkit/
git clone https://huggingface.co/cerspense/zeroscope_v2_576w ./stable-diffusion-webui/models/ModelScope/t2v/
git clone 
pip install ffmpeg
