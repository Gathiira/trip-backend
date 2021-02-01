from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.utils import timezone
import random
import string


def random_string_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_reference_number_generator(model, process_prefix):
    reference_number = 'SMOKINACE/' + process_prefix.upper() + '/' + \
        random_string_generator()

    Klass = model

    qs_exists = Klass.objects.filter(
        reference_number=reference_number).exists()
    if qs_exists:
        return unique_reference_number_generator(model, process_prefix=process_prefix)
    return reference_number


def generate_pdf(message):
    y = 700
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.setFont('Helvetica', 10)
    p.drawString(220, y, message)
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
