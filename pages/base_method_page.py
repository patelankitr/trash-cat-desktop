from alttester import By


def verify_element_is_present_on_screen(alt_driver, locator_type, locator_value, comment, wait):
    # Set the condition to choose By.PATH or By.ID based on the provided locator_type
    if locator_type == 'PATH':
        element = alt_driver.wait_for_object(By.PATH, locator_value, timeout=wait)
    elif locator_type == 'ID':
        element = alt_driver.wait_for_object(By.ID, locator_value, timeout=wait)
    else:
        raise ValueError(f"Unsupported locator_type: {locator_type}. Use 'PATH' or 'ID'.")

    # Check if the element is present
    if element is not None:
        print(f"Print: '{comment}' is present on screen")
    else:
        print(f"Print: '{comment}' is NOT present on screen")

def click_on_the_element(alt_driver, locator_type, locator_value, wait=None,comment=None ):
    # Set the condition to choose By.PATH or By.ID based on the provided locator_type
    if locator_type == 'PATH':
        element = alt_driver.wait_for_object(By.PATH, locator_value, timeout=wait)
    elif locator_type == 'ID':
        element = alt_driver.wait_for_object(By.ID, locator_value, timeout=wait)
    else:
        raise ValueError(f"Unsupported locator_type: {locator_type}. Use 'PATH' or 'ID'.")
    # Tap on the located element
    element.click()
    if comment:
        print(f"Clicked on element: {comment}")
    else:
        print("Clicked on element")

def verify_element_contains(alt_driver, locator_type, locator_value, wait, expected_text):
    # Set the condition to choose By.PATH or By.ID based on the provided locator_type
    if locator_type == 'PATH':
        element_text = alt_driver.wait_for_object(By.PATH, locator_value, timeout=wait).get_text()
    elif locator_type == 'ID':
        element_text = alt_driver.wait_for_object(By.ID, locator_value, timeout=wait).get_text()
    else:
        raise ValueError(f"Unsupported locator_type: {locator_type}. Use 'PATH' or 'ID'.")

    # Assertion to verify the text
    assert element_text == expected_text, f"Expected '{expected_text}', but found '{element_text}'"
    print(f"Parameter: '{expected_text}' is found in the element located by {locator_type}.")


