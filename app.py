from flask import Flask, render_template, request
import math  # นำเข้า math เพื่อใช้สำหรับการปัดเศษ
app = Flask(__name__)

# กำหนดค่าวันที่สำหรับการอัพเดต
UPDATE_DATE = "17 ต.ค. 2567"

# ใช้ context_processor เพื่อส่งตัวแปร update_date ไปทุก template
@app.context_processor
def inject_update_date():
    return dict(update_date=UPDATE_DATE)


@app.route('/')
def index():
    return render_template('index.html', update_date=UPDATE_DATE)




@app.route('/medication_administration')
def medication_administration_route():
    return render_template('Medication_administration.html', update_date=UPDATE_DATE)


@app.route('/time_management')
def time_management_route():
    return render_template('time_management.html', update_date=UPDATE_DATE)

@app.route('/run_time')
def run_time():
    return render_template('run_time.html')  # ให้แน่ใจว่ามีไฟล์ run_time.html ในโฟลเดอร์ templates

@app.route('/run_time_stop')
def run_time_stop():
    return render_template('run_time_stop.html')  # ให้แน่ใจว่ามีไฟล์ run_time_stop.html ในโฟลเดอร์ templates
   
@app.route('/small_dose')
def small_dose_route():
    return render_template('small_dose.html', update_date=UPDATE_DATE)

@app.route('/fluids')
def fluids_route():
    return render_template('fluids.html', update_date=UPDATE_DATE)


