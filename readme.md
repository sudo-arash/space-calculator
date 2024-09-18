# 🚀 Space Calculator 🌌

[View the website >>](https://ghalbeyou6.pythonanywhere.com/)
Welcome to the Space Calcuator! This web application allows you to perform various space-related calculations, including:

- Calculating when planets are aligned.
- Determining the Schwarzschild radius of black holes.
- Choosing between predefined stars or custom star masses.

## Features ✨

- **🌍 Planet Alignment Calculation**: Input two planets and a date (or let the system automatically calculate future alignments within a specified number of years).
- **🌌 Schwarzschild Radius Calculation**: Choose from a list of stars or input a custom mass to calculate the Schwarzschild radius of a black hole.
and more to come!
## Getting Started 🚀

### Prerequisites 📦

Ensure you have the following installed:

- Python 3.x
- Flask
- Astropy

### Installation 🛠️

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sudo-arash/space-calculator.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd space-calculator
   ```

3. **Install the required packages:**

   ```bash
   pip install astropy flask
   ```

### Running the Application 🏃

1. **Start the Flask server:**

   ```bash
   python app.py
   ```

2. **Open your browser and visit:**

   ```
   http://127.0.0.1:5000
   ```

### Usage 🌟

1. **Planet Alignment:**
   - Select two planets from the dropdown menu.
   - Choose a specific date or let the application find the next alignment automatically.
   - Click "Calculate" to see the results!

2. **Schwarzschild Radius:**
   - Choose a star from the list or enter a custom mass in solar masses.
   - Click "Calculate" to find out the Schwarzschild radius of a black hole for the selected star or mass.

## Code Structure 📁

- **`app.py`**: Contains the Flask routes and logic for calculations.
- **`templates/index.html`**: The main HTML file with forms and results display.
- **`static/`**: Contains static files like CSS and JavaScript.

## Contributing 🤝

If you would like to contribute to this project, please follow these steps:

1. **Fork the repository.**
2. **Create a new branch:**

   ```bash
   git checkout -b feature-branch
   ```

3. **Make your changes and commit:**

   ```bash
   git commit -m "Add feature"
   ```

4. **Push to the branch:**

   ```bash
   git push origin feature-branch
   ```

5. **Create a pull request.**

## License 📝

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments 🙏

- Thanks to the Astropy library for its powerful astronomical computations.
- Special thanks to all contributors and users who provide feedback!

---

Feel free to reach out if you have any questions or suggestions 🌠
