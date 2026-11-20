import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

output_dir = os.path.abspath("sample_resumes")
os.makedirs(output_dir, exist_ok=True)

resumes = [
    {
        "filename": os.path.join(output_dir, "Sarah_Chen_FullStack.pdf"),
        "name": "Sarah Chen",
        "email": "sarah.chen@example.com",
        "phone": "415-555-0192",
        "experience": [
            {
                "title": "Senior Full Stack Engineer",
                "company": "CloudScale Systems",
                "dates": "2021 - 2024",
                "desc": "Architected distributed web applications using React, Python, and FastAPI with PostgreSQL databases."
            },
            {
                "title": "Software Developer",
                "company": "Nexus Technologies",
                "dates": "2019 - 2021",
                "desc": "Developed responsive frontends with TailwindCSS and optimized backend database queries."
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Technology",
                "institution": "Stanford University",
                "year": "2019"
            }
        ],
        "skills": ["Python", "FastAPI", "React", "JavaScript", "PostgreSQL", "Docker", "Git", "TailwindCSS"]
    },
    {
        "filename": os.path.join(output_dir, "David_Miller_BackendEngineer.pdf"),
        "name": "David Miller",
        "email": "david.miller@example.com",
        "phone": "212-555-0144",
        "experience": [
            {
                "title": "Backend Systems Engineer",
                "company": "Apex Data Labs",
                "dates": "2020 - 2024",
                "desc": "Designed scalable REST APIs in Python and managed relational databases and microservices."
            }
        ],
        "education": [
            {
                "degree": "Master of Technology",
                "institution": "Georgia Institute of Technology",
                "year": "2020"
            }
        ],
        "skills": ["Python", "SQLAlchemy", "PostgreSQL", "Docker", "AWS", "FastAPI", "Git"]
    },
    {
        "filename": os.path.join(output_dir, "Priya_Sharma_FrontendDeveloper.pdf"),
        "name": "Priya Sharma",
        "email": "priya.sharma@example.com",
        "phone": "510-555-0183",
        "experience": [
            {
                "title": "Frontend React Engineer",
                "company": "PixelCraft Digital",
                "dates": "2022 - 2024",
                "desc": "Constructed immersive user interfaces with React, Three.js 3D animations, and TailwindCSS."
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Engineering",
                "institution": "University of California Berkeley",
                "year": "2022"
            }
        ],
        "skills": ["React", "JavaScript", "Three.js", "TailwindCSS", "HTML", "CSS", "Vite", "Git"]
    },
    {
        "filename": os.path.join(output_dir, "Alex_Johnson_EntryLevel.pdf"),
        "name": "Alex Johnson",
        "email": "alex.johnson@example.com",
        "phone": "650-555-0177",
        "experience": [
            {
                "title": "Junior Software Engineer",
                "company": "Innovatech Hub",
                "dates": "2023 - 2024",
                "desc": "Collaborated on frontend and backend web tasks, writing automated tests and documentation."
            }
        ],
        "education": [
            {
                "degree": "Bachelor of Technology",
                "institution": "State Polytechnic University",
                "year": "2023"
            }
        ],
        "skills": ["Python", "JavaScript", "React", "HTML", "CSS", "Git"]
    }
]

styles = getSampleStyleSheet()
title_style = ParagraphStyle("TitleStyle", parent=styles["Heading1"], fontSize=18, leading=22, textColor=colors.HexColor("#1E293B"), spaceAfter=2)
contact_style = ParagraphStyle("ContactStyle", parent=styles["Normal"], fontSize=10, leading=14, textColor=colors.HexColor("#475569"), spaceAfter=2)
heading_style = ParagraphStyle("SectionHeading", parent=styles["Heading2"], fontSize=12, leading=16, textColor=colors.HexColor("#2563EB"), spaceBefore=10, spaceAfter=4)
item_title = ParagraphStyle("ItemTitle", parent=styles["Normal"], fontSize=10, leading=14, textColor=colors.HexColor("#0F172A"), fontName="Helvetica-Bold")
item_subtitle = ParagraphStyle("ItemSubtitle", parent=styles["Normal"], fontSize=9.5, leading=13.5, textColor=colors.HexColor("#334155"))
item_meta = ParagraphStyle("ItemMeta", parent=styles["Normal"], fontSize=9, leading=13, textColor=colors.HexColor("#64748B"))
body_normal = ParagraphStyle("BodyNormal", parent=styles["Normal"], fontSize=9, leading=13, textColor=colors.HexColor("#334155"), spaceAfter=4)

for r in resumes:
    doc = SimpleDocTemplate(r["filename"], pagesize=letter, leftMargin=45, rightMargin=45, topMargin=35, bottomMargin=35)
    story = []
    
    # 1. Header (Name, Email, Phone on separate lines for CFG Lexer)
    story.append(Paragraph(r["name"].upper(), title_style))
    story.append(Paragraph(r["email"], contact_style))
    story.append(Paragraph(r["phone"], contact_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#CBD5E1"), spaceBefore=4, spaceAfter=8))
    
    # 2. Experience (SECTION_EXPERIENCE)
    story.append(Paragraph("EXPERIENCE", heading_style))
    for exp in r["experience"]:
        story.append(Paragraph(exp["title"], item_title))
        story.append(Paragraph(exp["company"], item_subtitle))
        story.append(Paragraph(exp["dates"], item_meta))
        story.append(Paragraph(exp["desc"], body_normal))
        story.append(Spacer(1, 4))
        
    # 3. Education (SECTION_EDUCATION)
    story.append(Paragraph("EDUCATION", heading_style))
    for edu in r["education"]:
        story.append(Paragraph(edu["degree"], item_title))
        story.append(Paragraph(edu["institution"], item_subtitle))
        story.append(Paragraph(edu["year"], item_meta))
        story.append(Spacer(1, 4))
        
    # 4. Skills (SECTION_SKILLS)
    story.append(Paragraph("SKILLS", heading_style))
    for s in r["skills"]:
        story.append(Paragraph(s, item_subtitle))
        
    doc.build(story)
    print(f"Generated: {r['filename']}")

print("\nDone! All sample resumes generated successfully.")