@app.route('/cloxacillin', methods=['GET', 'POST'])
def cloxacillin_route():
    dose = None
    result_ml = None
    final_result = None
    multiplication = None
    error = None
    formula_display = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])

            # เปลี่ยนการคำนวณเบื้องต้นให้เหมาะสมกับ cloxacillin
            result_ml = round((dose * 5) / 1000, 2)

            final_result = round(result_ml * multiplication, 2)

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('cloxacillin.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, formula_display=formula_display, error=error, update_date=UPDATE_DATE)


@app.route('/amikin', methods=['GET', 'POST'])
def amikin_route():
    dose = None
    result_ml = None
    final_result = None
    multiplication = None
    error = None
    formula_display = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])

            result_ml = round((dose * 2) / 500, 2)
            final_result = round(result_ml * multiplication, 2)

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('amikin.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, formula_display=formula_display, error=error, update_date=UPDATE_DATE)


@app.route('/aminophylline', methods=['GET', 'POST'])
def aminophylline_route():
    dose = None
    result_ml = None
    error = None
    
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml = dose * 10  # ตัวอย่างการคำนวณ
        except ValueError:
            error = "กรุณากรอกขนาดยาที่ถูกต้อง"
    
    return render_template('aminophylline.html', dose=dose, result_ml=result_ml, error=error, update_date=UPDATE_DATE)


@app.route('/morphine', methods=['GET', 'POST'])
def morphine_route():
    dose = None
    result_ml = None
    error = None
    
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml = dose * 10  # ตัวอย่างการคำนวณ
        except ValueError:
            error = "กรุณากรอกขนาดยาที่ถูกต้อง"
    
    return render_template('morphine.html', dose=dose, result_ml=result_ml, error=error, update_date=UPDATE_DATE)


@app.route('/phenytoin', methods=['GET', 'POST'])
def phenytoin_route():
    dose = None
    result_ml = None
    error = None
    
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml = dose * 4  # ตัวอย่างการคำนวณ
        except ValueError:
            error = "กรุณากรอกขนาดยาที่ถูกต้อง"
    
    return render_template('phenytoin.html', dose=dose, result_ml=result_ml, error=error, update_date=UPDATE_DATE)


@app.route('/hydrocortisone', methods=['GET', 'POST'])
def hydrocortisone_route():
    dose = None
    result_ml = None
    error = None
    
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml = dose * 4  # ตัวอย่างการคำนวณ
        except ValueError:
            error = "กรุณากรอกขนาดยาที่ถูกต้อง"
    
    return render_template('hydrocortisone.html', dose=dose, result_ml=result_ml, error=error, update_date=UPDATE_DATE)


@app.route('/ampicillin', methods=['GET', 'POST'])
def ampicillin_route():
    dose = None
    result_ml = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml = round((dose * 5) / 1000, 2)  # Example: Calculation for Ampicillin
        except ValueError:
            error = "กรุณากรอกขนาดยาที่ถูกต้อง"
    
    return render_template('ampicillin.html', dose=dose, result_ml=result_ml, error=error, update_date=UPDATE_DATE)


@app.route('/clindamycin', methods=['GET', 'POST'])
def clindamycin_route():
    dose = None
    result_ml_1 = None
    result_ml_2 = None
    final_result_1 = None
    final_result_2 = None
    multiplication = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml_1 = round((dose * 4) / 600, 2)
            result_ml_2 = round((dose * 1) / 6, 2)

            if 'multiplication' in request.form:  # ตรวจสอบการคำนวณคูณ
                multiplication = float(request.form['multiplication'])
                final_result_1 = round(result_ml_1 * multiplication, 2)
                final_result_2 = round(result_ml_2 * multiplication, 2)

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('clindamycin.html', dose=dose, result_ml_1=result_ml_1, result_ml_2=result_ml_2, final_result_1=final_result_1, final_result_2=final_result_2, multiplication=multiplication, error=error, update_date=UPDATE_DATE)


@app.route('/dobutamine', methods=['GET', 'POST'])
def dobutamine_route():
    dose = None
    result_ml = None
    error = None
    DobutamineVolume = None

    if request.method == 'POST':
        try:
            original_dosage = float(request.form['original_dosage'])
            original_volume = float(request.form['original_volume'])
            desired_dosage = float(request.form['desired_dosage'])

            result_ml = (desired_dosage / original_dosage) * original_volume
            DobutamineVolume = desired_dosage / 50

        except ValueError:
            error = "กรุณากรอกข้อมูลที่ถูกต้อง"

    return render_template('dobutamine.html', dose=dose, result_ml=result_ml, DobutamineVolume=DobutamineVolume, error=error, update_date=UPDATE_DATE)


@app.route('/dopamine', methods=['GET', 'POST'])
def dopamine_route():
    dose = None
    result_ml = None
    error = None
    DopamineVolume = None

    if request.method == 'POST':
        try:
            original_dosage = float(request.form['original_dosage'])
            original_volume = float(request.form['original_volume'])
            desired_dosage = float(request.form['desired_dosage'])

            result_ml = (desired_dosage / original_dosage) * original_volume
            DopamineVolume = desired_dosage / 25

        except ValueError:
            error = "กรุณากรอกข้อมูลที่ถูกต้อง"

    return render_template('dopamine.html', dose=dose, result_ml=result_ml, DopamineVolume=DopamineVolume, error=error, update_date=UPDATE_DATE)


@app.route('/remdsivir', methods=['GET', 'POST'])
def remdsivir_route():
    dose = None
    result_ml_1 = None
    result_ml_2 = None
    final_result_1 = None
    final_result_2 = None
    multiplication = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml_1 = round((dose * 20) / 100, 2)
            result_ml_2 = round((dose * 1) / 1.25, 2)

            if 'multiplication' in request.form:
                multiplication = float(request.form['multiplication'])
                final_result_1 = round(result_ml_1 * multiplication, 2)
                final_result_2 = round(result_ml_2 * multiplication, 2)

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('remdsivir.html', dose=dose, result_ml_1=result_ml_1, result_ml_2=result_ml_2, final_result_1=final_result_1, final_result_2=final_result_2, multiplication=multiplication, error=error, update_date=UPDATE_DATE)


@app.route('/amphotericinB', methods=['GET', 'POST'])
def amphotericinB_route():
    dose = None
    result_ml_1 = None
    result_ml_2 = None
    final_result_1 = None
    final_result_2 = None
    multiplication = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml_1 = round((dose * 10) / 50, 2)
            result_ml_2 = round((dose * 1) / 0.1, 2)

            if 'multiplication' in request.form:
                multiplication = float(request.form['multiplication'])
                final_result_1 = round(result_ml_1 * multiplication, 2)
                final_result_2 = round(result_ml_2 * multiplication, 2)

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('amphotericinB.html', dose=dose, result_ml_1=result_ml_1, result_ml_2=result_ml_2, final_result_1=final_result_1, final_result_2=final_result_2, multiplication=multiplication, error=error, update_date=UPDATE_DATE)


@app.route('/amoxicillin_clavimoxy')
def amoxicillin_clavimoxy_route():
    return render_template('amoxicillin_clavimoxy.html', update_date=UPDATE_DATE)


@app.route('/dexamethasone', methods=['GET', 'POST'])
def dexamethasone_route():
    dose = None
    result_ml = None
    error = None
    
    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml = dose * 100  # ตัวอย่างการคำนวณ
        except ValueError:
            error = "กรุณากรอกขนาดยาที่ถูกต้อง"
    
    return render_template('dexamethasone.html', dose=dose, result_ml=result_ml, error=error, update_date=UPDATE_DATE)


@app.route('/midazolam_fentanyl', methods=['GET', 'POST'])
def midazolam_fentanyl_route():
    midazolam_dosage = None
    fentanyl_dosage = None
    original_volume = None
    midazolam_volume = None
    fentanyl_volume = None
    final_volume = None
    error = None

    if request.method == 'POST':
        try:
            midazolam_dosage = float(request.form['midazolam_dosage'])
            fentanyl_dosage = float(request.form['fentanyl_dosage'])
            original_volume = float(request.form['original_volume'])

            midazolam_volume = midazolam_dosage / 5
            fentanyl_volume = fentanyl_dosage / 50

            final_volume = original_volume - (midazolam_volume + fentanyl_volume)

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('midazolam_fentanyl.html',
                           midazolam_dosage=midazolam_dosage,
                           fentanyl_dosage=fentanyl_dosage,
                           original_volume=original_volume,
                           midazolam_volume=midazolam_volume,
                           fentanyl_volume=fentanyl_volume,
                           final_volume=final_volume,
                           error=error,
                           update_date=UPDATE_DATE)


@app.route('/acyclovir', methods=['GET', 'POST'])
def acyclovir_route():
    dose = None
    result_ml_1 = None
    result_ml_2 = None
    final_result_1 = None
    final_result_2 = None
    multiplication = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml_1 = round((dose * 5) / 250, 2)
            result_ml_2 = round((dose * 1) / 5, 2)

            if 'multiplication' in request.form:
                multiplication = float(request.form['multiplication'])
                final_result_1 = round(result_ml_1 * multiplication, 2)
                final_result_2 = round(result_ml_2 * multiplication, 2)

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('acyclovir.html', 
                           update_date=UPDATE_DATE, 
                           dose=dose, 
                           result_ml_1=result_ml_1, 
                           result_ml_2=result_ml_2, 
                           final_result_1=final_result_1, 
                           final_result_2=final_result_2, 
                           multiplication=multiplication, 
                           error=error)


@app.route('/fentanyl', methods=['GET'])
def fentanyl_route():
    return render_template('fentanyl.html', update_date=UPDATE_DATE)


@app.route('/fentanyl_continuous', methods=['GET', 'POST'])
def fentanyl_continuous_route():
    dose = None
    result = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result = dose * 0.1  # ตัวอย่างการคำนวณ continuous infusion

        except (ValueError, KeyError) as e:
            error = f"กรุณากรอกข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('fentanyl_continuous.html', dose=dose, result=result, error=error, update_date=UPDATE_DATE)


@app.route('/fentanyl_small_dose', methods=['GET', 'POST'])
def fentanyl_small_dose_route():
    dose = None
    result = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result = dose * 0.05  # ตัวอย่างการคำนวณสำหรับ small dose

        except (ValueError, KeyError) as e:
            error = f"กรุณากรอกข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('fentanyl_small_dose.html', dose=dose, result=result, error=error, update_date=UPDATE_DATE)


@app.route('/midazolam', methods=['GET'])
def midazolam_route():
    return render_template('midazolam.html', update_date=UPDATE_DATE)


@app.route('/midazolam_continuous', methods=['GET', 'POST'])
def midazolam_continuous_route():
    dose = None
    result = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])  # รับค่าขนาดยา (mg)
            result = dose * 0.1  # ตัวอย่างการคำนวณ infusion rate

        except (ValueError, KeyError) as e:
            error = f"กรุณากรอกข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('midazolam_continuous.html', dose=dose, result=result, error=error, update_date=UPDATE_DATE)


