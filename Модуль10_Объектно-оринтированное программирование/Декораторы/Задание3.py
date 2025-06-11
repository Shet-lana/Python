# Каждый год ваша компания предоставляет различным
# государственным организациям финансовую отчетность.
# В зависимости от организации форматы отчетности разные.
# Используя механизм декораторов, решите вопрос отчетности для организаций.

from functools import wraps
import csv
import io
from datetime import date
import base64
from pdfkit import from_string as convert_to_pdf
import os
os.environ["PATH"] += os.pathsep + r'C:\Program Files\wkhtmltopdf\bin'

# Базовый класс для каждого формата отчета
class BaseReportGenerator:
    def __init__(self, format_name):
        self.format_name = format_name

    def create_report(self, content):
        raise NotImplementedError("Метод должен быть реализован в подклассах!")

# Класс для генерации XML-отчёта
class XmlReport(BaseReportGenerator):
    def __init__(self):
        super().__init__('XML')

    def create_report(self, content):
        return f'<root><data>{content}</data></root>'

# Класс для генерации JSON-отчёта
class JsonReport(BaseReportGenerator):
    def __init__(self):
        super().__init__('JSON')

    def create_report(self, content):
        import json
        return json.dumps({'report': content}, ensure_ascii=False).encode().decode()  # Преобразуем обратно в UTF-8

# Класс для генерации CSV-отчёта
class CsvReport(BaseReportGenerator):
    def __init__(self):
        super().__init__('CSV')

    def create_report(self, content):
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(['Отчёт'])
        writer.writerow([content])
        return output.getvalue()

# Класс для генерации PDF-отчёта
class PdfReport(BaseReportGenerator):
    def __init__(self):
        super().__init__('PDF')

    def create_report(self, content):
        today = date.today().strftime('%Y-%m-%d')
        html = f"""
        <html>
          <head><title>Финансовый отчёт {today}</title></head>
          <body>
              <h1>Финансовая отчётность</h1>
              <p>{content}</p>
          </body>
        </html>
        """
        return convert_to_pdf(html, False)

# Основной генератор отчётов
def generate_report(report_generator_class):
    def decorator(func):
        @wraps(func)
        def wrapper(content):
            generator = report_generator_class()
            report = generator.create_report(content)
            return report
        return wrapper
    return decorator

# Применение генераторов отчётов
@generate_report(XmlReport)
def generate_xml_report(content):
    return content

@generate_report(JsonReport)
def generate_json_report(content):
    return content

@generate_report(CsvReport)
def generate_csv_report(content):
    return content

@generate_report(PdfReport)
def generate_pdf_report(content):
    return base64.b64encode(convert_to_pdf(content)).decode()  # Конвертируем в Base64 для удобства отображения

# Генерируем отчёты
try:
    xml_report = generate_xml_report("Тестовый отчёт в XML")
    json_report = generate_json_report("Тестовый отчёт в JSON")
    csv_report = generate_csv_report("Тестовый отчёт в CSV")
    pdf_report_base64 = generate_pdf_report("Тестовый отчёт в PDF")

    print("\nXML ОТЧЁТ:")
    print(xml_report)

    print("\nJSON ОТЧЁТ:")
    print(json_report)

    print("\nCSV ОТЧЁТ:")
    print(csv_report)

    print("\nPDF ОТЧЁТ (Base64-кодировка):")
    print(pdf_report_base64[:50], "...")  # Показываем первые 50 символов для примера

except Exception as e:
    print(f"Ошибка при формировании отчёта: {e}")