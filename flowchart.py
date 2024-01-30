from PIL import Image, ImageDraw, ImageFont

def draw_text(draw, position, text, font=None, max_width=None):
    margin = 10
    line_height = 20

    x, y = position

    if font is None:
        font = ImageFont.load_default()

    lines = [text]

    if max_width:
        words = text.split()
        lines = []
        current_line = ""

        for word in words:
            if font.getsize(current_line + word)[0] <= max_width:
                current_line += f"{word} "
            else:
                lines.append(current_line)
                current_line = f"{word} "

        lines.append(current_line)

    for line in lines:
        draw.text((x + margin, y), line, font=font, fill="black")
        y += line_height

def create_image():
    image_width = 800
    image_height = 600
    background_color = "white"

    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()

    draw_text(draw, (10, 10), "- Main Folder: Assets", font=font)
    draw_text(draw, (30, 40), "  - Packages", font=font)

    # Draw the Asset Folder and its subfolders
    draw_text(draw, (30, 70), "- Asset Folder", font=font)
    draw_text(draw, (50, 100), "  - Apartment_Door", font=font)
    draw_text(draw, (50, 130), "  - diningRoom", font=font)
    draw_text(draw, (50, 160), "  - Monqo Flower Ceramic Vases (for flowers)", font=font)
    draw_text(draw, (50, 190), "  - New Home (My Main House)", font=font)

    # Draw the Scene Folder and its subfolders
    draw_text(draw, (30, 240), "- Scene Folder", font=font)
    draw_text(draw, (50, 270), "  - Roomception", font=font)
    draw_text(draw, (70, 300), "    - Backgrounds (In this section, background sections are placed)", font=font)
    draw_text(draw, (70, 330), "    - buttons (In this section, buttons are placed)", font=font)
    draw_text(draw, (70, 360), "    - Materials (In this section, all colors are placed)", font=font)
    draw_text(draw, (70, 390), "    - Scenes", font=font)
    draw_text(draw, (90, 420), "      - MainScene (In this section, the Main scene is placed)", font=font)
    draw_text(draw, (70, 450), "    - Script (Multiple C# codes placed, which are for game scripts)", font=font)
    draw_text(draw, (70, 480), "    - Sounds (All sound files are located here)", font=font)
    draw_text(draw, (70, 510), "    - tulipan (Different types of flowers placed here, downloaded from Unity Asset Store)", font=font)

    image.save("UnitySceneStructure.png")

if __name__ == "__main__":
    create_image()
