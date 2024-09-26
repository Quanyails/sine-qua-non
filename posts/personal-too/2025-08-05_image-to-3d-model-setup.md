---
tags:
  - image-to-3d
---

# Image to 3D Model Setup

## Commands

```shell
git clone https://github.com/Tencent-Hunyuan/Hunyuan3D-2.git
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu128
python gradio_app.py --model_path tencent/Hunyuan3D-2 --subfolder hunyuan3d-dit-v2-0 --texgen_model_path tencent/Hunyuan3D-2 --low_vram_mode
# python gradio_app.py --model_path tencent/Hunyuan3D-2mv --subfolder hunyuan3d-dit-v2-mv --texgen_model_path tencent/Hunyuan3D-2 --low_vram_mode
```

<!-- Path to model:  C:\Users\Quany/.cache/hy3dgen\tencent/Hunyuan3D-2\hunyuan3d-dit-v2-0 -->

## Resources used

- [ComfyUI NVIDIA#Troubleshooting](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file#troubleshooting)
- [Error: "CUDA error: no kernel image is available for execution on the device..."](https://github.com/easydiffusion/easydiffusion/issues/1918#issuecomment-2828234089)
- [[Feature Request] Multi-Image/Frame Input support to Improve output mesh geometry & texture placement](https://github.com/Tencent-Hunyuan/Hunyuan3D-2/issues/47)
- [Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2/blob/main/README.md)
- [Set Up Hunyuan3D-2 on Windows: A Step-by-Step Guide](https://codersera.com/blog/set-up-hunyuan3d-2-on-windows-a-step-by-step-guide) 
