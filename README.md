
# Rick it 🎵🕺

a Python-based app that, when launched, displays an image of Rick Astley with a transparent background over your desktop and plays the Rickroll song. You won’t be able to close it manually , the image stays on screen until the song finishes, then disappears on its own.

<p align="center">
  <img src="Source%20Code/rick.png" width="300" />
</p>




---

##  Requirements

to run the script, install the required Python packages:

```bash
pip install PyQt5 playsound
```


---

## 🛠 How to Build the `.exe` File

Make sure [PyInstaller](https://pyinstaller.org/) is installed:

```bash
pip install pyinstaller
```

Then run this command to convert your Python script into a Windows executable:

```bash
pyinstaller --onefile --noconsole --add-data "rick.png;." --add-data "rickr.mp3;." rickroll.py
```

- The `.exe` will be located in the `dist/` folder.
- `--noconsole` hides the terminal window.
- `--add-data` embeds the audio and image files into the `.exe`.

---

##  Git Commands Used

```bash
# Clone the repo
git clone https://github.com/issoupewd/RickRoll.git
cd RickRoll

# Add project files to the repo
git add .
git commit -m "text  text"

# Push to GitHub
git push
```

---

##  Notes

- Tested on Windows.
- This app is just for fun 


