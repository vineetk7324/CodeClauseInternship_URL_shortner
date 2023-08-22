# CodeClauseInternship_URL_shortner

This is a basic URL shortener application built using Python. The application allows users to enter a long URL, generates a short URL, and provides redirection to the original URL.

Features
Converts long URLs into short, shareable links.
Stores the short URLs and their corresponding original URLs in memory (non-persistent storage).
Basic web interface to interact with the URL shortener.
Requirements
Python 3.x
Libraries: Flask, shortuuid
Installation
Clone or download the repository to your local machine.

Install the required libraries using the following command:

pip install Flask shortuuid
Run the script:

python url_shortener.py
Open a web browser and navigate to http://localhost:5000/ to access the URL shortener interface.

Usage
Open the provided URL in your web browser.
Enter a long URL in the input field and click the "Shorten" button.
The application will generate a short URL and display it on the page.
Click on the generated short URL to be redirected to the original long URL.
