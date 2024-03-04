has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for Loan")

if has_good_credit or has_high_income:
    print("Eligible for Loan with study")

if has_good_credit and not has_criminal_record:
    print("Good for loan")