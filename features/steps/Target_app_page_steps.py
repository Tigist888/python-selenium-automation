from behave import given, when, then
from time import sleep


@given('Open Target App page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()
    print('Original window:', context.original_window)


@when('Click Privacy Policy link')
def click_privacy_policy_link(context):
    context.app.target_app_page.click_privacy_policy_link()


@when('Switch to new window')
def switch_to_window(context):
    context.app.base_page.switch_to_new_window()
    # sleep(1)
    # all_windows=context.driver.window_handlles()
    # context.driver.switch_to.window(  all_windows(1))
    # print('current window:', context.driver.current_window_handle)

@then('Verify Privacy Policy page opened')
def verify_privacy_policy_opened(context):
    context.app.target_app_page.verify_privacy_policy_opened()


@then('Close current page')
def close_page(context):
    context.app.base_page.close()
#close() -will close the current page
#quit()-closed every associated window.

@then('Return to original window')
def switch_to_original_window(context):
    context.app.base_page.switch_to_window_by_id(context.original_window)

    # print("switching to original", context.original_window)
    # context.driver.switch_to.window(context.original_window)