# /!/usr/bin/python3
# coding:utf-8
__author__ = "Yanwen Xu"
"""
description:Dealertarck's third page locator
"""
from selenium.webdriver.common.by import By


class ThirdPageLocator:
    third_page_text_loc = (By.ID, "header")
    first_number_loc = (By.ID, "multiplier")
    second_number_loc = (By.ID, "multiplicand")
    result_of_multiply_loc = (By.ID, "product")
    multiply_button_loc = (By.ID, "multiplicationButton")
    first_page_link_loc = (By.LINK_TEXT, "Go back to starting page.")
    pop_up_window_button_loc = (By.ID, "popupButton")

    submit_button_loc = (By.ID, "btnSubmit")
    exit_button_loc = (
        By.XPATH,
        "/html/body/input[2]",
    )  # CSS_SELECTOR, 'body > input:nth-child(5)'
    do_sth_button_loc = (By.ID, "btnCF04")

    home_link_loc = (By.LINK_TEXT, "Home")
    news_link_loc = (By.LINK_TEXT, "News")
    contact_link_loc = (By.LINK_TEXT, "Contact")
    help_link_loc = (By.LINK_TEXT, "Help")

    track_loc = (
        By.XPATH,
        '//*[@id="Table"]/div[4]/div/input',
    )

    track_locs = (
        By.CLASS_NAME,
        "dtdms-input",
    )
