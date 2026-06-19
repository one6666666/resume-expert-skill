#!/usr/bin/env python3
"""
Resume DOCX Generator — 生成 ATS 兼容的 Word 简历文档

用法:
    python generate_docx.py <output_path> <json_data_path>

JSON 数据格式:
{
    "name": "张三",
    "target_position": "高级后端工程师",
    "years": "5",
    "email": "zhangsan@example.com",
    "phone": "13800138000",
    "location": "北京",
    "summary": "个人简介文本...",
    "skills": ["Java", "Spring Boot", "MySQL", "Redis", "Docker"],
    "experience": [
        {
            "role": "高级Java开发工程师",
            "company": "某科技有限公司",
            "date": "2021.06 - 至今",
            "details": [
                "主导设计高并发支付系统，日均处理交易100万+，可用性99.99%",
                "优化核心查询链路，平均响应时间从500ms降至50ms"
            ]
        }
    ],
    "projects": [
        {
            "name": "分布式支付平台",
            "tech": "Java, Spring Cloud, Kafka, Redis, MySQL",
            "description": "从0到1搭建分布式支付平台，支撑日均百万级交易规模"
        }
    ],
    "education": {
        "degree": "计算机科学与技术 本科",
        "school": "某大学",
        "date": "2015.09 - 2019.06"
    }
}

依赖:
    pip install python-docx
"""

import json
import sys
import os

try:
    from docx import Document
    from docx.shared import Pt, Inches, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
except ImportError:
    print("Error: python-docx not installed. Run: pip install python-docx")
    sys.exit(1)


# ── 颜色配置 ──
PRIMARY = RGBColor(0x00, 0x33, 0x66)   # 深蓝
TEXT = RGBColor(0x33, 0x33, 0x33)
TEXT_LIGHT = RGBColor(0x55, 0x55, 0x55)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)


def set_cell_shading(cell, color_hex):
    """设置单元格背景色"""
    shading = OxmlElement('w:shd')
    shading.set(qn('w:fill'), color_hex)
    shading.set(qn('w:val'), 'clear')
    cell._tc.get_or_add_tcPr().append(shading)


def add_heading_styled(doc, text):
    """添加深蓝色标题"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = PRIMARY
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

    # 底部边框
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '8')
    bottom.set(qn('w:space'), '4')
    bottom.set(qn('w:color'), '003366')
    pBdr.append(bottom)
    pPr.append(pBdr)

    return p


def add_body_text(doc, text, bold=False, size=10, color=TEXT):
    """添加正文文本"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(1)
    return p


def add_bullet(doc, text, size=10):
    """添加项目符号条目"""
    p = doc.add_paragraph()
    prefix_run = p.add_run('• ')
    prefix_run.font.size = Pt(size)
    prefix_run.font.color.rgb = PRIMARY
    prefix_run.font.name = '微软雅黑'
    prefix_run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.color.rgb = TEXT_LIGHT
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.left_indent = Cm(0.5)
    return p


def add_header_line(doc, text, bold=False, size=11):
    """添加头部行"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = WHITE
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.space_before = Pt(0)
    return p


def generate_resume(data, output_path):
    """生成简历 DOCX"""

    doc = Document()

    # 页面设置
    section = doc.sections[0]
    section.page_width = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin = Cm(1.5)
    section.bottom_margin = Cm(1.5)
    section.left_margin = Cm(2.5)
    section.right_margin = Cm(2.5)

    # ── 头部区域 ──
    header_table = doc.add_table(rows=1, cols=1)
    header_cell = header_table.rows[0].cells[0]
    set_cell_shading(header_cell, '003366')

    name = data.get('name', '姓名')
    target = data.get('target_position', '')
    years = data.get('years', '')

    p = header_cell.paragraphs[0]
    run = p.add_run(name)
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.color.rgb = WHITE
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

    subtitle_text = f"{target}  |  {years}年经验" if target and years else target or years
    if subtitle_text:
        add_header_line(header_cell, subtitle_text, size=9)

    # 联系方式
    contact_parts = []
    if data.get('email'):
        contact_parts.append(data['email'])
    if data.get('phone'):
        contact_parts.append(data['phone'])
    if data.get('location'):
        contact_parts.append(data['location'])

    if contact_parts:
        add_header_line(header_cell, ' | '.join(contact_parts), size=9)

    doc.add_paragraph()  # 间距

    # ── 个人简介 ──
    summary = data.get('summary', '')
    if summary:
        add_heading_styled(doc, '个人简介')
        add_body_text(doc, summary, size=10, color=TEXT_LIGHT)
        doc.add_paragraph()

    # ── 专业技能 ──
    skills = data.get('skills', [])
    if skills:
        add_heading_styled(doc, '专业技能')
        skills_text = '、'.join(skills)
        add_body_text(doc, skills_text, size=10)
        doc.add_paragraph()

    # ── 工作经历 ──
    experience = data.get('experience', [])
    if experience:
        add_heading_styled(doc, '工作经历')

        for exp in experience:
            role = exp.get('role', '')
            company = exp.get('company', '')
            date = exp.get('date', '')
            header_text = f"{role} — {company}"
            if date:
                header_text += f"  ({date})"
            add_body_text(doc, header_text, bold=True, size=10, color=TEXT)

            for detail in exp.get('details', []):
                add_bullet(doc, detail, size=10)

            doc.add_paragraph()

    # ── 项目经验 ──
    projects = data.get('projects', [])
    if projects:
        add_heading_styled(doc, '项目经验')

        for proj in projects:
            add_body_text(doc, proj.get('name', '项目名称'), bold=True, size=10, color=PRIMARY)
            tech = proj.get('tech', '')
            if tech:
                add_body_text(doc, f"技术栈：{tech}", size=9, color=PRIMARY)

            desc = proj.get('description', '')
            if desc:
                add_bullet(doc, desc, size=10)

            doc.add_paragraph()

    # ── 教育背景 ──
    edu = data.get('education', {})
    if edu:
        add_heading_styled(doc, '教育背景')
        degree = edu.get('degree', '')
        school = edu.get('school', '')
        date = edu.get('date', '')
        edu_text = f"{degree} — {school}"
        if date:
            edu_text += f"  ({date})"
        add_body_text(doc, edu_text, size=10)

    # 保存
    doc.save(output_path)
    print(f"✅ 简历已生成: {output_path}")
    return output_path


def main():
    if len(sys.argv) < 3:
        print("用法: python generate_docx.py <output_path.docx> <json_data_path.json>")
        print("  or: python generate_docx.py <output_path.docx>")
        print("       (从 stdin 读取 JSON)")
        sys.exit(1)

    output_path = sys.argv[1]

    if len(sys.argv) >= 3:
        json_path = sys.argv[2]
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = json.load(sys.stdin)

    generate_resume(data, output_path)


if __name__ == '__main__':
    main()
