import numpy as np
import pandas as pd


def make_df_intercept():    
    x_a = []
    for i in range(0, 200):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_a.append(numb)
        
    y_a = []
    for i in x_a:
        num = 3.5 * i + 60 + np.random.normal(loc=0.0, scale=50.0, size=None)
        y_a.append(num)
        
    x_b = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_b.append(numb)
        
    y_b = []
    for i in x_b:
        num = 3.5 * i + -150 + np.random.normal(loc=0.0, scale=50.0, size=None)
        y_b.append(num)
        
    dict_a = {'x': x_a , 'y' : y_a}
    dict_b = {'x': x_b , 'y' : y_b}
    df_a = pd.DataFrame(dict_a)
    df_b = pd.DataFrame(dict_b)
    df_a['type'] ='A'
    df_b['type'] ='B'
    df_intercept = pd.concat([df_a, df_b])
    return df_intercept

def make_df_slope():    
    x_a = []
    for i in range(0, 200):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_a.append(numb)
        
    y_a = []
    for i in x_a:
        num = 3.5 * i + 20 + np.random.normal(loc=0.0, scale=50.0, size=None)
        y_a.append(num)
        
    x_b = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_b.append(numb)
        
    y_b = []
    for i in x_b:
        num = 10 * i + 20 + np.random.normal(loc=0.0, scale=50.0, size=None)
        y_b.append(num)
        
    dict_a = {'x': x_a , 'y' : y_a}
    dict_b = {'x': x_b , 'y' : y_b}
    df_a = pd.DataFrame(dict_a)
    df_b = pd.DataFrame(dict_b)
    df_a['type'] ='A'
    df_b['type'] ='B'
    df_slope = pd.concat([df_a, df_b])
    return df_slope


def make_df_complex():    
    x_a = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_a.append(numb)
        
    y_a = []
    for i in x_a:
        num = 3.5 * i + 250 + np.random.normal(loc=0.0, scale=100.0, size=None)
        y_a.append(num)
        
    x_b = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_b.append(numb)
        
    y_b = []
    for i in x_b:
        num = -2 * i + 20 + np.random.normal(loc=0.0, scale=70.0, size=None)
        y_b.append(num)
    
    x_c = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=20.0, size=None)
        x_c.append(numb)
        
    y_c = []
    for i in x_c:
        num = 5 * i + -230 + np.random.normal(loc=0.0, scale= 80.0, size=None)
        y_c.append(num)
    
    x_d = []
    for i in range(0, 100):
        numb = np.random.normal(loc=100.0, scale=40.0, size=None)
        x_d.append(numb)
        
    y_d = []
    for i in x_d:
        num = 5 * i + 246 + np.random.normal(loc=0.0, scale = 80.0, size=None)
        y_d.append(num)
    
    dict_a = {'x': x_a , 'y' : y_a}
    dict_b = {'x': x_b , 'y' : y_b}
    dict_c = {'x': x_c , 'y' : y_c}
    dict_d = {'x': x_d , 'y' : y_d}
    df_a = pd.DataFrame(dict_a)
    df_b = pd.DataFrame(dict_b)
    df_c = pd.DataFrame(dict_c)
    df_d = pd.DataFrame(dict_d)
    
    df_a['type_a'] ='A'
    df_b['type_a'] ='A'
    df_a['type_b'] ='A'
    df_b['type_b'] ='B'
    df_c['type_a'] ='B'
    df_d['type_a'] ='B'
    df_c['type_b'] ='A'
    df_d['type_b'] ='B'
    
    df_complex = pd.concat([df_a, df_b, df_c, df_d])
    return df_complex