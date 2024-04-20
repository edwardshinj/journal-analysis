# Journalysis - Journal Analysis

Combines daily journaling with logging and analysis of key/custom metrics. Finds what works for YOU!

Journalysis is a full-stack web app that combines daily journaling with logging of metrics such as happiness and sleep, with individualized analysis of correlations and trends. Provides users with the ability to track and improve their mental and physical wellness over the course of their life, unlocking the benefits of psychological research on the individual level. 


Journalysis is currently in development, and uilizes:
- React Framework with Vite and Tailwind for the frontend. 
- Django w/ PostgreSQL as the backend REST API. 

Implemented features (Frontend): 
- Enter/submit journal entries using default questions
- View list of all submitted entries

Implemented features (Backend):
- Journal Entry and User models, optimized for scalability and customizability
- GET and POST REST API endpoints submitting/viewing journal entries, using Django REST Framework

Features in progress: 
- User login/authentication functionality, for user privacy
- Allowing metrics to be user-customizable, and track virtually anything. 

Planned development:
- Dockerization w/ K8
- Cloud deployment
- Data analysis
- Customizable metrics


