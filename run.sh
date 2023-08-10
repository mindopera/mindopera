apt-get update
apt-get upgrade
apt-get -y install git-lfs
apt -y install git-lfs
wget -O /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_lineart.pth https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_lineart.pth
wget -O /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11p_sd15_openpose.pth https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11p_sd15_openpose.pth
wget -O /workspace/stable-diffusion-webui/extensions/sd-webui-controlnet/models/control_v11f1e_sd15_tile.pth https://huggingface.co/lllyasviel/ControlNet-v1-1/resolve/main/control_v11f1e_sd15_tile.pth
git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111/ /workspace/stable-diffusion-webui/extensions/ultimate-upscale/
wget -O /workspace/stable-diffusion-webui/models/Stable-diffusion/RevAnimated.safetensors https://civitai.com/api/download/models/46846
wget -O /workspace/stable-diffusion-webui/models/Stable-diffusion/realisticvision5.safetensors https://civitai.com/api/download/models/130072
wget -O /workspace/stable-diffusion-webui/embeddings/negative-embedding-realisticvision2.pt https://civitai.com/api/download/models/42247
wget -O /workspace/stable-diffusion-webui/embeddings/easynegative.pt https://civitai.com/api/download/models/9208
wget -O /workspace/stable-diffusion-webui/embeddings/fastnegative.pt https://civitai.com/api/download/models/94057
wget -O /workspace/stable-diffusion-webui/models/ESRGAN/4x-UltraSharp.pth https://huggingface.co/datasets/Kizi-Art/Upscale/resolve/main/4x-UltraSharp.pth
wget -O /workspace/stable-diffusion-webui/models/Stable-diffusion/sdxlbase-for-training.safetensors https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors
wget -O /workspace/stable-diffusion-webui/models/VAE/sdxl_vae.safetensors https://huggingface.co/stabilityai/sdxl-vae/resolve/main/sdxl_vae.safetensors
git clone https://github.com/pharmapsychotic/clip-interrogator-ext /workspace/stable-diffusion-webui/extensions/clip-interrogator/
git clone https://github.com/Zyin055/Config-Presets /workspace/stable-diffusion-webui/extensions/Config-Presets/
git clone https://github.com/AlUlkesh/stable-diffusion-webui-images-browser /workspace/stable-diffusion-webui/extensions/image-browser/
git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete /workspace/stable-diffusion-webui/extensions/tag-complete/
git clone https://github.com/LEv145/--sd-webui-ar-plus /workspace/stable-diffusion-webui/extensions/ar-helper/
git clone https://github.com/vladmandic/sd-extension-system-info /workspace/stable-diffusion-webui/extensions/systems-info/
git clone https://github.com/huchenlei/sd-webui-openpose-editor /workspace/stable-diffusion-webui/extensions/open-pose-editor/
git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui-wildcards /workspace/stable-diffusion-webui/extensions/wildcards/
git clone https://github.com/numz/sd-wav2lip-uhq /workspace/stable-diffusion-webui/extensions/wav2lip/
git clone https://github.com/OpenTalker/SadTalker /workspace/stable-diffusion-webui/extensions/SadTalker/
git clone https://github.com/kabachuha/sd-webui-text2video /workspace/stable-diffusion-webui/extensions/text2video/
git clone https://github.com/Bing-su/adetailer /workspace/stable-diffusion-webui/extensions/adetailer/
git clone https://github.com/CiaraStrawberry/TemporalKit /workspace/stable-diffusion-webui/extensions/temporalkit/
git clone https://huggingface.co/cerspense/zeroscope_v2_576w /workspace/stable-diffusion-webui/models/ModelScope/t2v/
git clone https://github.com/bmaltais/kohya_ss /workspace/kohya_ss/
pip install ffmpeg
