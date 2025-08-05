# Credit Risk Scoring Application

This project is a web-based credit risk scoring application that allows users to input personal and financial data to assess their credit risk level. It features real-time inline validation, server-side checks, and a responsive UI styled with Tailwind CSS.

## Features

- Form with real-time inline validation for:
  - National ID (8 or 9 digits)
  - Age (18–100)
  - Monthly income and household income (> 0)
  - Required field selections
- Tailwind CSS styling matching modern UX standards
- Flask backend integration
- Error feedback via inline messages and server-side flash messages

## Technologies Used

- HTML
- JavaScript
- Tailwind CSS
- Python (Flask)
- Git & GitHub

## Folder Structure

```
project/
│
├── static/
│   └── tailwind.css
│
├── templates/
│   └── form.html
│
├── app.py
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/credit-risk-scoring.git
   cd credit-risk-scoring
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install flask
   ```

3. Run the Flask app:
   ```bash
   flask run
   ```

4. Open your browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## Screenshot

![Form Screenshot](screenshot.png)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)

## Author

Created by Tevin Mwaura Migwi