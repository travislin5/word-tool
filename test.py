from docx import Document

def replace_text_in_docx(file_path, old_text, new_text):
    # 打開 Word 文件
    doc = Document(file_path)

    # 遍歷每一個段落和段落中的每一個run
    for para in doc.paragraphs:
        if old_text in para.text:
            for run in para.runs:
                if old_text in run.text:
                    run.text = run.text.replace(old_text, new_text)

    # 保存修改後的文件
    doc.save('modified_' + file_path)

# 替換文本
replace_text_in_docx('demo.docx', 'Document', '12345678')