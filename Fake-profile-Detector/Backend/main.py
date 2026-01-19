"""
main.py
Main controller for fake profile detection
"""

from scraper import scrape_profile
from image_check import reverse_image_check


def analyze_profile(profile_url, image_url):
    score = 0
    reasons = []

    profile_data = scrape_profile(profile_url)

    if profile_data["suspicious"]:
        score += 30
        reasons.extend(profile_data["reasons"])

    image_result = reverse_image_check(image_url)

    if image_result["image_suspicious"]:
        score += 30
        reasons.append(image_result["reason"])

    if score <= 30:
        verdict = "Likely Genuine"
    elif score <= 60:
        verdict = "Suspicious"
    else:
        verdict = "Likely Fake"

    return {
        "risk_score": score,
        "verdict": verdict,
        "reasons": reasons
    }


if __name__ == "__main__":
    profile_url = input("Enter profile URL: ")
    image_url = input("Enter profile image URL: ")

    result = analyze_profile(profile_url, image_url)

    print("\n--- Analysis Result ---")
    print("Risk Score:", result["risk_score"])
    print("Verdict:", result["verdict"])
    print("Reasons:")
    for r in result["reasons"]:
        print("-", r)
# -------- PDF REPORT GENERATION --------
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import os

report_folder = os.path.join("..", "Report")
os.makedirs(report_folder, exist_ok=True)

pdf_path = os.path.join(report_folder, "Fake_Social_Media_Profile_Detection_Report.pdf")

doc = SimpleDocTemplate(pdf_path)
styles = getSampleStyleSheet()
content = []

content.append(Paragraph("<b>Fake Social Media Profile Detection Report</b>", styles["Title"]))
content.append(Spacer(1, 20))

content.append(Paragraph("<b>Objective</b>", styles["Heading2"]))
content.append(Paragraph("To detect fake social media profiles using OSINT-based techniques.", styles["Normal"]))
content.append(Spacer(1, 12))

content.append(Paragraph("<b>Methodology</b>", styles["Heading2"]))
content.append(Paragraph("Profile data is analyzed, profile images are checked, and a risk score is generated.", styles["Normal"]))
content.append(Spacer(1, 12))

content.append(Paragraph("<b>Technology Stack</b>", styles["Heading2"]))
content.append(Paragraph("Python, BeautifulSoup, Requests, HTML, CSS, JavaScript.", styles["Normal"]))
content.append(Spacer(1, 12))

content.append(Paragraph("<b>Conclusion</b>", styles["Heading2"]))
content.append(Paragraph("The system successfully classifies profiles as Genuine, Suspicious, or Fake.", styles["Normal"]))

doc.build(content)

print("PDF report generated successfully!")
# -------- END OF REPORT --------