@app.route('/midazolam_small_dose', methods=['GET', 'POST'])
def midazolam_small_dose_route():
    dose = None
    result = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result = dose * 0.1  # ตัวอย่างการคำนวณสำหรับ small dose

        except (ValueError, KeyError) as e:
            error = f"กรุณากรอกข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('midazolam_small_dose.html', dose=dose, result=result, error=error, update_date=UPDATE_DATE)


@app.route('/gentamicin', methods=['GET', 'POST'])
def gentamicin_route():
    dose = None
    result_ml = None
    final_result = None
    multiplication = None
    error = None
    formula_display = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])
            result_ml = round((dose * 2) / 80, 2)

            final_result = round(result_ml * multiplication, 2)

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>"
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('gentamicin.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, formula_display=formula_display, error=error, update_date=UPDATE_DATE)


@app.route('/vancomycin', methods=['GET', 'POST'])
def vancomycin_route():
    dose = None
    result_ml_1 = None
    result_ml_2 = None
    final_result_1 = None
    final_result_2 = None
    multiplication = None
    concentration = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            concentration = int(request.form['concentration'])

            result_ml_1 = round((dose * 10) / 500, 2)

            if concentration == 5:
                result_ml_2 = round((dose * 1) / 5, 2)
            elif concentration == 7:
                result_ml_2 = round((dose * 1) / 7, 2)

            if 'multiplication' in request.form and request.form['multiplication']:
                multiplication = float(request.form['multiplication'])
                final_result_1 = round(result_ml_1 * multiplication, 2)
                final_result_2 = round(result_ml_2 * multiplication, 2)

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template(
        'vancomycin.html', 
        dose=dose, 
        concentration=concentration, 
        result_ml_1=result_ml_1, 
        result_ml_2=result_ml_2, 
        final_result_1=final_result_1, 
        final_result_2=final_result_2, 
        multiplication=multiplication, 
        error=error,
        update_date=UPDATE_DATE
    )


@app.route('/colistin', methods=['GET', 'POST'])
def colistin_route():
    dose = None
    result_ml = None
    final_result = None
    error = None
    multiplication = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])
            result_ml = round((dose * 2) / 150, 2)
            
            final_result = result_ml * multiplication

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }
        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('colistin.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, error=error, update_date=UPDATE_DATE)


@app.route('/cefotaxime', methods=['GET', 'POST'])
def cefotaxime_route():
    dose = None
    result_ml = None
    final_result = None
    multiplication = None
    error = None
    formula_display = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])
            result_ml = round((dose * 10) / 1000, 2)

            final_result = round(result_ml * multiplication, 2)

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('cefotaxime.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, formula_display=formula_display, error=error, update_date=UPDATE_DATE)


@app.route('/ceftazidime', methods=['GET', 'POST'])
def ceftazidime_route():
    dose = None
    result_ml = None
    final_result = None
    multiplication = None
    error = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])
            result_ml = round((dose * 10) / 1000, 2)

            final_result = round(result_ml * multiplication, 2)

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('ceftazidime.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, error=error, update_date=UPDATE_DATE)


@app.route('/sulbactam', methods=['GET', 'POST'])
def sulbactam_route():
    dose = None
    result_ml = None
    final_result = None
    multiplication = None
    error = None
    formula_display = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])
            result_ml = round((dose * 9.2) / 2000, 2)

            final_result = round(result_ml * multiplication, 2)

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('sulbactam.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, formula_display=formula_display, error=error, update_date=UPDATE_DATE)


@app.route('/sulperazone', methods=['GET', 'POST'])
def sulperazone_route():
    dose = None
    result_ml = None
    final_result = None
    error = None
    content_extra = None
    multiplication = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])
            result_ml = round((dose / 500) * 20, 2)
            final_result = result_ml * multiplication  # Calculate final_result

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }
        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('sulperazone.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, error=error, update_date=UPDATE_DATE)


@app.route('/insulin', methods=['GET', 'POST'])
def insulin_route():
    dose = None
    result = None
    concentration = 1

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result = round(dose * 100 / concentration, 2)
        except ValueError:
            result = "ข้อมูลไม่ถูกต้อง"

    return render_template('insulin.html', dose=dose, result=result, update_date=UPDATE_DATE)


@app.route('/tazocin', methods=['GET', 'POST'])
def tazocin_route():
    dose = None
    result_ml = None
    final_result = None
    multiplication = None
    error = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])
            result_ml = round((dose * 10) / 4000, 2)

            final_result = round(result_ml * multiplication, 2)

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('tazocin.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, error=error, update_date=UPDATE_DATE)


@app.route('/unasyun', methods=['GET', 'POST'])
def unasyun_route():
    dose = None
    result_ml = None
    final_result = None
    multiplication = None
    error = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])
            result_ml = round((dose * 8) / 3000, 2)

            final_result = round(result_ml * multiplication, 2)

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('unasyun.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, error=error, update_date=UPDATE_DATE)


@app.route('/nimbex', methods=['GET', 'POST'])
def nimbex_route():
    dose = None
    result_ml = None
    final_ml = None
    error = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            result_ml = round(dose * 5 / 10, 2)
            final_ml = round(5 - result_ml, 2)

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('nimbex.html', dose=dose, result_ml=result_ml, final_ml=final_ml, error=error, update_date=UPDATE_DATE)


@app.route('/meropenam', methods=['GET', 'POST'])
def meropenam_route():
    dose = None
    result_ml = None
    final_result = None
    multiplication = None
    error = None
    formula_display = None
    content_extra = None

    if request.method == 'POST':
        try:
            dose = float(request.form['dose'])
            multiplication = int(request.form['multiplication'])

            result_ml = round((dose * 20) / 1000, 2)
            final_result = round(result_ml * multiplication, 2)

            if multiplication == 3:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion pump",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักมากกว่า 1,500 กรัม",
                        "กำหนดให้ปริมาณสารละลายยา (ปริมาณยา + สารละลายเชื้อจางยา) = 8 ml.",
                        "(ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องบริหารเข้าผู้ป่วย 3 ml.)",
                        "<div style='text-align: center;'>(3X + สารละลายเจือจางยา Up to 9 ml.)</div>",
                        "การเตรียมยา:",
                        "1. คำนวณปริมาณยาที่ต้องการใช้เป็นมิลลิลิตร (ml.) แทนค่าในสูตร",
                        "2. ใช้ Syringe ขนาดที่เหมาะสม ดูดปริมาณยาที่ต้องการเตรียมไว้",
                        "3. ใช้ Syringe ขนาด 10 ml. หรือ 20 ml. ดูดปริมาณสารละลายเชื้อจางยาเตรียมไว้",
                        "4. ผสมยาใน Syringe ที่มีสารละลายเชื้อจางยาอยู่ Mixed ให้เข้ากัน",
                        "5. ต่อ Syringe กับ Extension Tube นำไปวางบน Syringe pump กด Start ตั้งอัตราเร็ว 6 ml/hr.",
                        "6. Purge ยาให้ทั่วท่อโดยการดัน Syringe 3 ml. แล้วจึงบริหารผู้ป่วย",
                    ]
                }

            elif multiplication == 6:
                content_extra = {
                    "message": "การบริหารยาโดย Intermittent intravenous infusion.",
                    "details": [
                        "สำหรับทารกที่มีน้ำหนักน้อยกว่า 1,500 กรัม",
                        "1. กำหนดให้สารละลายยาซึ่งบริหารเข้าสู่ผู้ป่วยปริมาณเท่ากับ 1 ml.",
                        "2. ให้ X คือ ปริมาณยาที่ต้องการเตรียม กำหนดสูตรในการเตรียมสารละลายยา ดังนี้:",
                        "<div style='text-align: center;'>6X + สารละลายเจือจางยา Up to 6 ml.</div>",
                        "3. จากข้อ 2 จะได้สารละลายทั้งหมด 6 ml. ซึ่งหมายถึง ความจุของ Extension Tube ประมาณ 5 ml. + Volume ที่ต้องการบริหารเข้าสู่ผู้ป่วย 1 ml.",
                        "4. บริหารยาโดยใช้ Syringe pump ตั้งอัตราเร็ว 2 ml/hr.",
                    ]
                }

        except (ValueError, KeyError) as e:
            error = f"กรุณาใส่ข้อมูลที่ถูกต้อง: {str(e)}"

    return render_template('meropenam.html', dose=dose, result_ml=result_ml, final_result=final_result, multiplication=multiplication, content_extra=content_extra, formula_display=formula_display, error=error, update_date=UPDATE_DATE)

