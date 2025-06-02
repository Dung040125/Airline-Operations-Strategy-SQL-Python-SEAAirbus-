# 📊 Airline Operations Strategy (SQL + Python – SEAAirbus) ✈️

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

This project focuses on designing and implementing a **foundational data system** and **analytical dashboards** for **SEAAirbus**, a new premium airline targeting key destinations in **Southeast Asia**. As per the project brief, SEAAirbus aims to initially operate between **two main cities from each of three distinct countries: Vietnam, Philippines, and Indonesia**. The primary goal is to equip SEAAirbus with tools for efficient **operational planning** and **strategic decision-making** from its inception.

The project aims to answer critical **business questions** for different stakeholders:
1.  How is our airline performing in specific countries (**Vietnam, Philippines, Indonesia**) regarding **booked flights**, **revenue growth**, **profitability**, and **cost structures**?
2.  What is the **overall business performance**, **service class performance**, and **most popular/profitable routes**?
3.  What are **passenger demographics**, **class preferences**, **average ticket prices**, and **booking trends**?

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

### Visual Summary 1: Local CEO Insights
*   **Objective:** Provide Local CEOs (Vietnam, Philippines, Indonesia) with an overview of their respective national operational performance (booked flights, revenue growth, profit, cost structure) to guide market-specific development.
*   **SQL/Python Techniques:** Aggregation of booking and financial data by country and office; time-series analysis for revenue growth; percentage calculations for profit distribution.
*   **Result Snapshot:**
    <p align="center">
      <img src="https://github.com/user-attachments/assets/7da3916e-116b-4cbc-aeef-beb3aa3f342c" alt="Local CEO Dashboard" width="700">
    </p>
### Key Findings:
*   **Overall Market Snapshot:** Performance varies significantly across the three key Southeast Asian markets.
    *   **Philippines:** Leads impressively in **booked flights** (~140) and dominates **profit share** (43.7%), indicating strong market demand and effective profit conversion. While having the highest revenue and operating costs, it maintains a healthy profit margin.
        *   *Focus: Maintain momentum, explore cost optimization.*
    *   **Vietnam:** A strong competitor with high **booked flights** (~130) and substantial **profit contribution** (36.8%). Shows a good balance between revenue generation and operating costs.
        *   *Focus: Enhance profit margins through cost improvements or strategic pricing.*
    *   **Indonesia:** Shows the lowest **booked flights** (~40) and **profit share** (19.5%). Both revenue and costs are lower, but profit margins appear tighter, signaling a need for strategic intervention to unlock potential.
        *   *Focus: Develop breakthrough strategies to improve market share and profitability.*

    **Performance by Service Class & Revenue Growth (Insights from Revenue Growth Rate chart):**
    *   **Private Class:** Exhibits high volatility but offers significant **revenue growth** potential in specific offices (e.g., HNOBO, QZOBO), suggesting it's driven by high-value, less frequent bookings.
    *   **Business Class:** Provides a more stable and significant revenue stream, particularly strong in offices like QZOBO, indicating consistent demand.
    *   **Economy Class:** Delivers consistent, albeit lower, revenue across offices.
    *   *Implication:* Performance varies by office and class, requiring Local CEOs to tailor strategies. Focus on stable high-margin classes while managing volatile ones and optimizing consistent contributors.

    **Cost Structures & Profitability:**
    *   The relationship between **revenue** and **operating costs** by country directly impacts overall **profitability**. Philippines and Vietnam demonstrate better margins than Indonesia, where the gap is visually smaller. This underscores the need to analyze and manage **cost structures** effectively in each market, especially Indonesia.


### Visual Summary 2: CEO Overview
*   **Objective:** Offer the Global CEO a holistic view of business operations, class performance, popular destinations, and overall profitability/revenue to support high-level strategic decisions.
*   **SQL/Python Techniques:** Aggregation by class type, destination, and country; trend analysis for profits; revenue segmentation by ticket type.
*   **Result Snapshot:**
    <p align="center">
      <img src="https://github.com/user-attachments/assets/d1dfd970-d896-4679-b36c-8860d962c1af" alt="CEO Overview Dashboard" width="700">
    </p>
