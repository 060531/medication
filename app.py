from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/medication_administration')
def medication_administration_route():
    return render_template('Medication_administration.html')

@app.route('/calculate_pma', methods=['GET', 'POST'])
def calculate_pma_route():
    pma_weeks = pma_days = calc = bw = None
    error = None
    if request.method == 'POST':
        try:
            gestational_age_weeks = int(request.form['gestational_age_weeks'])
            gestational_age_days = int(request.form['gestational_age_days'])
            postnatal_age_days = int(request.form['postnatal_age_days'])
            bw = float(request.form['bw'])
            pma_weeks, pma_days, calc = calculate_pma(gestational_age_weeks, gestational_age_days, postnatal_age_days)
        except (ValueError, TypeError):
            error = "Please enter valid numbers."
    return render_template('calculate_pma.html', pma_weeks=pma_weeks, pma_days=pma_days, calc=calc, bw=bw, error=error)

@app.route('/small_dose')
def small_dose_route():
    return render_template('small_dose.html')

@app.route('/fluids')
def fluids_route():
    return render_template('fluids.html')

@app.route('/clindamycin', methods=['GET', 'POST'])
def clindamycin_route():
    dose = None
    error = None
    if request.method == 'POST':
        try:
            dose = int(request.form['dose'])
        except ValueError:
            error = "Please enter a valid dose."
    return render_template('clindamycin.html', dose=dose, error=error)

@app.route('/vancomycin', methods=['GET', 'POST'])
def vancomycin_route():
    dose = None
    error = None
    if request.method == 'POST':
        try:
            dose = int(request.form['dose'])
        except ValueError:
            error = "Please enter a valid dose."
    return render_template('vancomycin.html', dose=dose, error=error)

@app.route('/aminophylline', methods=['GET', 'POST'])
def aminophylline_route():
    dose = None
    error = None
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])  # เปลี่ยนจาก int เป็น float
        except ValueError:
            error = "Please enter a valid dose."
    return render_template('aminophylline.html', dose=dose, error=error)

@app.route('/ampicillin', methods=['GET', 'POST'])
def ampicillin_route():
    dose = None
    error = None
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
        except ValueError:
            error = "Please enter a valid dose."
    return render_template('ampicillin.html', dose=dose, error=error)

@app.route('/amikin', methods=['GET', 'POST'])
def amikin_route():
    dose = None
    error = None
    if request.method == 'POST':
        try:
            dose = int(request.form['dose'])
        except ValueError:
            error = "Please enter a valid dose."
    return render_template('amikin.html', dose=dose, error=error)

@app.route('/gentamicin', methods=['GET', 'POST'])
def gentamicin_route():
    dose = None
    error = None
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
        except ValueError:
            error = "Please enter a valid dose."
    return render_template('gentamicin.html', dose=dose, error=error)
@app.route('/fentanyl', methods=['GET', 'POST'])
def fentanyl_route():
    dose = None
    error = None
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
        except ValueError:
            error = "Please enter a valid dose."
    return render_template('fentanyl.html', dose=dose, error=error)
@app.route('/midazolam', methods=['GET', 'POST'])
def midazolam_route():
    dose = None
    error = None
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
        except ValueError:
            error = "Please enter a valid dose."
    return render_template('midazolam.html', dose=dose, error=error)




def calculate_pma(gestational_age_weeks, gestational_age_days, postnatal_age_days):
    total_days = (gestational_age_weeks * 7) + gestational_age_days + postnatal_age_days
    pma_weeks = total_days // 7
    pma_days = total_days % 7
    calc = pma_weeks + round(pma_days / 7, 0)
    return pma_weeks, pma_days, calc

if __name__ == '__main__':
    app.run(debug=True, port=5002)


