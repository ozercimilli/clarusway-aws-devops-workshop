
from flask import Flask, render_template, request

app = Flask(__name__)

def convert(numbers):
    if numbers < 1000:
        print(f"just {number} miliseconds/s")
        
    numbers = int(numbers//1000)
    if numbers < 60:
        seconds=int(numbers%60)
        print(f"{seconds} second/s")
        
    elif numbers < 3600:
        seconds=int(numbers%60)
        minutes=int((numbers/60)%60)
        print(f"{minutes} minutes/s {seconds} second/s")
        
    else:
        seconds=int(numbers%60)
        minutes=int((numbers/60)%60)
        hours=int((numbers/(60*60))%60)
        print(f"{hours} hours/s {minutes} minutes/s {seconds} second/s")
        

@app.route('/', methods=['GET'])
def main_get():
    return render_template('index.html', developer_name='E2213', not_valid=False)

@app.route('/', methods=['POST'])
def main_post():
    alpha = request.form['number']
    if not alpha.isdecimal():
        return render_template('index.html', developer_name='E2213', not_valid=True)

    number = int(alpha)
    if number < 1:
        return render_template('index.html', developer_name='E2213', not_valid=True)

    return render_template('result.html', milliseconds= number, result= convert(number) , developer_name='E2213')


if __name__=='__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=80)