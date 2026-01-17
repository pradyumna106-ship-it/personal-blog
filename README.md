# Personal Blog Project

This is a simple personal blog application that allows the admin to write, publish, edit, and delete articles. Visitors (guests) can view published articles but cannot modify them.  

The project is divided into two sections: **Guest Section** and **Admin Section**.

---

## Features

### Guest Section
- **Home Page:** Displays a list of all published articles.
- **Article Page:** Displays the content of a selected article along with its date of publication.

### Admin Section
- **Dashboard:** Displays a list of all articles with options to add, edit, or delete articles.
- **Add Article Page:** Form to add a new article with fields:
  - Title
  - Content
  - Date of Publication
- **Edit Article Page:** Form to edit an existing article with fields:
  - Title
  - Content
  - Date of Publication
- **Delete Article:** Option to delete an article from the blog.

---

## Project Structure
<br>
<pre><Detail>
personal_blog/
├─ articles/ # Directory to store articles as JSON or Markdown files
├─ templates/ # HTML templates for frontend pages
│ ├─ home.html
│ ├─ article.html
│ ├─ dashboard.html
│ ├─ add_article.html
│ └─ edit_article.html
├─ static/ # CSS files for styling
│ └─ style.css
├─ app.py / main.py # Backend server file
├─ README.md # Project documentation
└─ requirements.txt # Python dependencies (if using Python)
</Detail></pre>

link: https://roadmap.sh/projects/personal-blog
---

## Storage
- Articles are stored as separate files in the `articles/` directory.
- Each article contains:
  - `title`: Title of the article
  - `content`: Article content
  - `date`: Date of publication
- You can use **JSON** or **Markdown** format for storing articles.

Example JSON structure:

```json
{
  "title": "Understanding Time Travel",
  "content": "Time travel is not about moving clocks, but bending reality...",
  "date": "2026-01-12"
}
