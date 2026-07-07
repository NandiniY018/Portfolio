"""
website/views.py
Views for the portfolio website — home page and contact form handler.
"""
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import ContactMessage


def home_view(request):
    """Render the single-page portfolio home."""
    return render(request, 'home.html')


@csrf_exempt
@require_http_methods(["POST"])
def contact_view(request):
    """
    Handle contact form submission via AJAX (JSON body).
    Validates input and saves the message to the database.
    Returns a JSON response with success/error status.
    """
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'success': False, 'error': 'Invalid request format.'}, status=400)

    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    subject = data.get('subject', '').strip()
    message = data.get('message', '').strip()

    # Server-side validation
    errors = {}
    if not name or len(name) < 2:
        errors['name'] = 'Please enter your full name (at least 2 characters).'
    if not email or '@' not in email:
        errors['email'] = 'Please enter a valid email address.'
    if not subject or len(subject) < 3:
        errors['subject'] = 'Please enter a subject (at least 3 characters).'
    if not message or len(message) < 10:
        errors['message'] = 'Please enter a message (at least 10 characters).'

    if errors:
        return JsonResponse({'success': False, 'errors': errors}, status=422)

    try:
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
    except Exception as db_error:
        # Log the error but return a graceful response
        print(f"[ContactForm] DB error: {db_error}")
        return JsonResponse(
            {'success': False, 'error': 'Could not save message. Please try again later.'},
            status=500
        )

    return JsonResponse({
        'success': True,
        'message': f"Thank you, {name}! Your message has been received. I'll get back to you soon."
    })
