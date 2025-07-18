# generator/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from generate import generate_image

@csrf_exempt
def index(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")
        filename = generate_image(prompt)
        if not filename:
            return render(request, "index.html", {"error": "이미지 생성에 실패했습니다."})

        return render(request, "result.html", {"image_url": f"/media/{filename}", "prompt": prompt})
    return render(request, "index.html")

