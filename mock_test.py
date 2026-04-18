import pytest

def test_frontend_timeout():
    # Simulate a network timeout error when loading a page
    raise TimeoutError("Page load timed out after 30000ms. Could not locate element '#submit-button'.")

def test_backend_assertion():
    # Simulate a failing API assertion
    response_code = 500
    assert response_code == 200, "Expected status code 200 but got 500 for endpoint /api/v1/users"

def test_missing_element():
    # Simulate an element not found
    element_found = False
    assert element_found, "NoSuchElementException: Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\".user-avatar\"}"
