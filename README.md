# Elemental - An Interactive Periodic Table

This project is a desktop application created with Python that displays an interactive periodic table. When a user clicks on an element, a popup window appears with detailed information about that element, and the information is simultaneously read aloud using text-to-speech.

---

## Features

*   **Interactive GUI:** A visually organized periodic table built with `tkinter`.
*   **Detailed Element Information:** Clicking an element reveals key properties:
    *   Name & Symbol
    *   Atomic Number
    *   Chemical Group & Phase at STP
    *   Melting & Boiling Points
    *   Electronegativity
    *   Common Oxidation States
    *   Number of Valence Electrons
*   **Text-to-Speech:** Element information is read aloud using Google's Text-to-Speech (gTTS) engine.
*   **Color-Coded Legend:** A simple legend helps users identify different chemical groups at a glance.
*   **Data-Driven:** The table is dynamically generated from an external `periodic_table_data.csv` file, making it easy to manage.

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

You will need Python 3 installed on your system. The application relies on the following Python libraries:

*   `pandas`
*   `gTTS`
*   `pygame`

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
    cd YOUR_REPOSITORY
    ```
    *(Remember to replace `YOUR_USERNAME` and `YOUR_REPOSITORY` with your actual GitHub details)*

2.  **Install the required libraries:**
    Create a `requirements.txt` file with the following content:
    ```
    pandas
    gTTS
    pygame
    ```
    Then, install them using pip:
    ```sh
    pip install -r requirements.txt
    ```
    Alternatively, you can install them one by one:
    ```sh
    pip install pandas gtts pygame
    ```

---

## Usage

Ensure the `periodic_table_data.csv` file is in the same directory as the Python script. To run the application, execute the following command in your terminal:

```sh
python name_of_your_script.py
```

This will launch the interactive periodic table window. Click on any element to see its details and hear them spoken.

---

## How It Works

*   **GUI (`tkinter`):** The main application window and all widgets (buttons, labels, popups) are created and managed by `tkinter`.
*   **Data Management (`pandas`):** The `periodic_table_data.csv` is loaded into a pandas DataFrame at startup for easy access and iteration.
*   **Text-to-Speech (`gTTS`):** When an element is clicked, the `gTTS` library is used to send the element's information as text to the Google Translate API, which returns an MP3 audio file.
*   **Audio Playback (`pygame`):** The `pygame.mixer` module is used to load and play the generated MP3 file, providing the audio narration. It is also used to properly stop the audio when a new element is clicked or the popup is closed.
*   **Temporary Files (`tempfile`):** The generated MP3 audio is saved as a temporary file to avoid cluttering the project directory.

---