@app.route('/phenobarbital', methods=['GET'])
def phenobarbital_route():
    return render_template('phenobarbital.html', update_date=UPDATE_DATE)



# ฟังก์ชันช่วยคำนวณ PMA
def calculate_pma_route(gestational_age_weeks, gestational_age_days, postnatal_age_days):
    total_days = (gestational_age_weeks * 7) + gestational_age_days + postnatal_age_days
    pma_weeks = total_days // 7
    pma_days = total_days % 7
    calc = pma_weeks + round(pma_days / 7, 0)
    return pma_weeks, pma_days, calc

# Route สำหรับคำนวณ PMA
@app.route('/calculate_pma', methods=['GET', 'POST'])
def calculate_pma_route():
    if request.method == 'POST':
        # รับค่าจากฟอร์ม
        gestational_age_weeks = int(request.form['gestational_age_weeks'])
        gestational_age_days = int(request.form['gestational_age_days'])
        postnatal_age_days = int(request.form['postnatal_age_days'])
        bw = float(request.form['bw'])  # น้ำหนักแรกเกิด

        # คำนวณ PMA
        total_gestational_age_days = (gestational_age_weeks * 7) + gestational_age_days
        total_pma_days = total_gestational_age_days + postnatal_age_days
        pma_weeks = total_pma_days // 7
        pma_days = total_pma_days % 7
        calc = total_pma_days // 7

        # ส่งค่าไปที่ template เพื่อแสดงผลลัพธ์ พร้อมกับ update_date
        return render_template('pma_template.html', pma_weeks=pma_weeks, pma_days=pma_days, calc=calc, bw=bw, postnatal_days=postnatal_age_days, update_date=UPDATE_DATE)
    
    # ถ้าเป็น GET request จะให้แสดงหน้า form
    return render_template('pma_template.html', update_date=UPDATE_DATE)

