from flask import Flask
from flask import request
from flask import jsonify
from flask import Response


app = Flask(__name__)


@app.route('/calc_payments', methods=['GET', 'POST'])
def calc_payments():
    
    print('Hello....')
    print(request.get_json())
    
    data_dict = request.get_json()
    loan_amt = data_dict.get("loan_amt")
    interest_rate = data_dict.get("interest_rate")
    monthly_payment = data_dict.get("monthly_payment")
    addl_amt = int(data_dict.get("addl_amt"))
    
    
    org_time = loan_amt / monthly_payment
    mod_pay = monthly_payment +  addl_amt
    mod_time = int(loan_amt / mod_pay)
    
    
    print(loan_amt)
    print(interest_rate)
    print(addl_amt)  
    print (monthly_payment)
        
    #resp = Response
    #resp.headers['Access-Control-Allow-Origin'] = '*'
    return jsonify({"loan_amt": loan_amt, "num_of_payments": org_time, "mod_time": mod_time})


app.run(host='0.0.0.0', port=81)

#base = principal *(rate/12)
#mod = add + (principal *(rate/12))
#num_months = total / base
#new_months = total / mod