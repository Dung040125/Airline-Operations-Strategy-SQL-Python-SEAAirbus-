import streamlit as st         
import pandas as pd             
import numpy as np               
import altair as alt
import pyodbc                      
import matplotlib.pyplot as plt    
import plotly.express as px      

theme_plotly = None 
# Page configuration

st.set_page_config(
    page_title="Group 6 - Final Project",
    layout="wide",
    initial_sidebar_state="expanded")
alt.themes.enable("dark")

st.cache_resource.clear()
@st.cache_resource
def init_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};SERVER="+ st.secrets["server"]
        + ";DATABASE="+ st.secrets["database"]
        + ";UID="+ st.secrets["username"]
        + ";PWD="+ st.secrets["password"]
    )
st.write("This is the connection string (check if details are correct, then delete when working:")
st.write("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+ st.secrets["server"]
        + ";DATABASE="+ st.secrets["database"]
        + ";UID="+ st.secrets["username"]
        + ";PWD="+ st.secrets["password"])
conn = init_connection()
st.sidebar.image("sea.jpg", caption="SEA AIRBUS")
st.sidebar.title('Group 6')
options = st.sidebar.radio('Pages',
                            options=['Local CEO','CEO','CUSTOMERS'])
@st.cache_data(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()
def run_query_df(query):
    data=conn.execute(query)
    df=pd.DataFrame.from_dict(data.fetchall())
    [nrows,ncols]=df.shape
    actualcols=2
    df2=pd.DataFrame(index=np.arange(nrows), columns=np.arange(actualcols))
    for i in np.arange(0,nrows):
        strfull=df.iloc[i,0]
        for j in np.arange(0,actualcols):
            df2.iloc[i,j]=strfull[j]
    return df2
def run_query_df3(query):
    data=conn.execute(query)
    df=pd.DataFrame.from_dict(data.fetchall())
    [nrows,ncols]=df.shape
    actualcols=3
    df3=pd.DataFrame(index=np.arange(nrows), columns=np.arange(actualcols))
    for i in np.arange(0,nrows):
        strfull=df.iloc[i,0]
        for j in np.arange(0,actualcols):
            df3.iloc[i,j]=strfull[j]
    return df3
def run_query_df33(query):
    data=conn.execute(query)
    df=pd.DataFrame.from_dict(data.fetchall())
    [nrows,ncols]=df.shape
    actualcols=4
    df3=pd.DataFrame(index=np.arange(nrows), columns=np.arange(actualcols))
    for i in np.arange(0,nrows):
        strfull=df.iloc[i,0]
        for j in np.arange(0,actualcols):
            df3.iloc[i,j]=strfull[j]
    return df3

def run_query_df333(query):
    data=conn.execute(query)
    df=pd.DataFrame.from_dict(data.fetchall())
    [nrows,ncols]=df.shape
    actualcols=5
    df3=pd.DataFrame(index=np.arange(nrows), columns=np.arange(actualcols))
    for i in np.arange(0,nrows):
        strfull=df.iloc[i,0]
        for j in np.arange(0,actualcols):
            df3.iloc[i,j]=strfull[j]
    return df3

if options =="Local CEO":
    col1, col2, col3 = st.columns([0.4,0.5,0.1])
    with col1:
        st.image("sea.jpg", width=330)
    with col2:
        st.title("LOCAL CEO")
    with col3:
        st.image("Logo HSB.png", width=100)
    col = st.columns((2, 2), gap='medium')
    with col[0]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):  
            df_age=run_query_df("SELECT A.COUNTRY, COUNT(T.SEATNO) AS NUM_OF_FLIGHT  FROM AIRPORT A INNER JOIN FLIGHT F ON A.FLIGHTNO = F.FLIGHTNO INNER JOIN BOOKING_OFFICE BO ON F.FLIGHTNO =BO.FLIGHTNO LEFT JOIN TICKET T ON BO.OFFICE_ID=T.OFFICE_ID WHERE T.OFFICE_ID IN ('MNLOBO','HNOBO', 'HCMOBO','JKTOBO','SRBOBO','QZOBO') GROUP BY A.COUNTRY;")
            st.write(df_age)
        df_age.columns=['COUNTRY','NUM_OF_FLIGHT']
        fig=plt.bar(df_age['COUNTRY'], df_age['NUM_OF_FLIGHT'],color='#5F6F94')
        plt.xlabel('COUNTRY', fontweight='bold')
        plt.ylabel('NUM_OF_FLIGHT', fontweight='bold')
        plt.title("NUMBER OF BOOKED FLIGHT", fontweight='bold', fontsize=18)
        plt.legend() 
        st.pyplot(plt)
    with col[1]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):
            df_2 = run_query_df3("SELECT CLASS_TYPE.CLASS_TYPE AS CLASS, BOOKING_OFFICE.OFFICE_ID, SUM(CAST(FARE.FINAL_PRICE AS DECIMAL(10, 2))) AS REVENUE FROM TICKET JOIN BOOKING_OFFICE ON TICKET.OFFICE_ID = BOOKING_OFFICE.OFFICE_ID JOIN CLASS_TYPE ON BOOKING_OFFICE.OFFICE_ID = CLASS_TYPE.OFFICE_ID JOIN FARE ON CLASS_TYPE.C_TYPE_ID = FARE.C_TYPE_ID GROUP BY CLASS_TYPE.CLASS_TYPE, BOOKING_OFFICE.OFFICE_ID ORDER BY CLASS_TYPE.CLASS_TYPE, BOOKING_OFFICE.OFFICE_ID;")
            st.write(df_2)
        x1e = []
        x2e = []
        x3e = []
        df_2.columns=['TYPE OF TICKETS','OFFICE_ID','REVENUE']   
        for i in range(18):
            if df_2['TYPE OF TICKETS'][i] == 'ECONOMY CLASS':
                x1e.append(df_2['REVENUE'][i])
            if df_2['TYPE OF TICKETS'][i] == 'BUSINESS CLASS':
                x2e.append(df_2['REVENUE'][i])
            if df_2['TYPE OF TICKETS'][i] == 'PRIVATE CLASS':
                x3e.append(df_2['REVENUE'][i])
        width = 0.2
        print(x1e)
        r = np.arange(6)
        plt.plot(['HCMOBO', 'HNOBO', 'JKTOBO', 'MNLOBO', 'QZOBO', 'SRBOBO'], x1e, 'go--', label='ECONOMY CLASS')
        plt.plot(['HCMOBO', 'HNOBO', 'JKTOBO', 'MNLOBO', 'QZOBO', 'SRBOBO'], x2e, 'bo--', label='BUSINESS CLASS')
        plt.plot(['HCMOBO', 'HNOBO', 'JKTOBO', 'MNLOBO', 'QZOBO', 'SRBOBO'], x3e, 'ro--', label='PRIVATE CLASS')
        plt.xlabel('OFFICE ID', fontweight='bold') 
        plt.ylabel('REVENUE', fontweight='bold')
        plt.title("REVENUE GROWTH RATE", fontsize=18, fontweight='bold')
        plt.legend()
        st.pyplot(plt)
    with col[0]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):
            df_gender=run_query_df("SELECT A.COUNTRY, SUM(CAST(FARE.COST AS DECIMAL(10, 2))) AS PROFIT FROM AIRPORT A INNER JOIN FLIGHT F ON A.FLIGHTNO = F.FLIGHTNO INNER JOIN BOOKING_OFFICE BO ON F.FLIGHTNO = BO.FLIGHTNO INNER JOIN TICKET T ON BO.OFFICE_ID = T.OFFICE_ID INNER JOIN CLASS_TYPE CT ON F.FLIGHTNO = CT.FLIGHTNO INNER JOIN FARE ON CT.C_TYPE_ID = FARE.C_TYPE_ID GROUP BY A.COUNTRY")
            st.write(df_gender)
        df_gender.columns=['COUNTRY','PROFIT']
        sizes= df_gender['PROFIT']
        labels=df_gender['COUNTRY']
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#7F9F80', '#F9E897', '#FFC374'])
        plt.title("PROFIT AREA", fontweight='bold', fontsize=18)
        plt.axis('equal')
        st.pyplot(plt)
    with col[1]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):
            df_3 = run_query_df3("SELECT  A.COUNTRY,  SUM(CAST(FARE.OPERATION_COST AS DECIMAL(10, 2))) AS OPERATION_COST, SUM(CAST(FARE.FINAL_PRICE AS DECIMAL(10, 2))) AS REVENUE FROM  AIRPORT A INNER JOIN FLIGHT F ON A.FLIGHTNO = F.FLIGHTNO INNER JOIN BOOKING_OFFICE BO ON F.FLIGHTNO = BO.FLIGHTNO INNER JOIN TICKET T ON BO.OFFICE_ID = T.OFFICE_ID INNER JOIN CLASS_TYPE CT ON F.FLIGHTNO = CT.FLIGHTNO INNER JOIN FARE ON CT.C_TYPE_ID = FARE.C_TYPE_ID GROUP BY  A.COUNTRY;")
            st.write(df_3)
        x11e = []
        x22e = []
        width=0.2
        r=np.arange(3)
        df_3.columns=['COUNTRY','OPERATING_COST','REVENUE']
        plt.bar(r, df_3['OPERATING_COST'], color='#FDF0F0',
                width=width, edgecolor='black',
                label='OPERATING_COST')
        plt.bar(r + width, df_3['REVENUE'], color='#F1B4BB',
                width=width, edgecolor='black',
                label='REVENUE')
        plt.xticks(r + width / 2, df_3['COUNTRY'])
        plt.xlabel('COUNTRY', fontweight='bold')
        plt.ylabel('REVENUE AND OPERATING COST RATE', fontweight='bold')
        plt.title("REVENUE AND OPERATING COST RATE", fontweight='bold', fontsize=18)
        plt.legend()
        st.pyplot(plt)
