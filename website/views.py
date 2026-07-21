"""
website/views.py
Views for the portfolio website — home page and contact form handler.
"""
import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, Project, Skill, Experience, Education, Article, Certificate


def home_view(request):
    """Render the single-page portfolio home."""
    context = {
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'experiences': Experience.objects.all(),
        'education': Education.objects.all(),
        'articles': Article.objects.all(),
        'certificates': Certificate.objects.all(),
    }
    return render(request, 'home.html', context)


@csrf_exempt
@require_http_methods(["POST"])
def contact_view(request):
    """
    Handle contact form submission via AJAX (JSON body).
    Validates input, saves the message, and sends an email alert.
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
        # Save to DB
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )
        
        # Send Email Alert
        mail_subject = f"New Portfolio Contact: {subject}"
        mail_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        try:
            result = send_mail(
                mail_subject,
                mail_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            print(f"[ContactForm] Email sent successfully! Result: {result}")
        except Exception as e:
            import traceback
            print(f"[ContactForm] Email failed to send: {e}")
            traceback.print_exc()
            return JsonResponse({
                'success': False, 
                'error': f'Database saved, but email failed to send. Error: {str(e)}'
            }, status=500)

    except Exception as db_error:
        print(f"[ContactForm] DB error: {db_error}")
        return JsonResponse(
            {'success': False, 'error': 'Could not save message. Please try again later.'},
            status=500
        )

    return JsonResponse({
        'success': True,
        'message': f"Thank you, {name}! Your message has been received. I'll get back to you soon."
    })
