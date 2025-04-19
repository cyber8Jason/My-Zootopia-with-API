# 🦊 Zootopia Animal Info Website (API Edition)

This Python project allows users to generate an HTML website that displays animal information fetched from the [API Ninjas Animal API](https://api-ninjas.com/api/animals).

## 📦 Features

- User can input any animal name (e.g., `fox`, `lion`, `penguin`)
- Information is fetched from the API
- A styled HTML page is generated using a pre-made template
- Displays characteristics like diet, location, and type
- Handles cases when the animal doesn’t exist

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/zootopia-api.git
   cd zootopia-api

2. Create and fill a .env file:
    ```bash
    API_KEY=your_api_key_here

3. Install requirements
    ```bash
   pip install requests
   
4. Run the script:
    ```bash
   python3 animals_web_generator.py

5. Open animals.html in your browser to view the result.

## 📁 File Structure
    zootopia-api/
    │
    ├── animals_web_generator.py    # Main Python script
    ├── animals_template.html       # HTML template
    ├── .env                        # Contains your API key (not pushed to GitHub)
    ├── .gitignore                  # Prevents sensitive files from being tracked
    ├── animals.html                # Output website (generated)
    └── README.md                   # Project description

## ⚠️ Note
- Make sure your .env file is listed in .gitignore to avoid accidentally pushing your API key.
- If the animal doesn’t exist, a message will be shown in the HTML.    

---
MIT License

Copyright (c) 2025 cyber8Jason

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.