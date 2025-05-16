# SEA-Airline-Operations-Analytics

![image](https://github.com/user-attachments/assets/3f9efd2e-0759-4c65-9165-f5efc057bbf9)

Database design, SQL implementation, and Streamlit dashboards for a new Southeast Asian airline (SEAAirbus) to support operational planning and strategic insights, initially focusing on operations between Vietnam, Philippines, and Indonesia.
---
## Table of Contents
- [Introduction & Objectives](#introduction--objectives)
- [Database Design](#database-design)
    - [Entity Relationship Diagram (ERD)](#entity-relationship-diagram-erd)
    - [Database Schema](#database-schema)
- [Database Implementation with SQL Server](#database-implementation-with-sql-server)
- [Dashboard Development with SQL & Streamlit](#dashboard-development-with-sql--streamlit)
    - [Dashboards Overview](#dashboards-overview)
        - [Dashboard 1: Local CEO Insights](#dashboard-1-local-ceo-insights)
        - [Dashboard 2: CEO Overview](#dashboard-2-ceo-overview)
        - [Dashboard 3: Customer Analytics](#dashboard-3-customer-analytics)
- [Technologies Used](#technologies-used)
- [Setup and Usage Instructions](#setup-and-usage-instructions)
- [Project Deliverables](#project-deliverables)
- [Design Discussions and Decisions](#design-discussions-and-decisions)

---
## Introduction & Objectives
SEAAirbus, a new premium airline in Southeast Asia (Vietnam, Philippines, Indonesia), requires a robust data foundation and visual analytics tools for efficient operations. This project addresses that need.

**Main Objectives:**
1.  Design and implement a relational database on SQL Server (ERD, schema, fake data).
2.  Develop 3 interactive dashboards (SQL & Streamlit) for Local CEOs, the CEO, and Customers.

---
## Database Design
### Entity Relationship Diagram (ERD)
The ERD model manages information on flights, passengers, bookings, tickets, aircraft, airports, class types, fares, and booking offices.
*   Main Entities: AIRPLANE, FLIGHT, AIRPORT, CABIN_CREW, TICKET, BOOKING_OFFICE, PASSENGERS_A, PASSENGERS_C, CLASS_TYPE, FARE.

<p align="center">
  <img src="https://github.com/user-attachments/assets/52a1eda8-b5a7-4252-bf51-307e32da9ebd" alt="ER Diagram" width="700">
</p>


### Database Schema
Includes main tables such as `AIRPLANE`, `FLIGHT`, `TICKET`, `PASSENGERS_A`, `CLASS_TYPE`, etc., with column details and constraints defined in the SQL script.

---
## Database Implementation with SQL Server
The database was created and populated with fake data on SQL Server using a single SQL script. This script includes `CREATE TABLE` statements for structure definition, integrity constraints (PK, FK, UNIQUE, NOT NULL), and `INSERT INTO` for data loading.
*   SQL Script File: `FINAL TEST 18.5.sql` [View more](https://github.com/Dung040125/SEA-Airline-Operations-Analytics/blob/main/FINAL%20TEST%2018.5.sql)

---
## Dashboard Development with SQL & Streamlit
Three interactive dashboards were built using Streamlit, querying data from SQL Server.

### Dashboards Overview
#### Dashboard 1: Local CEO Insights
*   **Target Audience:** Local CEOs (Vietnam, Philippines, Indonesia).
*   **Objective:** Provide an overview of national operational performance (booked flights, revenue growth, profit, cost structure) to guide market-specific development.
*   **Key Visuals:** Number of Booked Flights by Country, Revenue Growth Rate by Office ID, Profit Area by Country, Revenue and Operating Cost Rate by Country.
<p align="center">
  <img src="https://github.com/user-attachments/assets/7da3916e-116b-4cbc-aeef-beb3aa3f342c" alt="Local CEO Dashboard" width="700">
</p>


*   **Key Insight:** The Philippines leads in bookings and profit, indicating strong potential. Indonesia shows lower figures, requiring tailored strategies for growth. Vietnam demonstrates stability. Revenue growth varies by office and class type, necessitating close monitoring.

#### Dashboard 2: CEO Overview
*   **Target Audience:** Global CEO of SEAAirbus.
*   **Objective:** Offer a holistic view of business operations, class performance, popular destinations, and overall profitability/revenue to support high-level strategic decisions.
*   **Key Visuals:** Number of Booked Class, Number of Booked Flight by Destination, Profits by Country over time, Revenue by Type of Ticket.
<p align="center">
  <img src="https://github.com/user-attachments/assets/d1dfd970-d896-4679-b36c-8860d962c1af" alt="CEO Overview Dashboard" width="700">
</p>
*   **Key Insight:** Business Class is most popular, aligning with the premium airline positioning, while Private Class, despite fewer tickets, generates the highest revenue due to its high value. The Philippines is the most profitable market. Manila is the top booked route. The Indonesian market presents competitive challenges.

#### Dashboard 3: Customer Analytics
*   **Target Audience:** Marketing and Customer Service Departments.
*   **Objective:** Understand passenger demographics (age), class preferences, average ticket prices by country, and weekly booking trends to build effective marketing campaigns and enhance customer service.
*   **Key Visuals:** Age Classification of Passengers, Average Ticket's Price per Country, Percentage of Flight Classes, Number of Flights per Week (Sep, Oct, Nov) in Each Country.
<p align="center">
  <img src="https://github.com/user-attachments/assets/791ee86a-a19c-47e4-b9c4-b22fb2009a04" alt="Customer Analytics Dashboard 1" width="700">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/10e26e36-bf50-4e32-8a9e-c0e81e13e7dd" alt="Customer Analytics Dashboard 2" width="700">
</p>


*   **Key Insight:** Passengers are predominantly in their 20s-30s. Average ticket prices vary significantly by country, with Indonesia being the highest. Business Class is the most preferred. Weekly flight bookings fluctuate, providing customers with information for optimal booking times.

**General Recommendations (Based on aggregated insights):**
*   **Focus on Potential Markets:** The Philippines and Vietnam show positive reception. Maintain growth momentum and explore deeper market penetration.
*   **Strategy for Indonesia:** Due to high competition and lower initial performance, develop distinct marketing and product strategies, possibly focusing on niche routes.
*   **Optimize Class Offerings:** Maintain quality and strongly promote Business Class. Consider special packages for Private Class. Analyze Economy Class pricing for competitiveness.
*   **Enhance Customer Experience:** Personalize offers and services based on age demographics and class preferences.

## Technologies Used
-   **Database Design:** draw.io
-   **RDBMS:** SQL Server
-   **Query Language:** T-SQL (SQL)
-   **Visualization & Web App:** Python (with Streamlit.io)
-   **Other Python Libraries:** Pandas, pyodbc, Matplotlib, Plotly (or Plotly Express)
-   **Secrets Management:** `secrets.toml`

## Setup and Usage Instructions
### Prerequisites
*   SQL Server (compatible version).
*   Python 3.x.
*   Streamlit.
*   Git (for cloning the repository).

### Database Setup
1.  Create a new database in SQL Server (e.g., `SEAAirbusDB`).
2.  Execute the single SQL script `FINAL TEST 18.5.sql` to create tables and insert data.
3.  **Important:** Configure your database connection details (server name, database name, username, password if applicable) in the `secrets.toml` file (or directly in the Python code) to match your SQL Server environment.

### Running the Dashboard Application
1.  **Clone Repository:** `git clone https://github.com/Dung040125/SEA-Airline-Operations-Analytics` and `cd SEA-Airline-Operations-Analytics`.
2.  **(Recommended) Create and Activate a Python Virtual Environment.**
3.  **Install Libraries:**
    ```bash
    pip install streamlit pandas pyodbc matplotlib plotly
    ```
4.  **Run Dashboard:** `python -m streamlit run finalG6.py`
5.  **View Dashboard:** Access the URL (usually `http://localhost:8501`) in your browser.

## Project Deliverables
1.  **Entity Relationship Diagram (ERD)** (appeared above)
2.  **SQL Script:** `FINAL TEST 18.5.sql` [Go to file](https://github.com/Dung040125/SEA-Airline-Operations-Analytics/blob/main/FINAL%20TEST%2018.5.sql).
3.  **Streamlit Dashboard Source Code:** `finalG6.py` [Go to file](https://github.com/Dung040125/SEA-Airline-Operations-Analytics/blob/main/finalG6.py), `secrets.toml`[Go to file](https://github.com/Dung040125/SEA-Airline-Operations-Analytics/blob/main/secrets.toml)
4.  **Project Report (PDF):** Includes full project details.
    *   [Link to Report](https://github.com/Dung040125/SEA-Airline-Operations-Analytics/blob/main/REPORT-5-5.docx)

## Design Discussions and Decisions
Details regarding design choices and interpretation of requirements are documented in the Project Report.
