# Fairbanks Hackathon 2016: Alaska Market
A proof-of-concept for an online marketplace of Alaskan products.

## Requirements
This repo includes a Vagrant box of Ubuntu 14.04 with PostgreSQL installed for development, but the workstation needs the following:
- [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/downloads.html)
- [Python 2.7](https://www.python.org/downloads/)
- [Psycopg2](http://initd.org/psycopg/download/)
- [SQLAlchemy](http://www.sqlalchemy.org/download.html)

## Setup and Testing
Once you clone down this repo, CLI into the directory containing the Vagrantfile and `vagrant up`. It'll take a few minutes while it downloads the Ubuntu box and provisions it, but afterwards it will be much quicker. Once the Vagrant box is provisioned (there'll be a message about how to access the database), move into the database directory and `python database_setup.py` to create the database and tables.

You can verify the database and tables by doing the following from within the repo:
```
vagrant ssh
sudo su - postgres
psql market
\dt
\d (table)
```
This connects you to the Vagrant box, logs you in as the postgres user, connects to the "market" database, lists the tables, then lists a specific table in more detail.

`\q` to quit PostgreSQL and `logout` a couple of times to exit Vagrant.
`vagrant halt` to shutdown the VM.
`vagrant destroy` to completely destroy the VM so that you can start over.

## To-Do
- **Front-End**: We need one! And that probably means installing a web server or adding another Vagrant box.
- **Database Structure**: This will need to be refined and fleshed out.
- **Ranking Algorithm**: For "hot" items. Score increments by price per sale then decays over time?
- **User Registration**: What information do we want to collect? Don't forget to hash the passwords. Has the ability to leave reviews.
- **Business Registration**: Same. And they need to have the ability to create, modify, and delete products.
- **Money**: We'll need a third-party to handle the financial transactions.
- **Other**: Brainstorming session! What other stuff will this site need?