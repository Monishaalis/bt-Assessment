from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# Step 1: Launch the application URL
url = "https://www.bt.com/"
driver = webdriver.Chrome()
driver.get(url)

# Step 2: Close accept Cookie pop-up if it appears
try:
    cookie_popup = driver.find_element_by_id("onetrust-accept-btn-handler")
    cookie_popup.click()
except:
    pass

# Step 3: Hover to Mobile menu
mobile_menu = driver.find_element_by_link_text("Mobile")
actions = ActionChains(driver)
actions.move_to_element(mobile_menu).perform()

# Step 4: From mobile menu, select Mobile phones
mobile_phones_option = driver.find_element_by_link_text("Mobile phones")
mobile_phones_option.click()

# Step 5: Verify the number of banners
banners = driver.find_elements_by_css_selector(".banner")
assert len(banners) >= 3, "Less than 3 banners found."

# Step 6: Scroll down and click View SIM only deals
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
view_sim_deals_button = driver.find_element_by_partial_link_text("View SIM only deals")
view_sim_deals_button.click()

# Step 7: Validate the title for the new page
expected_title = "SIM Only Deals | 4G & 5G SIM Cards | BT Mobile"
assert expected_title in driver.title, f"Title mismatch. Expected: {expected_title}, Actual: {driver.title}"

# Step 8: Validate "30% off and double data" information
plan_info = driver.find_element_by_xpath("//*[contains(text(),'30% off and double data')]").text
expected_info = "30% off and double data was 125GB 250GB Essential Plan, was £27 £18.90 per month"
assert expected_info in plan_info, f"Plan information mismatch. Expected: {expected_info}, Actual: {plan_info}"

# Step 9: Close the browser and exit
driver.quit()
