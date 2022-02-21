
# Barber rest-api

Django rest-api program which implements all the basic functions which are needed to manage
barbershop. The program is meant to be used by three types of users. Client might register, 
verify account, make an appointment, see and modify profile, see and modify all users visits.
Hairdresser can see and edit visits which are connected to the hairdressers profile. Admin is able
to do all the functions mentioned above and also has access to list of users, list of services and
has rights to modify them.



## Setup

Install Django on your computer
Install Django rest framework with pip
```bash 
pip Install djangorestframework
```

Run migrations to create database migrations, firstly for app because of modified User.

```bash 
py manage.py makemigrations salon 
```
```bash 
py manage.py migrate salon
```
```bash 
py manage.py makemigrations
```
```bash 
py manage.py migrate
```
Create superuser to manage program
```bash
py manage.py createsuperuser
```
Run the server 
```bash
py manage.py runserver
```
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file.
Email, user and password are required to send email with verification email and secret is django
secret key.

`EMAIL`
`USER`
`PASSWORD`
`SECRET`

## Authors

- [@Szymon Cwynar](https://www.github.com/szymcwy)


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/szymon-cwynar-b1b4b5232/)