# Route สำหรับหน้าแสดงการคำนวณยา
@app.route('/drug_calculation', methods=['POST'])
def drug_calculation():
    pma_weeks = request.form.get('pma_weeks')
    pma_days = request.form.get('pma_days')
    calc = request.form.get('calc')
    bw = request.form.get('bw')
    postnatal_days = request.form.get('postnatal_days')

    # ตรวจสอบว่าทุกค่ามีการส่งมาแล้ว
    if not all([pma_weeks, pma_days, calc, bw, postnatal_days]):
        return "Invalid data received", 400

    # แปลงค่าที่รับมาเป็น float และปัดเศษน้ำหนักให้เป็นจำนวนเต็ม
    bw = math.ceil(float(bw))  # ใช้ math.ceil เพื่อปัดน้ำหนักขึ้นให้เป็นจำนวนเต็ม

    # เพิ่มตัวอย่างการคำนวณโดยใช้ค่าตัวแปร
    dose = float(calc) * bw  # ตัวอย่างการคำนวณโดยการคูณ calc ด้วยน้ำหนัก

    # ส่งข้อมูลไปยัง template drug_calculation.html
    return render_template(
        'drug_calculation.html',
        pma_weeks=pma_weeks,
        pma_days=pma_days,
        calc=calc,
        bw=bw,
        postnatal_days=postnatal_days,
        dose=dose,  # ส่งผลลัพธ์การคำนวณไปยัง template
        update_date=UPDATE_DATE
    )




