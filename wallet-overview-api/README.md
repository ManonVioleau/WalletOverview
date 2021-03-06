# WalletOverview

Developing a solution to have an overview on your Binance Wallet.  
Back using :

<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://codecov.io/gh/tiangolo/fastapi" target="_blank">
    <img src="https://img.shields.io/codecov/c/github/tiangolo/fastapi?color=%2334D058" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: <a href="https://fastapi.tiangolo.com" target="_blank">https://fastapi.tiangolo.com</a>

**Source Code**: <a href="https://github.com/tiangolo/fastapi" target="_blank">https://github.com/tiangolo/fastapi</a>

---

# Get Started

## Prerequisites
You will need Python version 3.6+ or greater and python3.8-venv installed on your system.

## Setup

Get the code by either cloning this repository using git

    > git clone https://github.com/ManonVioleau/WalletOverview.git  
Once downloaded, open the terminal in the project directory, and continue with:

```
pip install -r requirements.txt
```
### MySQL SetUp

Create a file in the "config" folder named "id_connect.py" and fill it like :
login = 'your_mysql_login'
password = 'your_mysql_password*'
db_name = 'your_db_name'.

Change the host name and other param in the db.py file if needed.

### Compiles and hot-reloads for development
```
uvicorn main:app --reload
```