# Wisdom is Silente
#### Video Demo:  <URL HERE>
#### Description:

## Creator info
`Name:`    =>  Carlos Mendes
`GitHub:`  =>  Carluuz
`edX:`     =>  Carluuz
`Origin:`  =>  Braga, Portugal


## Program Functionality Overview
This project is designed to automate the process of gathering, processing, and displaying quotes from popular authors. It consists of several interconnected programs, each serving a specific purpose in the overall workflow. Here's a brief overview of each program's functionality:

### `project.py`
- **Purpose:** Acts as the main entry point for the project, orchestrating the execution of other programs in a sequential manner. It ensures that all necessary data is gathered, processed, and displayed in a cohesive manner.
- **Key Features:** Manages the flow of data between different stages of the project, including scraping quotes from GoodReads, creating images of quotes, uploading these images to Google Drive, and updating Google Sheets with relevant information.

### `get_files.py`
- **Purpose:** Scrapes quotes from the popular quotes page on GoodReads.com. It filters out quotes from authors who are not considered to be free to use, based on their birth and death dates.
- **Key Features:** Utilizes web scraping techniques to gather quotes and their corresponding authors. It also maintains lists of authors to be blocked or allowed (green-listed) based on their eligibility for use.

### `death.py`
- **Purpose:** Determines whether an author is considered to be free to use based on their birth and death dates. This is a crucial step in filtering out quotes from authors whose works may not be freely available.
- **Key Features:** Uses Google search to find birth and death dates of authors, then applies specific criteria to determine their eligibility for use.

### `make_pic.py`
- **Purpose:** Creates images of quotes using predefined templates. These images are then used for display or further processing.
- **Key Features:** Utilizes the Python Imaging Library (PIL) to generate images from quotes. It supports the use of multiple templates and automatically adjusts the layout based on the quote's length and content.

### `upload_image.py`
- **Purpose:** Uploads the generated images of quotes to a specified Google Drive folder. This allows for easy sharing and distribution of the quotes.
- **Key Features:** Authenticates with Google Drive using a service account, uploads images, and maintains a list of uploaded image URLs for reference.

### `sheets_update.py`
- **Purpose:** Updates a Google Sheets document with information gathered during the project's execution. This includes lists of blocked and allowed authors, URLs of uploaded images, and the quotes themselves.
- **Key Features:** Connects to Google Sheets using the Google Sheets API, updates specified columns with new data, and ensures that the data is organized and accessible.

This project demonstrates the power of automation in gathering, processing, and displaying quotes from popular authors, showcasing the capabilities of web scraping, image generation, and integration with cloud services like Google Drive and Google Sheets.


## Skills/Knowledge requirement
To successfully undertake a project similar to this one, one would need to acquire or have a solid understanding of the following skills and technologies:

### `Programming Languages`
- **Python:** The core language used in this project, known for its simplicity and versatility, especially in web scraping, data manipulation, and automation tasks.

### `Web Scraping`
- **BeautifulSoup:** A Python library used for parsing HTML and XML documents, making it easier to extract data from websites.
- **Requests:** A Python library for making HTTP requests, which is essential for fetching web pages for scraping.

### `Image Processing`
- **Pillow (PIL):** A Python Imaging Library that adds image processing capabilities to your Python interpreter. It's used for opening, manipulating, and saving many different image file formats.

### `Cloud Services`
- **Google Drive API:** Knowledge of how to authenticate and interact with Google Drive to upload and manage files programmatically.
- **Google Sheets API:** Understanding of how to connect to Google Sheets, read from, and write to spreadsheets using the API.

### `JSON and File Handling`
- **JSON:** Familiarity with JSON format for data interchange, including reading from and writing to JSON files in Python.
- **File Handling:** Basic knowledge of how to read from and write to files in Python, which is crucial for managing data and configuration files.

### `Regular Expressions`
- **Regex:** Understanding of regular expressions for pattern matching and text manipulation, which can be particularly useful for parsing and cleaning data.

### `Web Development Basics`
- **HTML/CSS:** Basic understanding of HTML and CSS, as web scraping often involves navigating and understanding the structure of web pages.

### `APIs and Authentication`
- **OAuth2:** Familiarity with OAuth2, a protocol that allows applications to gain limited access to user accounts on an HTTP service, which is often required for accessing cloud services like Google Drive and Sheets.

### `Version Control`
- **Git:** Basic knowledge of using Git for version control, which is essential for managing and collaborating on code projects.

### `Problem-Solving and Debugging`
- **Debugging:** Ability to troubleshoot and debug code, as projects involving web scraping, API interactions, and file manipulation can encounter various issues.

### `Project Management`
- **Agile Methodologies:** Familiarity with Agile methodologies, such as Scrum or Kanban, can be beneficial for managing the project's workflow and iterating on the project.

By acquiring or strengthening these skills, one would be well-equipped to undertake a project similar to this one, leveraging web scraping, automation, and cloud services to gather, process, and display quotes from popular authors.