@app.route('/ampicillin_dose')
def ampicillin_dose():
    # รับค่าจาก query parameters
    pma_weeks = request.args.get('pma_weeks')
    pma_days = request.args.get('pma_days')
    calc = request.args.get('calc')
    postnatal_days = request.args.get('postnatal_days')
    bw = request.args.get('bw')

    # ตรวจสอบค่าที่ได้รับ
    if not all([pma_weeks, pma_days, calc, bw, postnatal_days]):
        return "Invalid data received - missing parameters", 400

    try:
        pma_weeks = int(pma_weeks)
        pma_days = int(pma_days)
        calc = float(calc)
        postnatal_days = int(postnatal_days)
        bw = float(bw)
    except ValueError:
        return "Invalid data received - value error", 400

    # คำนวณปริมาณยาสำหรับทารก
    avg_dose_per_kg = 100  # ค่าปริมาณยาต่อกิโลกรัม เช่น 100 mg/kg
    calculated_dose = math.ceil(avg_dose_per_kg * bw)  # ปัดเศษทศนิยมขึ้น

    # ส่งค่าไปที่ template พร้อมกับ update_date และปริมาณยาที่คำนวณได้
    return render_template('ampicillin_dose.html', pma_weeks=pma_weeks, pma_days=pma_days, calc=calc, postnatal_days=postnatal_days, bw=bw, calculated_dose=calculated_dose, update_date=UPDATE_DATE)


# Route สำหรับการคำนวณปริมาณยา Gentamicin
@app.route('/gentamicin_dose')
def gentamicin_dose():
    # รับค่าจาก query parameters
    pma_weeks = request.args.get('pma_weeks')
    pma_days = request.args.get('pma_days')
    calc = request.args.get('calc')
    postnatal_days = request.args.get('postnatal_days')
    bw = request.args.get('bw')

    # พิมพ์ค่าที่ได้รับจาก query parameters เพื่อการตรวจสอบ
    print(f"Received values - pma_weeks: {pma_weeks}, pma_days: {pma_days}, calc: {calc}, postnatal_days: {postnatal_days}, bw: {bw}")

    # ตรวจสอบค่าที่ได้รับ
    if not all([pma_weeks, pma_days, calc, postnatal_days, bw]):
        return "Invalid data received - missing parameters", 400

    try:
        pma_weeks = int(pma_weeks)
        pma_days = int(pma_days)
        calc = float(calc)
        postnatal_days = int(postnatal_days)
        bw = float(bw)
    except ValueError:
        return "Invalid data received - value error", 400

    # กำหนดค่า dose ตาม PMA และ postnatal age
    recommended_dose_per_kg = None

    # ตรวจสอบเงื่อนไขตามช่วงอายุเพื่อกำหนด dose
    if pma_weeks <= 29 and postnatal_days <= 7:
        recommended_dose_per_kg = 5.0  # mg/kg
    elif pma_weeks <= 29 and postnatal_days <= 28:
        recommended_dose_per_kg = 4.0  # mg/kg
    elif pma_weeks <= 29 and postnatal_days > 28:
        recommended_dose_per_kg = 4.0  # mg/kg
    elif 30 <= pma_weeks <= 34 and postnatal_days <= 7:
        recommended_dose_per_kg = 4.5  # mg/kg
    elif 30 <= pma_weeks <= 34 and postnatal_days > 7:
        recommended_dose_per_kg = 4.0  # mg/kg
    elif pma_weeks >= 35:
        recommended_dose_per_kg = 4.0  # mg/kg

    if recommended_dose_per_kg is None:
        return "No suitable dose found for the given PMA and postnatal age", 400

    # คำนวณปริมาณยาที่ควรได้รับ
    calculated_dose = recommended_dose_per_kg * bw
    calculated_dose = round(calculated_dose)  # ปัดเศษเป็นจำนวนเต็ม

    # พิมพ์ค่า dose ที่คำนวณได้เพื่อการตรวจสอบ
    print(f"Calculated dose: {calculated_dose} mg")

    # ส่งค่าไปที่ template พร้อมกับ update_date
    return render_template('gentamicin_dose.html', pma_weeks=pma_weeks, pma_days=pma_days, calc=calc, postnatal_days=postnatal_days, bw=bw, calculated_dose=calculated_dose, update_date=UPDATE_DATE)



