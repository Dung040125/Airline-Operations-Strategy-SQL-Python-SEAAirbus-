# 📊 **Project Title:** Airline Operations Strategy (SQL + Python – SEAAirbus) ✈️

![alt text](https://github.com/user-attachments/assets/9e84b890-db5a-4a60-9a10-0ae780b2a142)

* **Author:** Nguyen Thi Thuy Dung
* **Date:** 2024-05 
* **Tools Used:** SQL (SQL Server), Python (Streamlit, Pandas, pyodbc, Matplotlib, Plotly), draw.io 
---

## 📑 Table of Contents
- [📌 Background & Overview](#-background--overview)
- [📂 Dataset Description & Data Structure](#-dataset-description--data-structure)
- [⚒️ Main Process: Database Design, Implementation & Dashboard Development](#️-main-process-database-design-implementation--dashboard-development) 
- [🔎 Final Conclusion & Recommendations](#-final-conclusion--recommendations)
- [🚀 Setup and Usage Instructions](#-setup-and-usage-instructions-)
- [📂 Project Deliverables](#-project-deliverables)
- [💡 Design Discussions and Decisions](#-design-discussions-and-decisions) 

---

## 📌 Background & Overview

### Objective
📖 **What is this project about? What Business Question will it solve?**

This project focuses on designing and implementing a foundational data system and analytical dashboards for SEAAirbus, a new premium airline targeting key destinations in Southeast Asia (Vietnam, Philippines, Indonesia). The primary goal is to equip SEAAirbus with tools for efficient operational planning and strategic decision-making from its inception.

The project aims to answer critical business questions for different stakeholders:
*   How is our airline performing in specific countries (Vietnam, Philippines, Indonesia) regarding booked flights, revenue growth, profitability, and cost structures?
*   What is the overall business performance, service class performance, and most popular/profitable routes?
*   What are passenger demographics, class preferences, average ticket prices, and booking trends?

👤 **Who is this project for?**
*   Airline Management (CEOs, Regional Managers)
*   Operations Planners & Marketing Teams
*   Data Analysts & Business Intelligence Professionals.

---

## 📂 Dataset Description & Data Structure

📌 **Data Source**
*   **Source:** Custom-designed SQL Server database with fake data simulating SEAAirbus operations.
*   **Scope:** Covers flights, passengers, bookings, tickets, aircraft, airports, class types, fares, and booking offices.
*   **Format:** SQL Server Database.

📊 **Data Structure & Relationships**
*   **Key Entities/Tables:** `AIRPLANE`, `FLIGHT`, `AIRPORT`, `CABIN_CREW`, `TICKET`, `BOOKING_OFFICE`, `PASSENGERS_A` (Adults), `PASSENGERS_C` (Children), `CLASS_TYPE`, `FARE`.
*   **Entity Relationship Diagram (ERD):**
    <p align="center">
      <img src="https://github.com/user-attachments/assets/52a1eda8-b5a7-4252-bf51-307e32da9ebd" alt="ER Diagram for SEAAirbus" width="700">
    </p>
*   **Schema Snapshot:**
    <p align="center">
      <img src="https://github.com/user-attachments/assets/e9fe75b7-bd24-40e0-a9fd-d27f62cb6b99" alt="Database Schema Snapshot" width="700">
    </p>
    *(Detailed column definitions, data types, and constraints are specified in the `FINAL TEST 18.5.sql` script.)*

---

## ⚒️ Main Process: Database Design, Implementation & Dashboard Development

This project involved a comprehensive workflow from database conceptualization to interactive dashboard delivery.

### 1️⃣ Database Design & Implementation (SQL Server)
*   **Conceptual Design:** Developed an Entity Relationship Diagram (ERD) using **draw.io** to model core airline operations, ensuring fulfillment of project requirements (e.g., at least 5 entities, 4 relationships, 7 tables).
*   **Logical & Physical Design:** Translated the ERD into a relational schema in SQL Server.
*   **Implementation:** Utilized a single T-SQL script (`FINAL TEST 18.5.sql`) to:
    *   `CREATE` tables with appropriate data types.
    *   Define integrity constraints: Primary Keys (PK), Foreign Keys (FK), `UNIQUE`, `NOT NULL`.
    *   Populate the database with sufficient and diverse fake data using `INSERT INTO` statements to enable meaningful analysis.

### 2️⃣ Dashboard Development (SQL & Python with Streamlit)
Three distinct interactive dashboards were developed using Python (Streamlit) to query (via SQL) and visualize data from the SQL Server database. Each dashboard was tailored for a specific user role and analytical purpose, leveraging SQL techniques like `GROUP BY`, `ORDER BY`, `JOIN`, and subqueries.

**Task/Dashboard 1: Local CEO Insights**
*   **Objective:** Provide Local CEOs (Vietnam, Philippines, Indonesia) with an overview of their respective national operational performance (booked flights, revenue growth, profit, cost structure) to guide market-specific development.
*   **SQL/Python Techniques:** Aggregation of booking and financial data by country and office; time-series analysis for revenue growth; percentage calculations for profit distribution.
*   **Result Snapshot:**
    <p align="center">
      <img src="https://github.com/user-attachments/assets/7da3916e-116b-4cbc-aeef-beb3aa3f342c" alt="Local CEO Dashboard" width="700">
    </p>
*   **Key Findings:** The Philippines leads in bookings and profit, indicating strong potential. Indonesia shows lower booking figures and revenue despite operational costs being covered by revenue, suggesting a need for targeted strategies. Vietnam demonstrates operational stability.

**Task/Dashboard 2: CEO Overview**
*   **Objective:** Offer the Global CEO a holistic view of business operations, class performance, popular destinations, and overall profitability/revenue to support high-level strategic decisions.
*   **SQL/Python Techniques:** Aggregation by class type, destination, and country; trend analysis for profits; revenue segmentation by ticket type.
*   **Result Snapshot:**
    <p align="center">
      <img src="https://github.com/user-attachments/assets/d1dfd970-d896-4679-b36c-8860d962c1af" alt="CEO Overview Dashboard" width="700">
    </p>
*   **Key Findings:** Business Class is most popular, aligning with the premium airline positioning. Private Class, despite fewer tickets, generates the highest revenue due to its high value. The Philippines is the most profitable market. Manila is the top booked route. The Indonesian market presents competitive challenges.

**Task/Dashboard 3: Customer Analytics**
*   **Objective:** Help Marketing and Customer Service understand passenger demographics (age), class preferences, average ticket prices by country, and weekly booking trends to build effective marketing campaigns and enhance customer service.
*   **SQL/Python Techniques:** Passenger data aggregation by age groups; calculation of average ticket prices per country; percentage distribution of flight classes; weekly trend analysis of flight bookings.
*   **Result Snapshot:**
    <p align="center">
      <img src="https://github.com/user-attachments/assets/791ee86a-a19c-47e4-b9c4-b22fb2009a04" alt="Customer Analytics Dashboard 1" width="700">
    </p>
    <p align="center">
      <img src="https://github.com/user-attachments/assets/10e26e36-bf50-4e32-8a9e-c0e81e13e7dd" alt="Customer Analytics Dashboard 2" width="700">
    </p>
*   **Key Findings:** Passengers are predominantly in their 20s-30s. Average ticket prices vary significantly by country, with Indonesia being the highest. Business Class is the most preferred. Weekly flight bookings fluctuate, providing customers with information for optimal booking times.

---

## 🔎 Final Conclusion & Recommendations
👉🏻 Based on the aggregated insights from the dashboards, SEAAirbus should consider the following strategic directions to optimize its initial operations and drive growth:

📌 **Key Takeaways & Recommendations:**
*   ✔️ **Targeted Market Strategies:** Develop distinct approaches for promising markets like the Philippines and Vietnam (focus on growth and service enhancement) versus more competitive markets like Indonesia (focus on brand building and niche offerings).
*   ✔️ **Service Class Optimization:** Leverage the popularity and profitability of Business Class. Explore strategies to increase the appeal and booking volume of Private Class. Analyze Economy Class pricing against competitors to ensure value for a premium airline.
*   ✔️ **Data-Driven Customer Engagement:** Utilize insights on passenger demographics (e.g., 20-30 age group) and preferences (e.g., Business Class) to tailor marketing campaigns, loyalty programs, and onboard services.
*   ✔️ **Operational Efficiency:** Continuously monitor booking trends, revenue, and cost metrics via the dashboards to make agile adjustments to flight schedules, pricing, and resource allocation.

---

## 🚀 Setup and Usage Instructions

### Prerequisites
*   SQL Server (compatible version).
*   Python 3.x.
*   Streamlit.
*   Git.

### Setup Steps
1.  **Clone Repository:** `git clone https://github.com/Dung040125/SEA-Airline-Operations-Analytics` and `cd SEA-Airline-Operations-Analytics`.
2.  **Database Setup:**
    *   Create a new database in SQL Server (e.g., `SEAAirbusDB`).
    *   Execute the single SQL script `FINAL TEST 18.5.sql` to create tables and insert data.
3.  **Configure Database Connection:**
    *   This project requires a `secrets.toml` file in the project's root directory to store your SQL Server database credentials. **This file should not be committed to Git.**
    *   Create the `secrets.toml` file locally with the following structure, replacing placeholder values with your actual credentials:
        ```toml
        # Content for your local secrets.toml
        server = "YOUR_SERVER_NAME\\YOUR_INSTANCE_NAME" 
        database = "YOUR_DATABASE_NAME"                 
        username = "YOUR_USERNAME"                      
        password = "YOUR_PASSWORD"                      
        ```
4.  **(Recommended) Create and Activate a Python Virtual Environment.**
5.  **Install Libraries:**
    ```bash
    pip install streamlit pandas pyodbc matplotlib plotly
    ```
6.  **Run Dashboard:** `python -m streamlit run finalG6.py`
7.  **View Dashboard:** Access the URL (usually `http://localhost:8501`) in your browser.

---
## 📂 Project Deliverables
1.  **Entity Relationship Diagram (ERD)** (as shown above).
2.  **SQL Script:** [`FINAL TEST 18.5.sql`](https://github.com/Dung040125/SEA-Airline-Operations-Analytics/blob/main/FINAL%20TEST%2018.5.sql).
3.  **Streamlit Dashboard Source Code:** [`finalG6.py`](https://github.com/Dung040125/SEA-Airline-Operations-Analytics/blob/main/finalG6.py).
    *(Note: The `secrets.toml` file for database credentials must be created locally by the user as per setup instructions and should be added to `.gitignore`.)*
4.  **Project Report (PDF):** Includes full project details, design rationale, and in-depth analysis.
    *   [Link to Report](https://github.com/Dung040125/SEA-Airline-Operations-Analytics/blob/main/REPORT-5-5.docx)

---
## 💡 Design Discussions and Decisions
Key design choices and interpretations of the open-ended requirements were made to best serve SEAAirbus's initial operational needs. These include:
*   **Entity Selection & Granularity:** Focused on core operational entities (Flights, Bookings, Passengers, etc.) and attributes essential for initial analysis, balancing detail with manageability for a new airline.
*   **Relationship Definitions:** Established logical relationships (e.g., one-to-many, many-to-many with junction tables implicit in the design) with appropriate integrity constraints to ensure data consistency.
*   **Dashboard Tailoring:** Designed three distinct dashboards, each addressing the specific analytical needs and perspectives of target stakeholders (Local CEOs, Global CEO, and Customer-facing teams), ensuring each dashboard had at least four meaningful data inputs/visualizations.
*   **Freedom of Interpretation:** Leveraged the allowance for free interpretation of unspecified client requirements to create a practical and logical data model and set of analytical tools. For instance, defining specific KPIs for each dashboard based on assumed business priorities.

Further details on the rationale behind specific schema designs, data generation strategies, and dashboard feature selections are documented comprehensively in the [Project Report](https://github.com/Dung040125/SEA-Airline-Operations-Analytics/blob/main/REPORT-5-5.docx).
