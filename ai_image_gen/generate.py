from diffusers import StableDiffusionPipeline
import torch
import uuid
import os

# 모델 로드 (1회만)
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-2-1",  # ← 대체 모델
    torch_dtype=torch.float16
).to("cuda")

def generate_image(prompt: str) -> str:
    # 프롬프트 유효성 검사
    if not prompt or len(prompt.strip()) < 3:
        raise ValueError("프롬프트가 너무 짧거나 비어있습니다.")

    # 이미지 생성
    result = pipe(prompt, guidance_scale=7.5, num_inference_steps=30)

    if not result or not result.images:
        raise RuntimeError("이미지 생성 실패: 결과 없음")

    image = result.images[0]

    # 저장
    filename = f"{uuid.uuid4()}.png"
    save_path = os.path.join("media", filename)
    image.save(save_path)
    return filename
