fimport os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Use absolute path
report_folder = r"C:\Users\Angelica\Desktop\Fake-profile-Detector\Report"
pdf_file = os.path.join(report_folder, "Fake_Social_Media_Profile_Detection_Report.pdf")

# Create PDF
doc = SimpleDocTemplate(pdf_file)
styles = getSampleStyleSheet()
content = []

sections = [
    ("Introduction", "Fake social media profiles are increasingly used for scams, misinformation, and identity theft. This project focuses on detecting such profiles using open-source intelligence techniques."),
    ("Objective", "To design a tool that analyzes public social media data and identifies potentially fake profiles."),
    ("Technology Stack", "Python, Requests, BeautifulSoup, Selenium, HTML, CSS, JavaScript, GitHub."),
    ("System Architecture", "Frontend interface, backend analysis engine, and reporting module."),
    ("Methodology", "Scrape public profile data, check profile images, assign risk scores, and classify profiles."),
    ("Results", "Profiles are categorized as Genuine, Suspicious, or Fake based on calculated risk scores."),
    ("Conclusion", "The project demonstrates practical OSINT and cybersecurity skills."),
    ("Future Scope", "Integration with real APIs, machine learning models, and real-time monitoring.")
]

for title, text in sections:
    content.append(Paragraph(f"<b>{title}</b>", styles["Heading2"]))
    content.append(Spacer(1, 6))
    content.append(Paragraph(text, styles["Normal"]))
    content.append(Spacer(1, 12))

doc.build(content)
print(f"PDF generated successfully at: {pdf_file}")