### Key Findings:
*   **Ticket Class: Volume vs. Revenue**
    *   **Booking Volume:** **Business Class** (~170+) and **Economy Class** (~140+) bookings dominate, indicating popular choices. **Private Class** has very few bookings.
    *   **Revenue:** Conversely, **Private Class** contributes outstanding revenue (over 1M units), significantly higher than Business Class (~0.2M) and Economy Class.
    *   *Strategy:* Focus on the high value of Private Class despite low volume, while optimizing profitability from Business and Economy for cash flow.

    **Destinations & Route Network**
    *   **Most Popular:** **Manila (25.5%)**, **Hanoi (22.0%)**, **Ho Chi Minh City (20.4%)**, and **Quezon (18.9%)** are key destinations, accounting for the majority of flights.
    *   **Less Popular:** **Jakarta (7.9%)** and **Surabaya (5.3%)** have lower shares, requiring re-evaluation or enhanced marketing.
    *   *Strategy:* Strengthen core markets, consider strategies for less popular destinations.

    **Profits by Country**
    *   **Philippines:** Leads in profit (over 0.5M), but shows signs of plateauing/slight decline.
    *   **Vietnam:** Stable profits, lower than the Philippines, with growth potential.
    *   **Indonesia:** Lowest profits, needs clear improvement strategies.
    *   *Strategy:* Maintain strong markets (Philippines), drive growth (Vietnam), and improve performance (Indonesia).


### Visual Summary 3: Customer Analytics
*   **Objective:** Help Marketing and Customer Service understand passenger demographics (age), class preferences, average ticket prices by country, and weekly booking trends to build effective marketing campaigns and enhance customer service.
*   **SQL/Python Techniques:** Passenger data aggregation by age groups; calculation of average ticket prices per country; percentage distribution of flight classes; weekly trend analysis of flight bookings.
*   **Result Snapshot:**
    <p align="center">
      <img src="https://github.com/user-attachments/assets/791ee86a-a19c-47e4-b9c4-b22fb2009a04" alt="Customer Analytics Dashboard 1" width="700">
    </p>
    <p align="center">
      <img src="https://github.com/user-attachments/assets/10e26e36-bf50-4e32-8a9e-c0e81e13e7dd" alt="Customer Analytics Dashboard 2" width="700">
    </p>
### Key Findings:
    **1. SEAAirbus Customer Profile: Young, Prefers Premium, and Willing to Pay.**
    *   Passengers are predominantly in the **21-30** and **31-40** age groups, suggesting a core of young, dynamic professionals or entrepreneurs.
    *   The preference for **Business Class** (54.1% share) reflects a demand for comfortable, premium flight experiences, affirming SEAAirbus's positioning.
    *   *Narrative & Implication:* SEAAirbus is successfully attracting its target demographic – young, successful individuals willing to pay for quality. Marketing should focus on engaging this "golden customer" segment with tailored messaging and channels, emphasizing the premium experience.

    **2. Ticket Prices by Country: Indonesia Leads, but Deeper Analysis Needed.**
    *   **Indonesia** has the highest average ticket price (>2200), significantly more than the **Philippines** (~1600) and **Vietnam** (~1300).
    *   This high price could be due to longer routes, a higher proportion of premium class bookings, or a specific pricing strategy. However, when combined with low profit information for Indonesia (from CEO Overview), this suggests a need for deeper analysis of operating costs or the actual revenue structure there.
    *   *Narrative & Implication:* High ticket prices don't always equal high profits. Understanding cost structures and the actual contribution of each ticket segment in Indonesia is crucial. Other markets might compensate for lower ticket prices with higher volume or cost efficiency.

    **3. Weekly Booking Trends: Understanding the Market "Rhythm".**
    *   Weekly flight numbers fluctuate significantly by country and month (Sept, Oct, Nov), indicating seasonality and local influencing factors.
    *   For example, the Philippines might see higher demand mid-September to October, while Vietnam experiences a surge in late November. Indonesia generally maintains lower, less volatile levels.
    *   *Narrative & Implication:* Understanding this "rhythm" allows SEAAirbus to flexibly adjust flight schedules, allocate resources, and implement timely marketing/promotional campaigns to optimize revenue and meet specific market demands.

---

## 🔎 Final Conclusion & Recommendations
👉🏻 Based on the aggregated insights from the dashboards, SEAAirbus should consider the following strategic directions to optimize its initial operations and drive growth:

📌 **Key Takeaways & Recommendations:**
1.  **Smart Market Prioritization:**
    *   Prioritize resources for high-performing markets like the **Philippines** and **Vietnam**.
    *   Develop a distinct, breakthrough strategy to unlock **Indonesia's** potential, focusing on cost optimization and demand stimulation.

2.  **Optimized Service Class Experience:**
    *   Maximize value from **Private Class** with exclusive offerings.
    *   Reinforce **Business Class** as the top choice for young, successful professionals.
    *   Ensure the competitiveness and efficiency of **Economy Class** for a stable passenger flow.

3.  **Agile Marketing & Demand Management:**
    *   Target marketing efforts towards the **21-40 age demographic**, emphasizing premium experiences.
    *   Leverage **weekly booking trend** data for dynamic scheduling, pricing, and promotions, especially for **key routes** (Manila, Hanoi, HCMC).

4.  **Cultivate Data-Driven Decision-Making:**
    *   Encourage data utilization across all operational and business decisions.
    *   Continuously refine analytical systems and track **KPIs** for ongoing optimization.

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
