# landing.py

from pywebio import start_server
from pywebio.output import put_image, put_html, put_buttons, clear
from main import main  # Import the tutorial entry function

def landing():
    # Display the pixelated Standard Model logo
    with open("assets/qubitquest_logo_pixelated.png", "rb") as f:
        img_data = f.read()
    put_image(img_data)

    # One-sentence description
    put_html(
        "<p style='font-family: monospace; font-size: 16px;'>"
        "Enter the quantum realm where real particles, real math, and real code power your quest "
        "for fundamental understanding."
        "</p>"
    )

    # “▶ Begin QubitQuest” button: when clicked, clear the landing page and call main()
    put_buttons(
        ["▶ Begin QubitQuest"],
        onclick=[lambda: _enter_tutorial()]
    )

def _enter_tutorial():
    """
    Clear the landing page and invoke the main() function
    to start the QubitQuest tutorial directly.
    """
    clear()
    main()

if __name__ == "__main__":
    # Serve only the landing() function, with MathJax enabled via CDN
    start_server(landing, port=8080, cdn=True)

