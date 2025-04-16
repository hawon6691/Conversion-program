import zipfile
import xml.etree.ElementTree as ET
from docx import Document

def extract_text_from_hwpx(hwpx_path):
    texts = []
    with zipfile.ZipFile(hwpx_path, 'r') as zip_ref:
        with zip_ref.open('Contents/section0.xml') as section_file:
            tree = ET.parse(section_file)
            root = tree.getroot()

            # 실제 네임스페이스 이름
            ns = {'hp': 'http://www.hancom.co.kr/hwpml/2011/paragraph'}

            # 텍스트 추출
            for t in root.findall('.//hp:t', ns):
                if t.text:
                    texts.append(t.text)
    
    return texts

def save_texts_to_docx(texts, docx_path):
    doc = Document()
    for t in texts:
        doc.add_paragraph(t)
    doc.save(docx_path)

# 사용 예
file_name = '안녕하세요'
hwpx_file = f"C:/Users/hawon/Develop/python/uni/hwp_form/change_file/{file_name}.hwpx"
docx_file = f"C:/Users/hawon/Develop/python/uni/hwp_form/change_file/{file_name}.docx"

texts = extract_text_from_hwpx(hwpx_file)
save_texts_to_docx(texts, docx_file)

print("✅ 변환 완료:", docx_file)
