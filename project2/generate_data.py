import pandas as pd
import random
import sklearn.utils

'''
問題 : 根據一個人的身體質量指標, 判斷出該人是否為三高(血糖、血脂、血壓)風險族群
    BMI : 18.5 ~ 23.9為正常
        BMI公式 : Weight / Height^2
    體脂率 : 男性>=25%, 女性>=32%為肥胖標準
        體脂公式 : (1.2 * BMI) + (0.23 * Age - 5.4) - (10.8 * Sex)
        Sex : 男性為1, 女性為0
    腰圍 : BMI<18.5 -> 男性腰圍<=95為正常, 女性<=90為正常
           BMI 18.5 ~ 23.9 -> 男性腰圍<=90為正常, 女性<=85為正常
    無脂肪質量指數(FFMI) : 男性>=18為正常，女性>=15為正常
        FFMI公式 : Weight * (1 - 體脂率) / Height^2
    血糖 : <126為正常
    收縮壓 : <120為正常
    舒張壓 : <80為正常
    資料格式 : (性別,年齡,身高,體重,FFMI,腰圍,居住地,血糖,收縮壓,舒張壓,風險)
        Sex : 1/0 (Male/Female)
        Age : 18 ~ 75
        Height : 1.35 ~ 1.95(meter)
        Weight : 30 ~ 110(kilogram)
        FFMI : 公式如上述
        Waistline : 60 ~ 110(centimeter)
        Residence : north/south/west/east
        Glucose : 80 ~ 140
        Systolic : 100 ~ 140
        Diastolic : 70 ~ 90
        Risk : 0/1 (no/yes)
    規則 : 
        1.BMI超標，且體脂率超標為真
        2.BMI適中或低標，且腰圍超標為真
        3.FFMI低標為真
        4.血糖指數超標為真
        5.血管收縮壓和舒張壓超標為真
    備註 : 因為隨機產生的資料大多落在風險為真的區域，故另外產出風險為否的資料平衡訓練集
'''

num = 10000
additional = 6000
feature = ['Sex','Age','Height','Weight','FFMI','Waistline','Residence','Glucose','Systolic','Diastolic','Risk']
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
    if BMI > 23.9:
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
    dataset.loc[i] = [sex,age,hei,wei,FFMI,was,res,glu,syst,dia,risk]

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
    dataset.loc[i] = [sex,age,hei,wei,FFMI,was,res,glu,syst,dia,risk]

dataset = sklearn.utils.shuffle(dataset)
dataset.to_csv('data.csv',index=False)