@app.route('/cloxacillin_dose')
def cloxacillin_dose():
    # รับค่าจาก query parameters
    pma_weeks = request.args.get('pma_weeks')
    pma_days = request.args.get('pma_days')
    calc = request.args.get('calc')
    postnatal_days = request.args.get('postnatal_days')
    bw = request.args.get('bw')

    # ตรวจสอบค่าที่ได้รับ
    if not all([pma_weeks, pma_days, calc, postnatal_days, bw]):
        return "Invalid data received - missing parameters", 400

    try:
        pma_weeks = int(pma_weeks)
        pma_days = int(pma_days)
        calc = float(calc)
        postnatal_days = int(postnatal_days)
        bw = float(bw)
    except ValueError:
        return "Invalid data received - value error", 400

    # กำหนดค่า dose ตาม PMA และ postnatal age
    recommended_dose_per_kg = None

    if pma_weeks <= 29 and postnatal_days <= 28:
        recommended_dose_per_kg = 40.0
    elif 30 <= pma_weeks <= 36 and postnatal_days <= 14:
        recommended_dose_per_kg = 40.0
    elif 30 <= pma_weeks <= 36 and postnatal_days > 14:
        recommended_dose_per_kg = 40.0
    elif 37 <= pma_weeks <= 44 and postnatal_days <= 7:
        recommended_dose_per_kg = 40.0
    elif 37 <= pma_weeks <= 44 and postnatal_days > 7:
        recommended_dose_per_kg = 40.0
    elif pma_weeks >= 45:
        recommended_dose_per_kg = 40.0

    if recommended_dose_per_kg is None:
        return "No suitable dose found for the given PMA and postnatal age", 400

    # คำนวณปริมาณยาที่ควรได้รับ
    calculated_dose = recommended_dose_per_kg * bw
    calculated_dose = round(calculated_dose)  # ปัดเศษเป็นจำนวนเต็ม

    # พิมพ์ค่า dose ที่คำนวณได้เพื่อการตรวจสอบ
    print(f"Calculated dose: {calculated_dose} mg")

    # ส่งค่าไปที่ template พร้อมกับ update_date
    return render_template('cloxacillin_dose.html', pma_weeks=pma_weeks, pma_days=pma_days, calc=calc, postnatal_days=postnatal_days, bw=bw, calculated_dose=calculated_dose, update_date=UPDATE_DATE)





@app.route('/aminophylline_dose')
def aminophylline_dose():
    # รับค่าจาก query parameters
    pma_weeks = request.args.get('pma_weeks')
    pma_days = request.args.get('pma_days')
    calc = request.args.get('calc')
    postnatal_days = request.args.get('postnatal_days')
    bw = request.args.get('bw')

    # ตรวจสอบค่าที่ได้รับ
    if not all([pma_weeks, pma_days, calc, postnatal_days, bw]):
        return "Invalid data received - missing parameters", 400

    try:
        pma_weeks = int(pma_weeks)
        pma_days = int(pma_days)
        calc = float(calc)
        postnatal_days = int(postnatal_days)
        bw = float(bw)
    except ValueError:
        return "Invalid data received - value error", 400

    # คำนวณ Loading dose และ Maintenance dose
    loading_dose = round(bw * 8, 2)  # BW x 8 mg/kg for loading dose
    maintenance_dose_min = round(bw * 1.5, 2)  # BW x 1.5 mg/kg for maintenance dose (minimum)
    maintenance_dose_max = round(bw * 3, 2)    # BW x 3 mg/kg for maintenance dose (maximum)

    # ส่งค่าไปที่ template พร้อมกับ update_date
    return render_template('aminophylline_dose.html', pma_weeks=pma_weeks, pma_days=pma_days, calc=calc, postnatal_days=postnatal_days, bw=bw, loading_dose=loading_dose, maintenance_dose_min=maintenance_dose_min, maintenance_dose_max=maintenance_dose_max, update_date=UPDATE_DATE)



