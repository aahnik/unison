# temple-web

A modern and dynamic website for temple communities.

[![Code style: djLint](https://img.shields.io/badge/html%20style-djLint-blue.svg)](https://github.com/Riverside-Healthcare/djlint)

## Features

- Robust admin panel to customize every aspect of the web page
- Accept donations or sell items. Integration with upigateway.com
- Modular and easily extensible code base

## Tech Stack

- Django
- Tailwind CSS
- Flowbite components and Blocks


## Installation

- To install on a ubuntu VPS you can probably run `scripts/install.sh`.

  ```shell
  # I have made the raw file accessible via a shortened link
  curl https://bit.ly/twiubd -Lks | bash
  ```

## Environment Variables

| Environment Variable      | Purpose                                                          | Example Value                |
|-------------------------|------------------------------------------------------------------|----------------------------|
| DEBUG                   | Enable Django debug mode                                          | True                       |
| PROD                    | Enable production mode                                            | False                      |
| SECRET_KEY              | Django secret key for security                                    | your-secret-key-here       |
| MORE_ALLOWED_HOSTS      | Additional allowed hosts (comma-separated IPs/domains)            | 139.59.38.218,139.59.38.219|
| PROD_FILES_ROOT         | Root directory for production files                               | /var/www/                  |
| PROD_DOMAIN            | Production domain name                                            | iskconbarasat.com          |
| DEPLOYMENT_VERSION      | Version identifier for deployment                                 | TestingLocal-Tue-June-20-2023|
| DEFAULT_FROM_EMAIL     | Default sender email address                                      | templeweb@email.com        |
| EMAIL_HOST_USER        | SMTP server username                                              | templeweb@email.com        |
| EMAIL_HOST_PASSWORD    | SMTP server password                                              | your-email-password        |
| PAYMENT_GATEWAY_API_KEY| API key for payment gateway                                       | your-gateway-api-key       |
| DB_NAME                | PostgreSQL database name                                          | unison_db                  |
| DB_USER                | PostgreSQL database user                                          | unison_user                |
| DB_PASSWORD            | PostgreSQL database password                                      | your-strong-password       |
| DB_HOST                | PostgreSQL database host                                          | db                         |
| DB_PORT                | PostgreSQL database port                                          | 5432                       |
| CELERY_BROKER_URL      | URL for Celery message broker (if using Celery)                  | redis://localhost:6379     |
| CELERY_RESULT_BACKEND  | URL for Celery result backend (if using Celery)                  | redis://localhost:6379     |

### Important Notes:

1. For production deployment:
   - Set `DEBUG=False`
   - Set `PROD=True`
   - Ensure `SECRET_KEY` is a strong, unique value
   - Configure `MORE_ALLOWED_HOSTS` with your server IPs/domains

2. Email Configuration:
   - `DEFAULT_FROM_EMAIL` and `EMAIL_HOST_USER` are typically the same
   - Ensure `EMAIL_HOST_PASSWORD` is secure and properly configured

3. Database Configuration:
   - When using Docker, `DB_HOST` should be set to `db`
   - Ensure `DB_PASSWORD` is strong and secure

4. Payment Gateway:
   - `PAYMENT_GATEWAY_API_KEY` is required for processing payments
   - Keep this key secure and never commit it to version control

## Note

- In addition to turning Debug=False, you also need to set Prod=True in the env vars


## Trusted by

- ISKCON Barasat [Live Website →]()

**Want to deploy this website for your own organization ?**

Feel free to create an issue in this repo mentioning your needs and email,
and we will get back to you soon.

## Django Guide

Other than extensively refering to the Django documentation, I found these articles really helpful.

- [One Database Model, Many Behaviors: A Practical Introduction to Django Proxy Models](https://wellfire.co/learn/using-django-proxy-models/)

## Deployment Guide

- [Basic server configuration](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04)
- [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04)
- [Setup SSL certificate for HTTPS](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04)
