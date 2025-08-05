from flask import Flask, render_template, request, redirect, flash
from credit_score import calculate_credit_score, get_risk_category_and_interest

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flash messages

# Simulated credit bureau function
def get_bureau_data(national_id):
    # Replace this with actual API/database lookup when ready
    return {
        "open_credit_lines": 4,
        "current_delinquent_accounts": 0,
        "past_2y_delinquent_accounts": 1
    }

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    try:
        form_data = request.form

        # Extract and validate inputs
        national_id = form_data["national_id"]
        education_level = form_data["education_level"]
        employment_status = form_data["employment_status"]
        home_ownership = form_data["home_ownership"]
        collateral = form_data["collateral"]
        marital_status = form_data["marital_status"]

        monthly_income = float(form_data["monthly_income"])
        mean_income = float(form_data["mean_household_income"])
        age = int(form_data["age"])

        if monthly_income <= 0 or mean_income <= 0:
            flash("Monthly income and mean household income must be greater than 0.")
            return redirect("/")
        if not (18 <= age <= 100):
            flash("Age must be between 18 and 100.")
            return redirect("/")

        # Calculate income ratio
        income_ratio = monthly_income / mean_income

        # Simulate bureau data fetch
        bureau_data = get_bureau_data(national_id)

        input_data = {
            "education_level": education_level,
            "employment_status": employment_status,
            "monthly_income": monthly_income,
            "home_ownership": home_ownership,
            "collateral": collateral,
            "household_income_ratio": income_ratio,
            "marital_status": marital_status,
            "age": age,
            "open_credit_lines": bureau_data["open_credit_lines"],
            "current_delinquent_accounts": bureau_data["current_delinquent_accounts"],
            "past_2y_delinquent_accounts": bureau_data["past_2y_delinquent_accounts"]
        }

        score = calculate_credit_score(input_data)
        risk_category, interest_rate = get_risk_category_and_interest(score)

        return render_template("result.html", score=score, risk_category=risk_category, interest_rate=interest_rate)

    except (ValueError, KeyError) as e:
        flash("Please fill all fields correctly. " + str(e))
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
