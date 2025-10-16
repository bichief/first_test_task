import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from admin_panel.telebot.models import Questions, Users


@csrf_exempt
def render_webapp(request):
    return render(request, 'webapp/index.html')


# ------------- API ------------
@csrf_exempt
def save_answer(request):
    if request.method != "POST":
        return JsonResponse({"error": "Метод не разрешен"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
        telegram_id = data.get("telegram_id")
        text = data.get("text")

        if not telegram_id or not text:
            return JsonResponse({"error": "Отсутствуют обязательные поля"}, status=400)

        user = Users.objects.get(telegram_id=telegram_id)
        Questions.objects.create(
            sender=user,
            question=text,
        )

        return JsonResponse({"status": "ok", "message": "Ответ сохранен"})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Некорректный JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
