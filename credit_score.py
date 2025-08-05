def calculate_credit_score(data):
    score = 50  # Starting base score

    # 1. Education Level
    education_points = {
        "Postgraduate Degree": 10,
        "Bachelor's Degree": 7,
        "Diploma/Certificate": 4,
        "High School": 1,
        "No Formal Education": -5
    }
    score += education_points.get(data.get("education_level"), 0)

    # 2. Employment Status
    employment_points = {
        "Full-time": 10,
        "Part-time/Contract": 5,
        "Self-employed": 3,
        "Unemployed": -10,
        "Unverified": -5
    }
    score += employment_points.get(data.get("employment_status"), 0)

    # 3. Verified Monthly Income
    income = data.get("monthly_income", 0)
    if income > 5000:
        score += 10
    elif 3000 <= income <= 5000:
        score += 6
    elif 1500 <= income < 3000:
        score += 2
    else:
        score -= 5

    # 4. Home Ownership
    home_points = {
        "Owns home": 8,
        "Mortgaged": 5,
        "Renting": 2,
        "Lives with family": 0,
        "Homeless/Unknown": -5
    }
    score += home_points.get(data.get("home_ownership"), 0)

    # 5. Collateral Value (simple levels)
    collateral_value = data.get("collateral", "").lower()
    if collateral_value == "high":
        score += 10
    elif collateral_value == "medium":
        score += 5
    elif collateral_value == "low":
        score += 2
    elif collateral_value == "none":
        score -= 10

    # 6. Mean Household Income (relative to region)
    household_income_ratio = data.get("household_income_ratio", 1.0)  # 1.0 = 100% of average
    if household_income_ratio > 1.5:
        score += 5
    elif 1.0 <= household_income_ratio <= 1.5:
        score += 3
    elif 0.75 <= household_income_ratio < 1.0:
        score += 0
    else:
        score -= 3

    # 7. Marital Status
    marital_points = {
        "Married (with dependents)": 3,
        "Married (no dependents)": 2,
        "Single": 0,
        "Divorced/Widowed": -2
    }
    score += marital_points.get(data.get("marital_status"), 0)

    # 8. Age
    age = data.get("age", 0)
    if 35 <= age <= 60:
        score += 5
    elif 25 <= age < 35:
        score += 3
    elif age < 18:
        score -= 10
    else:
        score += 0

    # 9. Number of Open Credit Lines
    open_lines = data.get("open_credit_lines", 0)
    if 0 <= open_lines <= 3:
        score += 5
    elif 4 <= open_lines <= 6:
        score += 2
    elif 7 <= open_lines <= 10:
        score -= 3
    else:
        score -= 6

    # 10. Current Delinquencies
    current_delinquencies = data.get("current_delinquent_accounts", 0)
    if current_delinquencies == 0:
        score += 10
    elif 1 <= current_delinquencies <= 2:
        score -= 10
    else:
        score -= 20

    # 11. Delinquencies in Past 2 Years
    past_delinquencies = data.get("past_2y_delinquent_accounts", 0)
    if past_delinquencies == 0:
        score += 5
    elif 1 <= past_delinquencies <= 2:
        score -= 5
    elif 3 <= past_delinquencies <= 5:
        score -= 10
    else:
        score -= 15

    return score

def get_risk_category_and_interest(score):
    if score >= 90:
        return "Extremely Low Risk", 7.5
    elif 75 <= score < 90:
        return "Low Risk", 10.0
    elif 60 <= score < 75:
        return "Neutral", 12.5
    elif 40 <= score < 60:
        return "High Risk", 15.0
    else:
        return "Extremely High Risk", 17.5


if __name__ == "__main__":
    sample_input = {
        "education_level": "Bachelor's Degree",
        "employment_status": "Full-time",
        "monthly_income": 4200,
        "home_ownership": "Renting",
        "collateral": "medium",
        "household_income_ratio": 1.1,
        "marital_status": "Married (no dependents)",
        "age": 33,
        "open_credit_lines": 4,
        "current_delinquent_accounts": 1,
        "past_2y_delinquent_accounts": 3
    }

    final_score = calculate_credit_score(sample_input)
    risk_category, interest_rate = get_risk_category_and_interest(final_score)

    print(f"Calculated Credit Score: {final_score}")
    print(f"Risk Category: {risk_category}")
    print(f"Assigned Interest Rate: {interest_rate}%")
