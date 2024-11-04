# Django Basic Electronic Shop

Welcome to the Django Basic Electronic Shop project! This web application allows users to browse and purchase electronic products in a user-friendly interface. Built with Django, this project serves as a foundational demonstration of building an e-commerce website with various functionalities.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **User Authentication:** Register, login, and logout functionality for users.
- **Product Listings:** Browse through a wide range of electronic products with images, descriptions, and prices.
- **Product Detail Page:** View detailed information about each product.
- **Cart Functionality:** Add products to a shopping cart.
- **Checkout Process:** Complete purchases through a simple checkout process.
- **Admin Dashboard:** Manage products, orders, and users from the Django admin panel.

## Technologies Used

- **Django:** A high-level Python Web framework for rapid development.
- **Python:** The programming language used for writing the application.
- **SQLite:** Default database used for local development (can be switched to PostgreSQL or another database).
- **HTML/CSS:** Markup and style for designing the frontend of the application.
- 
## Installation

To get started with the Django Basic Electronic Shop project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/electronic-shop.git
   cd electronic-shop
   ```

2. **Create a Virtual Environment:**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database:**
   Run migrations to set up your database.
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser:**
   Create an admin account to access the admin dashboard.
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**
   Start the server to view the application in your browser.
   ```bash
   python manage.py runserver
   ```
   Navigate to `http://127.0.0.1:8000/` in your browser to view the application.

## Usage

1. **Access the Website:** Open your browser and navigate to `http://127.0.0.1:8000/`.
2. **Register/Login:** Create a new account or log in with existing credentials.
3. **Browse Products:** Explore different electronic products available in the shop.
4. **Add to Cart:** Click on the product to view details and add it to your shopping cart.
5. **Checkout:** Proceed to checkout to complete your purchase.

## Contributing

Contributions are welcome! Here’s how you can help:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push to your branch and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any inquiries or feedback, feel free to reach out:

- Your Name: Maziyar kolagar
- Gmail: [Maziyarkolagar@gmail.com]

---

Thank you for checking out the Django Basic Electronic Shop project! Happy coding!
