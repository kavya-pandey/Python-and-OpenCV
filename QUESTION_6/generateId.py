import pandas as pd
from PIL import Image, ImageDraw, ImageFont

df = pd.read_csv("students.csv")

records = df.to_dict(orient='record')
font = ImageFont.truetype("OpenSans-Semibold.ttf", size=25)

def generate_card(data):
    template = Image.open("C:/Users/KAVYA/Desktop/7th sem/Assignment_1/QUESTION_1/ID_Card_Template-1.jpeg")
    pic = Image.open(f"photos/{data['id']}.jpg").resize((165, 190), Image.ANTIALIAS)
    template.paste(pic, (25, 75, 190, 265))
    draw = ImageDraw.Draw(template)
    draw.text((315, 80), str(data['id']), font=font, fill='black')
    draw.text((315, 125), data['name'], font=font, fill='black')
    draw.text((315, 170), data['semester'], font=font, fill='black')
    draw.text((315, 215), data['dob'], font=font, fill='black')
    return template
for record in records:
    card = generate_card(record)
    card.save(f"cards/{record['id']}.jpg")