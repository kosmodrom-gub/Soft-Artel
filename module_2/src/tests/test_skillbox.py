import pytest
// comment
def test_stub():
    """Заглушка для теста."""
    pass

def test_sklibox_title():
    """Проверяет заголовок главной страницы skillbox.ru"""
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options


    options = Options()
    options.add_argument('--headless')  # Без интерфейса браузера
    driver = webdriver.Chrome(options=options)

    try:
        driver.get('https://skillbox.ru')
        title = driver.title
        assert "Skillbox" in title
    finally:
        driver.quit()