elif options =="CEO":
    col1, col2, col3 = st.columns([0.4,0.35,0.1])
    with col1:
        st.image("sea.jpg", width=330)
    with col2:
        st.title("CEO")
    with col3:
        st.image("Logo HSB.png", width=100)
    col = st.columns((2, 2), gap='medium')
    with col[0]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):
            df_cars=run_query_df("SELECT CLASS_TYPE, COUNT(CLASS_TYPE) AS NUM_OF_CLASS FROM TICKET WHERE CLASS_TYPE IN ('ECONOMY CLASS','BUSINESS CLASS', 'PRIVATE CLASS') GROUP BY CLASS_TYPE;")
            st.write(df_cars)
        df_cars.columns=['BOOKED CLASS','NUMBER OF BOOKED CLASS']
        fig=plt.bar(df_cars['BOOKED CLASS'], df_cars['NUMBER OF BOOKED CLASS'],color='#eab159')
        plt.xlabel('BOOKED CLASS', fontweight='bold')
        plt.ylabel('NUMBER OF BOOKED CLASS', fontweight='bold')
        plt.title("NUMBER OF BOOKED CLASS", fontweight='bold', fontsize=18)
        plt.legend()
        st.pyplot(plt)
    with col[1]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):
            df_pie=run_query_df("SELECT A.CITY, COUNT(T.SEATNO) AS NUM_OF_FLIGHT  FROM AIRPORT A INNER JOIN FLIGHT F ON A.FLIGHTNO = F.FLIGHTNO INNER JOIN BOOKING_OFFICE BO ON F.FLIGHTNO =BO.FLIGHTNO LEFT JOIN TICKET T ON BO.OFFICE_ID=T.OFFICE_ID WHERE T.OFFICE_ID IN ('MNLOBO','HNOBO', 'HCMOBO','JKTOBO','SRBOBO','QZOBO') GROUP BY A.CITY ;")
            st.write(df_pie)
        df_pie.columns=['CITY','NUMBER OF BOOKED FLIGHT']
        sizes= df_pie['NUMBER OF BOOKED FLIGHT']
        labels=df_pie['CITY']
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['#7F9F80', '#F9E897', '#FFC374','#FFB1B1', '#FFCBCB', '#FFEAE3'])
        plt.title("NUMBER OF BOOKED FLIGHT", fontweight='bold', fontsize=18)
        plt.axis('equal')
        st.pyplot(plt)
    with col[0]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):
            df_line=run_query_df("SELECT AIRPORT.COUNTRY, SUM(CAST(FARE.FINAL_PRICE AS DECIMAL(10, 2)) - CAST(FARE.OPERATION_COST AS DECIMAL(10, 2))) AS PROFIT FROM FARE JOIN CLASS_TYPE ON FARE.C_TYPE_ID = CLASS_TYPE.C_TYPE_ID JOIN TICKET ON CLASS_TYPE.OFFICE_ID = TICKET.OFFICE_ID JOIN BOOKING_OFFICE ON BOOKING_OFFICE.OFFICE_ID = TICKET.OFFICE_ID JOIN AIRPORT ON AIRPORT.FLIGHTNO = BOOKING_OFFICE.FLIGHTNO GROUP BY AIRPORT.COUNTRY ORDER BY AIRPORT.COUNTRY;")
            st.write(df_line)
        df_line.columns=['FLIGHTNO','PROFIT']
        fig=plt.plot(df_line['FLIGHTNO'], df_line['PROFIT'],color='#4F6F52')
        plt.xlabel('FLIGHTNO', fontweight='bold')
        plt.ylabel('PROFIT', fontweight='bold')
        plt.title("PROFITS BY COUNTRY", fontweight='bold', fontsize=18)
        plt.legend()
        st.pyplot(plt)
    with col[1]:
        plt.figure(figsize=(8, 5))  
        with st.expander('Data table'):
            df_clre = run_query_df("SELECT CLASS_TYPE.CLASS_TYPE, SUM(CAST(FARE.FINAL_PRICE AS DECIMAL(10, 2))) AS REVENUE FROM TICKET JOIN CLASS_TYPE ON TICKET.OFFICE_ID = CLASS_TYPE.OFFICE_ID JOIN FARE ON CLASS_TYPE.C_TYPE_ID = FARE.C_TYPE_ID GROUP BY CLASS_TYPE.CLASS_TYPE;SELECT CLASS_TYPE.CLASS_TYPE, SUM(CAST(FARE.FINAL_PRICE AS DECIMAL(10, 2))) AS REVENUE FROM TICKET JOIN CLASS_TYPE ON TICKET.OFFICE_ID = CLASS_TYPE.OFFICE_ID JOIN FARE ON CLASS_TYPE.C_TYPE_ID = FARE.C_TYPE_ID GROUP BY CLASS_TYPE.CLASS_TYPE;")
            st.write(df_clre)
        df_clre.columns=['TYPE OF TICKETS','REVENUE']
        fig = plt.bar(df_clre['TYPE OF TICKETS'], df_clre['REVENUE'],color='#e18d96')
        plt.xlabel('TYPE OF TICKETS', fontweight='bold')
        plt.ylabel('REVENUE', fontweight='bold')
        plt.title("REVENUE BY TYPE OF TICKET", fontsize=18, fontweight='bold')
        st.pyplot(plt)

