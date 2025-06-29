# 📚 My E-Learning Platform

## Overview

Welcome to **Learnopath**! This is a simple yet functional e-learning platform template designed to facilitate online learning experiences. It allows users to browse courses, watch video content, and manage their learning progress. Built with a focus on simplicity and scalability for small to medium-sized educational content, this platform serves as a solid foundation for your online learning initiatives.

## Features

* **User Authentication:** Secure user registration and login system.
* **Course Management:** Organize and display various courses.
* **Video Playback:** Seamless integration for playing video content (via YouTube embeds for efficient streaming).
* **Responsive Design:** (If applicable) Adapts to various screen sizes for a consistent user experience on desktop and mobile devices.
* **Local Database:** Uses SQLite for easy setup and local data storage during development.

## Technologies Used

* **Backend:**
    * Python 3.x
    * Flask: A lightweight and flexible web framework.
    * Flask-SQLAlchemy: ORM for database interactions.
    * SQLite: A file-based SQL database, ideal for local development and small-scale deployments.
    * Werkzeug.security (for password hashing): (If implemented) Securely handles user passwords.
* **Frontend:**
    * HTML5: Structure of the web pages.
    * CSS3: Styling and visual presentation.
    * JavaScript: (Minimal, for interactive elements like video playback if custom controls are used, or just for form validation etc.)
* **Database Tool:**
    * SQLAlchemy: (Underneath Flask-SQLAlchemy)
