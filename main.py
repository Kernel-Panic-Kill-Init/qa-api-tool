import tests

print("QA API TOOL START\n")

tests.test_root()
tests.test_user_endpoint()
tests.test_rate_limit()

print("\nDONE")
