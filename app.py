from flask import request, Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/calculate',methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operator = request.form['operator']

    result = None

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Cannot divide by zero."
    print('The result is:-',result)
    return render_template('home.html', results=result)

if __name__ == '__main__':
    app.run(debug=True)