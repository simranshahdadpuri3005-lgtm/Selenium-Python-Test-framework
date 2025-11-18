import pymysql
import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome" , help="specify the browser to use")

@pytest.fixture()
def db_connection():
    conn= pymysql.connect(
        host = "127.0.0.1",
        user = "root",
        password = "MySQl@1234",
        database = "automation_db"
    )
    yield conn
    conn.close()

@pytest.fixture
def browser(request):
    return request.config.getoption("browser")


@pytest.fixture

def setup(browser):
    global driver

    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        raise Exception("browser must be either chrome or firefox")
    return driver

# ----- For pytest html reports  -----
# ---- Hooks for adding env info on html reports ----

def pytest_configure(config):
    config.stash[metadata_key]['Project Name']  = 'SwagLabsProject Pytest Framework for Darts'
    config.stash[metadata_key]['Test Module']  = 'Admin Page'
    config.stash[metadata_key]['Tester']  = 'Simran'


# --- Hook for deleting Default Env variables in HTML report ----
def pytest_metadata(metadata):
    metadata.pop('Packages', None)
    metadata.pop('Plugins', None)

