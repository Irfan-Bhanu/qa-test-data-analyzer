# This script analyzes test execution results and identifies risk level based on failure percentage
import pandas as pd

def test_summary(test_results):

    total = len(test_results)

    failed_module = []
    pass_count = 0
    fail_count = 0

    for key, value in test_results.items():
        if value == "fail":
            fail_count += 1
            failed_module.append(key)
        else:
            pass_count += 1

    pass_per = (pass_count / total) * 100
    fail_per = (fail_count / total) * 100

    if fail_per > 50:
        status = "Critical"
    elif 30 <= fail_per <= 50:
        status = "Warning"
    else:
        status = "Stable"

    return {
        "pass": pass_count,
        "fail": fail_count,
        "pass_per": pass_per,
        "fail_per": fail_per,
        "failed_modules": failed_module,
        "status": status
    }


# MAIN EXECUTION

data = pd.read_csv("../data/test_results.csv")

# Clean data
data['module'] = data['module'].str.strip()
data['result'] = data['result'].str.strip().str.lower()

# Convert to dictionary
data_dict = dict(zip(data['module'], data['result']))

# Run analysis
result = test_summary(data_dict)

print("------ Test Summary Report ------")
print(result)
