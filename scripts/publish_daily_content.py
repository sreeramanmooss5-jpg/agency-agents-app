import os
import requests
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# --- BRAND CONFIGURATION & GUARDRAILS ---
INSTITUTION_NAME = "Ashtavaidyan Pulamanthole Mooss Ayurveda Hospital & Pharmaceuticals"
LOCATION = "Pulamanthole, Malappuram, Kerala (Est. 1795)"
ACCREDITATION = "ROHINI Registration Certified Hospital"
BOOKING_PHONE = "+91 9778004082"
WEB_HOSPITAL = "https://www.pulamantholemoosshospital.com"
WEB_PHARMA = "https://www.pulamantholemooss.com"

UNIVERSAL_HASHTAGS = (
    "#pulamantholemoooss #pulamantholemooss #rohiniregistered "
    "#ayurveda #keralaayurveda #ayurvedalifestyle #holistichealth "
    "#naturalhealing #ashtavaidya #wellnessjourney #healthylifestyle "
    "#traditionalmedicine #ayurvedicmedicine #panchakarma #healthtips "
    "#guthealth #longevity #mindbodyhealing #naturalremedies #selfcare "
    "#keralatourism #malappuram #perinthalmanna #kerala #indiawellness"
)

COLOR_CORE = "#174A3A"
COLOR_PAPER = "#F8F5EE"
COLOR_INK = "#1A1A1A"
COLOR_GOLD = "#B58A3A"

def generate_carousel_slide(slide_number, title_text, body_text, output_path):
    width, height = 1080, 1350
    is_dark = (slide_number % 2 == 0)
    bg_color = COLOR_INK if is_dark else COLOR_PAPER
    text_color = COLOR_PAPER if is_dark else COLOR_INK
    accent_color = COLOR_GOLD if is_dark else COLOR_CORE
    
    image = Image.new("RGB", (width, height), color=bg_color)
    draw = ImageDraw.Draw(image)
    
    try:
        title_font = ImageFont.truetype("fonts/PlayfairDisplay-Bold.ttf", 64)
        body_font = ImageFont.truetype("fonts/DMSans-Regular.ttf", 40)
        footer_font = ImageFont.truetype("fonts/DMSans-Medium.ttf", 28)
    except IOError:
        title_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()

    progress_width = int((width / 7) * slide_number)
    draw.rectangle([0, 0, progress_width, 12], fill=accent_color)
    
    draw.text((80, 100), "ASHTAVAIDYAN PULAMANTHOLE MOOSS", fill=accent_color, font=footer_font)
    draw.text((80, 140), ACCREDITATION, fill=accent_color, font=footer_font)
    
    draw.text((80, 320), title_text, fill=text_color, font=title_font)
    
    margin_x, current_y = 80, 520
    max_width_chars = 38
    words = body_text.split()
    line = ""
    for word in words:
        test_line = line + word + " "
        if len(test_line) > max_width_chars:
            draw.text((margin_x, current_y), line, fill=text_color, font=body_font)
            current_y += 65
            line = word + " "
        else:
            line = test_line
    if line:
        draw.text((margin_x, current_y), line, fill=text_color, font=body_font)

    footer_text = f"Slide {slide_number}/7 | 📞 {BOOKING_PHONE}"
    draw.text((80, 1220), footer_text, fill=accent_color, font=footer_font)
    
    image.save(output_path, "JPEG", quality=95)
    return output_path

if __name__ == "__main__":
    print("=== PULAMANTHOLE MOOSS: PUBLISHING SCRIPT INITIALIZED ===")
    os.makedirs("output", exist_ok=True)
    for i in range(1, 8):
        generate_carousel_slide(i, f"Pillar {i}: Heritage Healing", "Authentic classical Ayurveda treatments rooted in 500+ years of Ashtavaidya tradition.", f"output/slide_{i}.jpg")
    print("Successfully rendered 7-slide carousel deck.")
