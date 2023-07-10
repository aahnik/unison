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

## Note

- In addition to turning Debug=False, you also need to set Prod=True in the env vars


## Trusted by

- ISKCON Barasat [Live Website →]()

**Want to deploy this website for your own organization ?**

Feel free to create an issue in this repo mentioning your needs and email,
and we will get back to you soon.

## Deployment Guide

- [Basic server configuration](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-22-04)
- [How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-22-04)
- [Setup SSL certificate for HTTPS](https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-22-04)
