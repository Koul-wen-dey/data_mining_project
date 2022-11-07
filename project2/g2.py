import pandas as pd
import random
import sklearn.utils
num = 10000
additional = 6000
feature = ['Sex','Age','BMI','Fat','FFMI','Waistline','Residence','Glucose','Systolic','Diastolic','Label']
dataset = pd.DataFrame(columns=feature)
for i in range(num):
    sex = random.choice([1,0])
    age = random.randint(18,80)
    hei = round(random.uniform(1.3,2.0),3)
    wei = random.randint(30,110)
    was = random.randint(60,110)
    res = random.choice(['north','south','west','east'])
    glu = random.randint(60,140)
    syst = random.randint(80,140)
    dia = random.randint(50,90)
    risk = 0
    BMI = wei / hei**2
    fat = (1.2 * BMI) + (0.23 * age - 5.4) - (10.8 * sex)
    FFMI = round(wei * (1 - fat / 100) / hei**2,3)
    if sex == 1 and fat >=25 or sex == 0 and fat >=32:
            risk = 1
    elif BMI < 18.5:
        if sex == 1 and was > 95 or sex == 0 and was > 90:
            risk = 1
    else:
        if sex == 1 and was > 90 or sex == 0 and was > 85:
            risk = 1
    if sex == 1 and FFMI < 18 or sex == 0 and FFMI < 15:
        risk = 1
    elif glu >= 126:
        risk = 1
    elif syst > 120 and dia > 80:
        risk = 1 
    dataset.loc[i] = [sex,age,BMI,fat,FFMI,was,res,glu,syst,dia,risk]

for i in range(num,num+additional):
    sex = random.choice([1,0])
    age = random.randint(18,80)
    hei = round(random.uniform(1.8,2.0),3)
    wei = random.randint(30,70)
    was = random.randint(80,85)
    res = random.choice(['north','south','west','east'])
    glu = random.randint(60,126)
    syst = random.randint(80,120)
    dia = random.randint(50,80)
    risk = 0
    BMI = wei / hei**2
    fat = (1.2 * BMI) + (0.23 * age - 5.4) - (10.8 * sex)
    FFMI = round(wei * (1 - fat / 100) / hei**2,3)
    if sex == 1 and fat >= 25 or sex == 0 and fat >= 32 or sex == 1 and FFMI < 18 or sex == 0 and FFMI < 15:
        i -= 1
    dataset.loc[i] = [sex,age,BMI,fat,FFMI,was,res,glu,syst,dia,risk]

dataset = sklearn.utils.shuffle(dataset)
dataset.to_csv('data2.csv',index=False)