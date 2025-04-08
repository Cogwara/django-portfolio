# Chris Portfolio Website

This is a personal portfolio website built using Django. It showcases my skills, experience, education, projects, and blog posts. It also includes a contact form for visitors to send me messages.

## Features

*   **Profile:** Displays information about me (name, title, description, avatar, social links, etc.).
*   **Expertise:** Highlights my areas of expertise with titles, descriptions, and icons.
*   **Experience:** Shows my work experience details (start date, end date, position, company, description).
*   **Education:** Lists my education history (start date, end date, degree, institution, description).
*   **Skills:** Represents my skills with names and proficiency percentages.
*   **Services:** Describes the services I offer with titles, descriptions, and icons.
*   **Project Categories:** Organizes projects into categories.
*   **Projects:** Showcases my projects with titles, descriptions, images, dates, and links.
*   **Blog Posts:** Features blog posts with titles, content, excerpts, images, dates, authors, likes, and comments.
*   **Contact Form:** Allows visitors to send me messages, which are stored in the database and sent to my email address.
*   **Category Filtering:** Portfolio items can be filtered by category.

## Technologies Used

*   Python
*   Django
*   HTML
*   CSS
*   JavaScript (optional, for enhanced filtering)
*   PostgreSQL (or your preferred database)

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd [project_directory]
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the database:**

    *   Create a PostgreSQL database (or your preferred database).
    *   Update the `DATABASES` settings in `chris_portfolio/settings.py` with your database credentials.

5.  **Set up email settings:**

    *   Configure the email settings in `chris_portfolio/settings.py` (e.g., `EMAIL_BACKEND`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`).
    *   If using Gmail, generate an App Password and use that as the `EMAIL_HOST_PASSWORD`.

6.  **Run migrations:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7.  **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

8.  **Collect static files:**

    ```bash
    python manage.py collectstatic
    ```

9.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

10. **Access the website:**

    *   Open your web browser and go to `http://localhost:8000/`.
    *   Access the admin interface at `http://localhost:8000/admin/` and log in with the superuser credentials you created.

## Models

*   `Profile`: Stores profile information.
*   `Expertise`: Stores expertise information.
*   `Experience`: Stores experience information.
*   `Education`: Stores education information.
*   `Skill`: Stores skill information.
*   `Service`: Stores service information.
*   `ProjectCategory`: Stores project categories.
*   `Project`: Stores project information.
*   `BlogPost`: Stores blog post information.
*   `ContactMessage`: Stores contact message information.
*   `PortfolioItem`: Stores portfolio item information.

## Views

*   `HomeView`: Displays the home page.
*   `ProjectListView`: Displays a list of projects.
*   `BlogListView`: Displays a list of blog posts.
*   `BlogDetailView`: Displays a single blog post.
*   `contact_view`: Handles the contact form submission.
*   `contact_success_view`: Displays the contact success page.

## Templates

The templates are located in the `chris_portfolio/portfolio/templates/portfolio/` directory.

*   `index.html`: The home page template.
*   `projects.html`: The projects page template.
*   `blog.html`: The blog page template.
*   `blog_detail.html`: The blog detail page template.
*   `contact.html`: The contact form template.
*   `contact_success.html`: The contact success page template.
*   `base.html`: The base template for all pages.

## Contributing

Contributions are welcome! Please feel free to submit pull requests with bug fixes, new features, or improvements to the documentation.

## License

[Specify the license here, e.g., MIT License]
