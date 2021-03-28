from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
import random
import string


def random_string_generator(size=8,
                            chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_reference_number_generator(model):
    reference_number = random_string_generator()

    Klass = model

    qs_exists = Klass.objects.filter(
        reference_number=reference_number).exists()
    if qs_exists:
        return unique_reference_number_generator(model)
    return reference_number


def generate_pdf(title, body):
    y = 800
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    p.setFont('Helvetica-Bold', 10)
    p.drawString(220, y, title)
    p.setFont('Helvetica', 10)
    p.drawString(50, 780, body)
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    return pdf
