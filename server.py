from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ='I will work to understand this!'


# our index route will handle rendering our form

@app.route('/')
def index():
    #want to increment count by 1, have to set up a condiitonal
    if 'visit' in session:
        session['visit'] += 1
    else:
        #if it doesn't exist we want the starting value to be 1, because the person is on the page
        session['visit'] = 1
    #want to increment count by 1, have to set up a condiitonal
    if 'count' in session:
        session['count'] += 1
    else:
        #if it doesn't exist we want the starting value to be 0
        session['count'] = 0
    
    return render_template("index.html")

@app.route('/reset')
def reset():
    session.clear()

    return redirect("/")


@app.route("/addtwo")
def add_two():
    session['count'] += 1
    return redirect("/")


@app.route('/form', methods=['POST'])
def add_increment():
    #want the user to be able to add however many counts 
    print(request.form)
    amount = int(request.form['amount'])-1
    session['count'] += amount
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

