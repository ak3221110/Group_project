# Bihar Darshan Web Application

This is a Flask-based web application that provides information about various cultural, natural, historical, and wildlife attractions in Bihar, India. The application fetches data from multiple CSV files and allows users to search across all categories.

## Features

- Browse information on religious places, natural attractions, cultural heritage spots, wildlife eco-tourism, adventure locations, political and historical leaders, artists, musicians, and more.
- Search functionality that fetches data from all CSV files to provide comprehensive results.
- Organized data presentation with dedicated pages for different categories.
- Responsive and user-friendly interface.

## Project Structure

- `bihar_project/app.py`: Main Flask application with routes and search functionality.
- `bihar_project/templates/`: HTML templates for rendering pages.
- `bihar_project/data/`: CSV data files containing information about Bihar's attractions and notable personalities.
- `requirements.txt`: Python dependencies for the project.

## Setup and Installation

1. Clone the repository or download the project files.
2. Ensure Python 3.7+ is installed on your system.
3. Install dependencies using pip:

   ```
   pip install -r requirements.txt
   ```

4. Run the Flask application:

   ```
   python bihar_project/app.py
   ```

5. Open your browser and navigate to `http://127.0.0.1:5000/` to access the application.

## Usage

- Use the search bar on the homepage to search for any term across all categories.
- Navigate through different sections using the navigation bar.
- Explore detailed information on various cultural, natural, and historical sites.

## Notes

- The data is sourced from multiple CSV files located in the `data` directory.
- Ensure the CSV files maintain consistent column headers as per the project requirements for accurate search results.

## License

This project is open-source and free to use.

## Contact

For any queries or contributions, please contact the project maintainer.
