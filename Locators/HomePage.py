from selenium.webdriver.common.by import By

# locators
HomePage = {
    'logoHome' : (By.XPATH, '//div[@class="orangehrm-login-branding"]/img'),
    'txtUsername' : (By.XPATH, '//input[@name="username"]'),
    'txtPassword' : (By.XPATH, '//input[@name="password"]'),
    'btnLogin' : (By.XPATH, '//button[@type="submit"]'),
    'logoInsideHome' : (By.XPATH, '//div[@class="oxd-brand-banner"]//img'),
    'invalidCredsMsg' : (By.XPATH, '//p[text()="Invalid credentials"]'),
    'pageRecruitment' : '//li//a//span[text()="{}"]',
    'titleRecruitment' : (By.XPATH, '//div[contains(@class,"header-title")]//*[text()="Recruitment"]'),
}

RcruitmentPage = {
    'dropdownVacancy' : '//label[text()="{}"]/../following-sibling::div',
    'filterBy' : '//div[@class="oxd-select-option"]/span[text()="{}"]',
    'btnSearch' : (By.XPATH, '//button[text()=" Search "]'),
    'tableCellVacancy' : (By.XPATH, '//div[contains(@class,"table-cell")][2]/div'),
}