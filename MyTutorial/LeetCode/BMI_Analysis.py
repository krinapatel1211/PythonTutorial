def convert_height_in_meter(h):
    h_meter = h/100
    return h_meter

def convert_weight_in_kg(w):
    w_kg = w/2.2
    return w_kg

def calculate_BMI(h, w):
    return (w / (h * h))*10000


height = [180, 170, 170, 140, 180, 150, 185, 165, 150, 140, 155, 182, 170]
weight = [180, 200, 180, 190, 130, 220, 110, 300, 86, 300, 150, 178, 150]
underweight, overweight, normalweight, obesity = {}, {},{},{}
for i in range(len(height)):
    h = height[i]
    w = convert_weight_in_kg(weight[i])
    bmi = calculate_BMI(h, w)
    if bmi <= 18.5:
        underweight['Person'+str(i)] = bmi
    elif bmi > 18.5 and bmi <= 24.9:
        normalweight['Person'+str(i)] = bmi
    elif bmi >= 25 and bmi <= 29.9:
        overweight['Person'+str(i)] = bmi
    else:
        obesity['Person'+str(i)] = bmi
print(underweight)