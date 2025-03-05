---

# VCF Viewer App

This is a Python-based mobile application built with KivyMD, designed to load and display contact information from a VCF (vCard) file. The app allows users to choose a VCF file, view the contact details, and interact with the app using an intuitive interface. It also includes an "About Us" screen where users can contact the developers through Telegram.

## Features:
- **VCF File Selection:** Choose a VCF file from the device.
- **Contact Display:** View contacts in the VCF file, showing names and phone numbers.
- **About Us:** Access a page with information and contact links to the developers via Telegram.

## Installation:
To use this app, you need to install the following dependencies:

1. **Python** (version 3.7 or higher)
2. **KivyMD** for the UI components
3. **Plyer** for file system interaction

You can install the required dependencies using pip:

```bash
pip install kivymd plyer
```

## Usage:

1. **Running the App:**
   - After installing the dependencies, run the script by executing:
   ```bash
   python app_name.py
   ```
   
2. **Selecting a VCF File:**
   - Once the app is running, press the "Choose your vcf file" button to open a file chooser dialog.
   - Select a `.vcf` file to load and view the contacts.

3. **Viewing Contacts:**
   - The contacts from the VCF file will be displayed in a list, showing the names and corresponding phone numbers.
   
4. **About Us Page:**
   - Tap the right menu on the top app bar to open the "About Us" page with information and a contact link.

## How It Works:

The app uses the `filechooser` module from **Plyer** to let users select a `.vcf` file. It reads the content of the file and extracts contact information using regular expressions. The extracted contacts are displayed in a list, and users can easily view the details.

The app uses KivyMD components such as `MDTextButton`, `MDTopAppBar`, and `MDList` for the user interface, and it utilizes Kivy's `ScreenManager` for navigation between different screens.

## File Structure:

- **app_name.py:** Main Python file containing the app's logic.
- **image_phone.jpg:** Image used in the UI.
- **vcf_image.ico:** Icon used for the button.
- **logo6_16_21816.png:** Logo image for the "About Us" page.

## Screens:

1. **Welcome Screen:** Displays a welcome message and a button to choose a VCF file.
2. **VCF File Screen:** Displays the contact list after a VCF file is selected.
3. **About Us Screen:** Provides contact information and a link to contact the developers on Telegram.

## Contact Us:

- For any issues or feedback, please contact the developer via Telegram: [@Thekingdynamo](https://t.me/Thekingdynamo).

---
