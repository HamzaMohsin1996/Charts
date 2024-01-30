from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

# Define your project information
metadata = {
    "Hamza Mohsin": {
        "Role": "Lead Developer & Design Artist",
        "Experience": "4 years in front-end development",
        "Contribution": [
            "Transitioned from front-end development to Unity game development during the project.",
            "Proficient in C# for Unity functions.",
            "Implemented VR-specific elements like background sounds, particle systems, and terrains.",
            "Customized XR interactables for a more immersive experience.",
        ],
        "Project Management": "Successfully led the team, coordinated efforts, and managed project tasks.",
    },
    "Usama Asif": {
        "Role": "Art Sound Designer",
        "Experience": "Specialized in art sound design",
        "Contribution": [
            "Created and implemented sound design elements for the project.",
            "Assisted in the development of documentation, ensuring a comprehensive project overview.",
            "Contributed to finding necessary project assets, enhancing the overall project quality.",
        ],
    },
}

github_info = {
    "GitHub Link": "Roomception GitHub Repository(https://github.com/HamzaMohsin1996/Roomception)",
    "Contributors": "Markus Weißenberger and Joed Lopes da Silva have been added as contributors to the project.",
}

project_startup_instructions = [
    "To access the latest code, clone the project from the 'development' branch on GitHub.",
    "In Unity, navigate to Assets/Scenes/Roomception/Scenes/MainScene to open the main game scene.",
]

# Create a DataFrame for easier organization
metadata_df = pd.DataFrame(metadata).T

# Create a PDF
def generate_pdf():
    filename = "Roomception_Report.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, 750, "Roomception: The Button Flower Mystery Report")

    # Metadata
    c.setFont("Helvetica", 12)
    c.drawString(72, 720, "1. Metadata")
    for i, (name, details) in enumerate(metadata.items(), start=2):
        c.drawString(90, 720 - i * 15, f"{i}. {name}:")
        for j, (key, value) in enumerate(details.items(), start=1):
            c.drawString(108, 720 - (i * 15 + j * 12), f"{key}: {value}")

    # GitHub Information
    c.drawString(72, 580 - len(metadata) * 180, "GitHub Information:")
    for i, (key, value) in enumerate(github_info.items(), start=1):
        c.drawString(90, 580 - len(metadata) * 180 - i * 12, f"{key}: {value}")

    # Project Startup Instructions
    c.drawString(72, 480 - len(metadata) * 180, "Project Startup Instructions:")
    for i, instruction in enumerate(project_startup_instructions, start=1):
        c.drawString(90, 480 - len(metadata) * 180 - i * 12, f"{i}. {instruction}")

    # Save the PDF
    c.save()
    print(f"PDF Report generated successfully: {filename}")


# Run the function to generate the PDF
generate_pdf()