@app.route('/amphotericinB_dose')
def amphotericinB_dose():
    # รับค่าจาก query parameters
    pma_weeks = request.args.get('pma_weeks')
    pma_days = request.args.get('pma_days')
    calc = request.args.get('calc')
    postnatal_days = request.args.get('postnatal_days')
    bw = request.args.get('bw')

    # ตรวจสอบค่าที่ได้รับ
    if not all([pma_weeks, pma_days, calc, postnatal_days, bw]):
        return "Invalid data received - missing parameters", 400

    try:
        pma_weeks = int(pma_weeks)
        pma_days = int(pma_days)
        calc = float(calc)
        postnatal_days = int(postnatal_days)
        bw = float(bw)
    except ValueError:
        return "Invalid data received - value error", 400

    # คำนวณ Maintenance dose for Amphotericin B
    maintenance_dose_min = round(bw * 1.0, 2)  # 1 mg/kg for the minimum maintenance dose
    maintenance_dose_max = round(bw * 1.5, 2)  # 1.5 mg/kg for the maximum maintenance dose

    # ส่งค่าไปที่ template พร้อมกับ update_date
    return render_template('amphotericinB_dose.html', pma_weeks=pma_weeks, pma_days=pma_days, calc=calc, postnatal_days=postnatal_days, bw=bw, maintenance_dose_min=maintenance_dose_min, maintenance_dose_max=maintenance_dose_max, update_date=UPDATE_DATE)



@app.route('/acyclovir_dose')
def acyclovir_dose():
    # รับค่าจาก query parameters
    pma_weeks = request.args.get('pma_weeks')
    pma_days = request.args.get('pma_days')
    calc = request.args.get('calc')
    postnatal_days = request.args.get('postnatal_days')
    bw = request.args.get('bw')

    # ตรวจสอบค่าที่ได้รับ
    if not all([pma_weeks, pma_days, calc, postnatal_days, bw]):
        return "Invalid data received - missing parameters", 400

    try:
        pma_weeks = int(pma_weeks)
        pma_days = int(pma_days)
        calc = float(calc)
        postnatal_days = int(postnatal_days)
        bw = float(bw)
    except ValueError:
        return "Invalid data received - value error", 400

    # Example dose calculation (can be customized)
    dose = bw * 20  # Example of a dose calculation for Acyclovir (20 mg/kg)

    # ส่งค่าไปที่ template พร้อมกับ update_date
    return render_template('acyclovir_dose.html', pma_weeks=pma_weeks, pma_days=pma_days, calc=calc, postnatal_days=postnatal_days, bw=bw, dose=dose, update_date=UPDATE_DATE)

@app.route('/vancomycin_dose')
def vancomycin_dose():
    # Retrieve values from query parameters
    pma_weeks = request.args.get('pma_weeks')
    pma_days = request.args.get('pma_days')
    calc = request.args.get('calc')
    postnatal_days = request.args.get('postnatal_days')
    bw = request.args.get('bw')

    # Print statements for debugging
    print(f"pma_weeks: {pma_weeks}, pma_days: {pma_days}, calc: {calc}, postnatal_days: {postnatal_days}, bw: {bw}")

    # Check if all necessary parameters are present
    if not all([pma_weeks, pma_days, calc, postnatal_days, bw]):
        print("Missing parameters, returning 400")
        return "Invalid data received - missing parameters", 400

    try:
        # Convert to appropriate data types
        pma_weeks = int(pma_weeks)
        pma_days = int(pma_days)
        calc = float(calc)
        postnatal_days = int(postnatal_days)
        bw = float(bw)
    except ValueError:
        print("Value error occurred, returning 400")
        return "Invalid data received - value error", 400

    # Calculate Maintenance dose for vancomycin
    maintenance_dose_min = round(bw * 10)  # 10 mg/kg for the minimum maintenance dose
    maintenance_dose_max = round(bw * 15)  # 15 mg/kg for the maximum maintenance dose
    
    # Use one of these or combine them as needed
    calculated_dose = f"{maintenance_dose_min} mg - {maintenance_dose_max} mg"

    # Pass the data to the template
    return render_template(
        'vancomycin_dose.html',
        pma_weeks=pma_weeks,
        pma_days=pma_days,
        calc=calc,
        postnatal_days=postnatal_days,
        bw=bw,
        calculated_dose=calculated_dose,  # Corrected to ensure this is defined
        update_date=UPDATE_DATE  # Make sure UPDATE_DATE is defined elsewhere
    )









if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)











