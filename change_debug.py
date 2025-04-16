import zipfile
import xml.etree.ElementTree as ET

def debug_hwpx_structure(hwpx_path):
    with zipfile.ZipFile(hwpx_path, 'r') as zip_ref:
        with zip_ref.open('Contents/section0.xml') as section_file:
            tree = ET.parse(section_file)
            root = tree.getroot()

            # 모든 태그 이름 출력해보기
            for elem in root.iter():
                print(elem.tag, "=>", elem.text)

# 실행
hwpx_file = "C:/Users/hawon/Develop/python/uni/hwp_form/안녕하세요.hwpx"
debug_hwpx_structure(hwpx_file)
