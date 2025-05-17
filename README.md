
 Mobile Price Prediction

This project is focused on **predicting the price category of mobile phones** (Low, Medium, High, or Very High) based on their specifications using machine learning techniques. The model is trained on a clean dataset and deployed using Gradio for easy interaction. The objective is to assist customers and mobile sellers in making informed decisions by providing accurate price category suggestions.


 Project Objective

To build a machine learning model that classifies a mobile phone into one of four pricing categories using its specifications. This solution can be used in mobile shops or e-commerce platforms to recommend phones based on customer requirements and help in pricing new models based on hardware features.

---

\ Dataset

The dataset used for this project is a public dataset from Kaggle titled **Mobile Price Classification**.

Features:

  * `battery_power`: Total energy capacity of the battery (mAh)
  * `blue`: Bluetooth (1 = Yes, 0 = No)
  * `clock_speed`: Speed at which microprocessor executes instructions (GHz)
  * `dual_sim`: Dual SIM support (1 = Yes, 0 = No)
  * `fc`: Front Camera megapixels
  * `four_g`: 4G support (1 = Yes, 0 = No)
  * `int_memory`: Internal memory (GB)
  * `m_dep`: Mobile depth (cm)
  * `mobile_wt`: Weight of mobile phone (grams)
  * `n_cores`: Number of processor cores
  * `pc`: Primary Camera megapixels
  * `px_height`: Pixel resolution height
  * `px_width`: Pixel resolution width
  * `ram`: RAM capacity (MB)
  * `sc_h`: Screen height (cm)
  * `sc_w`: Screen width (cm)
  * `talk_time`: Battery backup (hours)
  * `three_g`: 3G support (1 = Yes, 0 = No)
  * `touch_screen`: Touchscreen availability (1 = Yes, 0 = No)
  * `wifi`: WiFi support (1 = Yes, 0 = No)

  Target Variable:

  * `price_range`: Categorical variable with values:

    * 0 = Low Cost
    * 1 = Medium Cost
    * 2 = High Cost
    * 3 = Very High Cost



 Algorithms Used

* **Exploratory Data Analysis (EDA):**

  * Checked feature distributions and correlations
  * Identified the most important features



  Model Selection:

  * Evaluated several classification models:

    * Logistic Regression
    * Random Forest
    * Decision Tree
    * Gradient Boosting Classifier ✅ (Best Performance)
    * Support Vector Machines

  Model Evaluation:

  * Metrics Used: Accuracy, Confusion Matrix
  * Gradient Boosting achieved the highest accuracy and was selected for deployment

---

 Deployment

The final model was deployed using **Gradio**, a Python library that allows easy UI creation for ML models.

* 📦 **Gradio Interface**: Allows users to input mobile specs and get a predicted price category
* 🐳 **Docker**: Containerized the application for easy deployment

## 🛠️ Tools & Technologies

* Python
* Pandas, NumPy
* Matplotlib, Seaborn
* Scikit-learn
* Gradio
* Docker

---

 Future Work

* Real-time deployment on cloud (e.g., AWS/GCP)
* Integration into mobile shop CRM software
* Add more features like brand, release year, OS
* Extend the model for regression to predict actual prices instead of price ranges

---



JAY KUNJIR 
MSc Statistics | Data Science Enthusiast


