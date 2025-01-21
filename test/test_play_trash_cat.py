from config import init_alt_tester_driver,launch_app
from pages.trash_cat_page import MyTests



def test_play():
    launch_app()
    alt_tester_driver = init_alt_tester_driver()
    assert alt_tester_driver is not None, "AltTester driver failed to initialize"
    print("AltTester driver initialized.")
    cat = MyTests(alt_tester_driver)
    cat.trash_launch_game()
    cat.avoid_obstacles_and_play()
