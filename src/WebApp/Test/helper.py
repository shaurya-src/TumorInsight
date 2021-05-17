from selenium.webdriver.support.ui import WebDriverWait


def test_result(cond, sno, desc):
    status = ""
    if cond:
        status = "PASSED"
    else:
        status = "FAILED"

    print(f"Test {sno}: Testing {desc} --> {status}")


def wait_elem(web_driver, elem):
    WebDriverWait(web_driver, 100).until(lambda driver: elem)
