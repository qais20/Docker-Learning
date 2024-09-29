# VisitCounterX

Welcome to **VisitCounterX**, my very first Flask web application! 🎉 This project represents my journey from an aspiring developer to successfully deploying a web app that tracks visits in real-time. I’ve put my heart and soul into this project, learning a ton along the way, and I’m excited to share it with you!

![VisitCounterX Screenshot](https://github.com/qais20/Docker-Learning/blob/b6b8cc21bee20448bebd7d5f2d969aed6aa92f7e/VisitCounterX-app/Screenshots/homepage%20-%20visitcounterx.jpg)

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [My Journey](#my-journey)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Application Walkthrough](#application-walkthrough)
  - [1. Home Page](#1-home-page)
  - [2. Visit Counter Page](#2-visit-counter-page)
  - [3. About Page](#3-about-page)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Real-Time Visit Counter**: Keeps track of the number of visits and stores the count in Redis.
- **Dynamic Progress Bar**: A visually appealing progress bar that fills based on the visit count.
- **Inspirational Quotes**: Every time you visit the counter page, you’ll see a random quote inspired by the sayings of **Prophet Muhammad (PBUH)**.
- **Dockerised Application**: I utilised Docker and Docker Compose to create a seamless development environment.
- **Responsive UI**: A clean and modern design that enhances user experience.
- **Nginx Load Balancing**: Ensures smooth handling of traffic and lays the groundwork for future scalability.


## Tech Stack
- **Backend**: Python (Flask)
- **Database**: Redis
- **Frontend**: HTML, CSS (custom styling)
- **Containerisation**: Docker, Docker Compose
- **Web Server**: Nginx
- **Deployment**: Nginx + uWSGI

## My Journey

This project marks my first foray into full-stack development and deployment. From the initial brainstorming to coding, testing, and finally deploying VisitCounterX, every step has been a valuable learning experience. 

**Key milestones in my journey:**
- **Learning Flask**: Diving into Flask was both challenging and rewarding. Building the routes and templates allowed me to understand web development principles.
- **Setting Up Redis**: Implementing Redis for the visit counter was an eye-opener. I learned about caching and data storage, which are critical for modern web applications.
- **Containerisation**: Discovering Docker and setting up a multi-container environment changed my perspective on application deployment. I can now build and run applications in isolated environments, making development smoother.
- **Deployment with Nginx**: Finally, I configured Nginx for load balancing, a crucial step for scalability. It was exhilarating to see my app go live!

This journey has ignited my passion for web development, and I can’t wait to build upon this foundation.

## Getting Started

### Prerequisites
Before you get started, make sure you have the following installed:
- **Python 3.8+**
- **Docker** and **Docker Compose**
- **Redis**

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/VisitCounterX.git
   cd VisitCounterX
   ```

2. **Set Up Virtual Environment (Optional)**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate  # For Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application Locally**:
   Start the Flask server using:
   ```bash
   flask run
   ```

5. **Run via Docker**:
   If you prefer running the app in a Docker container, use:
   ```bash
   docker-compose up --build
   ```

6. **Access the App**:
   Navigate to `http://localhost:7777` in your browser to see the application.

## Usage

Once the application is up and running, you can interact with it through the following pages:

- **Home Page** (`/`): This page welcomes users to VisitCounterX and provides links to the **About** and **Visit Counter** pages.
- **Visit Counter Page** (`/count`): Displays the current visit count, a progress bar, and a random quote.
- **About Page** (`/about`): Explains the purpose of the project and the technologies used.

## Application Walkthrough

### 1. Home Page

The home page is designed to welcome users to VisitCounterX. It features two buttons:
- **About**: Takes users to the About page.
- **Check Visit Counter**: Redirects users to the Visit Counter page where they can view the visit count.

![Home Page](https://github.com/qais20/Docker-Learning/blob/b6b8cc21bee20448bebd7d5f2d969aed6aa92f7e/VisitCounterX-app/Screenshots/homepage%20-%20visitcounterx.jpg)

### 2. Visit Counter Page

The Visit Counter page is the core feature of the app. It displays:
- **Visit Count**: Updated in real-time using Redis.
- **Dynamic Progress Bar**: Visually reflects the visit count.
- **Inspirational Quote**: A random quote from Prophet Muhammad (PBUH) is displayed at the bottom of the page.

You can customise the progress bar and background to fit the look and feel of your brand.

![Visit Counter Page](https://github.com/qais20/Docker-Learning/blob/b6b8cc21bee20448bebd7d5f2d969aed6aa92f7e/VisitCounterX-app/Screenshots/counter%20-%20visitcounterx.jpg) 

### 3. About Page

The About page provides a detailed overview of the project, including:
- The purpose of the app.
- The technologies used (Flask, Redis, Docker, Nginx).
- Future plans for the project.

![About Page](https://github.com/qais20/Docker-Learning/blob/b6b8cc21bee20448bebd7d5f2d969aed6aa92f7e/VisitCounterX-app/Screenshots/about%20-%20visitcounterx.jpg)

## Future Enhancements

VisitCounterX is just the beginning! I have plans to enhance the application further, including:
- **User Tracking**: Implementing user sessions for detailed visit statistics.
- **Interactive Maps**: Visualising the locations of visitors around the globe.
- **Advanced Analytics**: Adding data visualisation tools for deeper insights into visitor behaviour.
- **Scaling**: Improving the scalability of the app using Kubernetes.

## Contributing

If you want to contribute to VisitCounterX, feel free to fork the repository and submit pull requests. I welcome all contributions, including new features, bug fixes, and documentation improvements.

### Steps to Contribute:
1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit and push your changes.
5. Open a pull request.

For any questions or suggestions, feel free to open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/username/VisitCounterX/blob/main/LICENSE) file for details.

---

Thank you for taking the time to explore my project, **VisitCounterX**. I hope it inspires others to dive into web development and share their own creations with the world! 

