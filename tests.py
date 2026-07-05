from api_client import get

def test_root():
	r=get("/")

	print("\nTEST: ROOT")
	print("EXPECTED: 200")
	print("ACTUAL:", r.status_code)

	if r.status_code == 200:
		print("RESULT: PASS")
	else: 
		print("RESULT: FAIL")


def test_user_endpoint():
	r=get("/user")

	print("\nTEST: USER")
	print("EXPECTED: 200, 401\nNEED AUTH")
	print("ACTUAL:", r.status_code)

	if r.status_code in [200, 401]:
		print("USER TEST: PASS (expected auth behavior)")

	else:
		print("USER TEST: FAIL")


def test_rate_limit():
	r=get("/rate_limit")

	print("\nTEST: RATE LIMIT")
	print("EXPECTED: 200")
	print("ACTUAL: ", r.status_code)

	if r.status_code ==200:
		print("RESULT PASS")
	else:
		print("RESULT FAIL")

