# django-simplestore [![CircleCI](https://circleci.com/gh/martinstastny/django-simplestore.svg?style=svg)](https://circleci.com/gh/martinstastny/django-simplestore) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/042bb2f744884d00961e6dcbecd915f6)](https://www.codacy.com/app/martinstastny/django-simple-eccomerce?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=martinstastny/django-simple-eccomerce&amp;utm_campaign=Badge_Coverage) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/042bb2f744884d00961e6dcbecd915f6)](https://www.codacy.com/app/martinstastny/django-simple-eccomerce?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=martinstastny/django-simple-eccomerce&amp;utm_campaign=Badge_Grade)

Simple and tested app that can be taken as a starting point for extending and building custom ecommerce site with Python / Django.
 
This project was created for learning / demo purposes.

Demo
========

 - Demo is hosted on free Heroku account.
 - Static files are hosted on Amazon S3 with CloudFlare for CDN.

https://django-simple-store.herokuapp.com
   
 
Features
======== 
- Products
- Category
- Cart 
- User Accounts
- Checkout (Supports Guest Checkout and Logged User Account Checkout)
- Orders
- Mailing (Order Confirmation)
- REST API endpoints for Cart App
- Static files (sass, css, js) bundling and management is done via Webpack.

Dependencies
========
 - Python >= 3.6.1
 - Django >= 1.10.5
 - django-webpack-loader >= 0.4.1
 - easy_thumbnails >= 2.3
 - django-filer >= 1.2.6
 - django-mptt >= 0.8.7
 - django-crispy-forms >= 1.6.1
 - django-storages >= 1.5.2
 - djangorestframework >= 3.6.3