elif options =="CUSTOMERS":
    col1, col2, col3 = st.columns([0.4,0.5,0.1])
    with col1:
        st.image("sea.jpg", width=330)
    with col2:
        st.title("CUSTOMERS")
    with col3:
        st.image("Logo HSB.png", width=100)
    col = st.columns((3, 3), gap='small')
    with col[0]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):
            df_age=run_query_df("SELECT CASE WHEN AGE BETWEEN 0 AND 10 THEN '0-10' WHEN AGE BETWEEN 10 AND 20 THEN '10-20' WHEN AGE BETWEEN 21 AND 30 THEN '21-30' WHEN AGE BETWEEN 31 AND 40 THEN '31-40' WHEN AGE BETWEEN 41 AND 50 THEN '41-50' WHEN AGE BETWEEN 51 AND 60 THEN '51-60' WHEN AGE BETWEEN 61 AND 70 THEN '61-70' WHEN AGE BETWEEN 71 AND 80 THEN '71-80' END AS AGE_GROUP, COUNT(*) AS NUM_OF_PEOPLE FROM TOTAL_PASSENGER GROUP BY  CASE WHEN AGE BETWEEN 0 AND 10 THEN '0-10' WHEN AGE BETWEEN 10 AND 20 THEN '10-20' WHEN AGE BETWEEN 21 AND 30 THEN '21-30' WHEN AGE BETWEEN 31 AND 40 THEN '31-40' WHEN AGE BETWEEN 41 AND 50 THEN '41-50' WHEN AGE BETWEEN 51 AND 60 THEN '51-60' WHEN AGE BETWEEN 61 AND 70 THEN '61-70' WHEN AGE BETWEEN 71 AND 80 THEN '71-80' END")
            st.write(df_age)
        df_age.columns=['AGE GROUPS','NUM_OF_PEOPLE']
        fig=plt.bar(df_age['AGE GROUPS'], df_age['NUM_OF_PEOPLE'],color = ['#e18d96'])
        plt.xlabel('AGE GROUPS', fontweight='bold')
        plt.ylabel('NUM_OF_PEOPLES', fontweight='bold')
        plt.title("AGE CLASSIFICATION OF PASSENGERS", fontweight='bold', fontsize=18)
        plt.legend() 
        st.pyplot(plt)

    with col[1]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):
            df_ticket=run_query_df("SELECT A.COUNTRY, AVG(CAST(FA.FINAL_PRICE AS DECIMAL(10, 2))) AS AVERAGE_PRICE FROM AIRPORT A INNER JOIN FLIGHT F ON A.FLIGHTNO = F.FLIGHTNO INNER JOIN CLASS_TYPE CT ON F.FLIGHTNO = CT.FLIGHTNO INNER JOIN FARE FA ON CT.C_TYPE_ID = FA.C_TYPE_ID GROUP BY A.COUNTRY")
            st.write(df_ticket)
        df_ticket.columns=['COUNTRY','A_PRICE']
        fig=plt.bar(df_ticket['COUNTRY'], df_ticket['A_PRICE'],color= ['#eab159'])
        plt.xlabel('COUNTRY', fontweight='bold')
        plt.ylabel('A_PRICE', fontweight='bold')
        plt.title("AVERAGE TICKET'S PRICE PER COUNTRY", fontweight='bold', fontsize=18)
        plt.legend() 
        st.pyplot(plt)

    col = st.columns((3, 3), gap='small')
    with col[0]:
        plt.figure(figsize=(8, 5))
        with st.expander('Data table'):
            df_class=run_query_df("SELECT CLASS_TYPE, COUNT(CLASS_TYPE) AS QUANTITY,ROUND((COUNT(CLASS_TYPE) * 100.0 / SUM(COUNT(CLASS_TYPE)) OVER()), 2) AS PERCENTAGE FROM TICKET WHERE CLASS_TYPE IN ('ECONOMY CLASS','BUSINESS CLASS', 'PRIVATE CLASS') GROUP BY CLASS_TYPE")
            st.write(df_class)
        df_class.columns=['CLASS_TYPE','QUANTITY']
        sizes= df_class['QUANTITY']
        labels=df_class['CLASS_TYPE']
        plt.pie(sizes, labels=labels, autopct='%1.1f%%',colors= ['Salmon','plum','wheat'])
        plt.title("PERCENTAGE OF FLIGHT CLASSES", fontweight='bold', fontsize=18)
        plt.axis('equal')
        st.pyplot(plt)
    

    with col[1]:
        with st.expander('Data table'):
            query = """
                SELECT 
                    A.COUNTRY, 
                    SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 1 AND 7 THEN 1 ELSE 0 END) AS 'WEEK 1', 
                    SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 8 AND 14 THEN 1 ELSE 0 END) AS 'WEEK 2', 
                    SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 15 AND 21 THEN 1 ELSE 0 END) AS 'WEEK 3', 
                    SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 22 AND 31 THEN 1 ELSE 0 END) AS 'WEEK 4' 
                FROM AIRPORT A 
                INNER JOIN BOOKING_OFFICE BO ON A.FLIGHTNO = BO.FLIGHTNO 
                INNER JOIN TICKET T ON BO.OFFICE_ID = T.OFFICE_ID 
                WHERE MONTH(T.PAYMENT_DATE) = 9 
                GROUP BY A.COUNTRY
            """
            
            df_country = run_query_df333(query)
            st.write(df_country)

        df_country.columns = ['COUNTRY', 'WEEK 1', 'WEEK 2', 'WEEK 3', 'WEEK 4']
        countries = ['VIETNAM', 'PHILIPPINES', 'INDONESIA']
        data = {country: [] for country in countries}

        for index, row in df_country.iterrows():
            country = row['COUNTRY']
            if country in data:
                data[country] = [row['WEEK 1'], row['WEEK 2'], row['WEEK 3'], row['WEEK 4']]

        plt.figure(figsize=(8, 6))
        weeks = ['WEEK 1', 'WEEK 2', 'WEEK 3', 'WEEK 4']
        colors = {'VIETNAM': 'o--', 'PHILIPPINES': 'o--', 'INDONESIA': 'o--'}

        for country in countries:
            plt.plot(weeks, data[country], colors[country], label=country)

        plt.xlabel('Weeks', fontweight='bold')
        plt.ylabel('Quantity', fontweight='bold')
        plt.title("Number of Flights per Week in September in Each Country", fontsize=18, fontweight='bold')
        plt.legend()
        st.pyplot(plt)


    col = st.columns((3, 3), gap='small')
    with col[0]:
        with st.expander('Data table'):
            query = """
                SELECT 	A.COUNTRY,
                SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 1 AND 7 THEN 1 ELSE 0 END) AS 'WEEK 1',
                SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 8 AND 14 THEN 1 ELSE 0 END) AS 'WEEK 2',
                SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 15 AND 21 THEN 1 ELSE 0 END) AS 'WEEK 3',
                SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 22 AND 31 THEN 1 ELSE 0 END) AS 'WEEK 4'
                FROM AIRPORT A 
                INNER JOIN BOOKING_OFFICE BO ON A.FLIGHTNO = BO.FLIGHTNO
                INNER JOIN TICKET T ON BO.OFFICE_ID = T.OFFICE_ID
                WHERE  MONTH(T.PAYMENT_DATE) = 10
                GROUP BY A.COUNTRY 
            """

            df_country = run_query_df333(query)
            st.write(df_country)
        df_country.columns = ['COUNTRY', 'WEEK 1', 'WEEK 2', 'WEEK 3', 'WEEK 4']
        countries = ['VIETNAM', 'PHILIPPINES', 'INDONESIA']
        data = {country: [] for country in countries}

        for index, row in df_country.iterrows():
            country = row['COUNTRY']
            if country in data:
                data[country] = [row['WEEK 1'], row['WEEK 2'], row['WEEK 3'], row['WEEK 4']]
        plt.figure(figsize=(8, 6))
        weeks = ['WEEK 1', 'WEEK 2', 'WEEK 3', 'WEEK 4']
        colors = {'VIETNAM': 'o--', 'PHILIPPINES': 'o--', 'INDONESIA': 'o--'}

        for country in countries:
            plt.plot(weeks, data[country], colors[country], label=country)

        plt.xlabel('Weeks', fontweight='bold')
        plt.ylabel('Quantity', fontweight='bold')
        plt.title("Number of Flights per Week in Octocber in  Each Country", fontsize=18, fontweight='bold')
        plt.legend()
        st.pyplot(plt)

    with col[1]:
        with st.expander('Data table'):
            query = """
                SELECT 	A.COUNTRY,
                SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 1 AND 7 THEN 1 ELSE 0 END) AS 'WEEK 1',
                SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 8 AND 14 THEN 1 ELSE 0 END) AS 'WEEK 2',
                SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 15 AND 21 THEN 1 ELSE 0 END) AS 'WEEK 3',
                SUM(CASE WHEN DAY(T.PAYMENT_DATE) BETWEEN 22 AND 31 THEN 1 ELSE 0 END) AS 'WEEK 4'
                FROM AIRPORT A 
                INNER JOIN BOOKING_OFFICE BO ON A.FLIGHTNO = BO.FLIGHTNO
                INNER JOIN TICKET T ON BO.OFFICE_ID = T.OFFICE_ID
                WHERE  MONTH(T.PAYMENT_DATE) = 11
                GROUP BY A.COUNTRY 
            """

            df_country = run_query_df333(query)
            st.write(df_country)
        df_country.columns = ['COUNTRY', 'WEEK 1', 'WEEK 2', 'WEEK 3', 'WEEK 4']
        countries = ['VIETNAM', 'PHILIPPINES', 'INDONESIA']
        data = {country: [] for country in countries}
        for index, row in df_country.iterrows():
            country = row['COUNTRY']
            if country in data:
                data[country] = [row['WEEK 1'], row['WEEK 2'], row['WEEK 3'], row['WEEK 4']]
        plt.figure(figsize=(8, 6))
        weeks = ['WEEK 1', 'WEEK 2', 'WEEK 3', 'WEEK 4']
        colors = {'VIETNAM': 'o--', 'PHILIPPINES': 'o--', 'INDONESIA': 'o--'}

        for country in countries:
            plt.plot(weeks, data[country], colors[country], label=country)

        plt.xlabel('Weeks', fontweight='bold')
        plt.ylabel('Quantity', fontweight='bold')
        plt.title("Number of Flights per Week in November in Each Country", fontsize=18, fontweight='bold')
        plt.legend()
        st.pyplot(plt)

    
    
    
    
    
    
    
   




    


