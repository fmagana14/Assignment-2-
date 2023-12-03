from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results', methods = ["POST"])
def show_results():
    context = { 
    'users_toppings': request.form.get('toppings'),
    'user_froyo_flavor': request.form.get('flavor')
    
    }
    return render_template('froyo_results.html', **context)

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return render_template('favorites.html')

@app.route('/favorites_results', methods = ['POST'])
def favorites_results():
    fav_color = request.form.get('color')
    fav_animal = request.form.get('animal')
    fav_city = request.form.get('city')

    result_string = f'Wow, I didnt know {fav_color} {fav_animal} lived in {fav_city}!'
    """Shows the user a nice message using their form results."""
    return result_string


@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return render_template('secret.html')


    """
     <form action="/message_results" method="POST">
        Enter your secret message: <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """
@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    if request.method == 'POST':
        message = request.form['message']
        return f"Here's the secret message! {message}"
    else:
        return f"Redo the form til you get a message."
    # sorted_message = request.args.get('sorted_message')

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
      

    # Render the calculator form template for the initial GET request
    return render_template('calculator_form.html')

@app.route('/calculator_results', methods = ['POST'])
def calculator_results():
    """Shows the user the result of their calculation."""
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operator = request.form['operator']

    # Perform the operation based on the operator
    if operator == '+':
        result = num1 + num2
        operation = 'add'
    elif operator == '-':
        result = num1 - num2
        operation = 'subtract'
    elif operator == '*':
        result = num1 * num2
        operation = 'multiply'
    elif operator == '/':
        result = num1 / num2
        operation = 'divide'
    else:
        return "Invalid operator"

    # Render the results template
    return render_template('calculator_results.html', num1=num1, num2=num2, operation=operation, result=result)


HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results', methods = ["POST"])
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
    name = request.form.get('name')
    
    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.form.get('horoscope_sign')  # Lowercase for case-insensitive matching
    
    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    users_personality = HOROSCOPE_PERSONALITIES.get(horoscope_sign)

    # TODO: Generate a random number from 1 to 99
    lucky_number = random.randint(1, 99)

    context = {
        'name': name,
        'horoscope_sign': horoscope_sign,
        'personality': users_personality, 
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)



if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True, port=5001)
