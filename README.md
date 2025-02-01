Crop Suitability Prediction System
📌 Project Overview

The Crop Suitability Prediction System is a machine learning-powered application that helps farmers and agricultural stakeholders determine the best crops to cultivate based on soil and climate conditions. This system leverages advanced classification models, including Random Forest, XGBoost, LightGBM, and CatBoost, to provide accurate recommendations.

🚀 Features

Predict suitable crops based on input soil and climate conditions.

Provides top 3 crop recommendations with probability scores.

Interactive visualizations using Plotly for better insights.

Web-based interface built with Streamlit.

📂 Dataset Overview

The dataset includes the following features:

Soil Properties: Nitrogen (N), Phosphorus (P), Potassium (K), pH.

Climate Factors: Temperature, Humidity, Rainfall.

Crop Labels: 22 different crop types, label-encoded.

🛠️ Technologies Used

Programming Language: Python

Machine Learning Libraries: Scikit-learn, XGBoost, LightGBM, CatBoost

Data Manipulation: Pandas, NumPy

Visualization: Matplotlib, Seaborn, Plotly

Web Framework: Streamlit

Deployment: Streamlit Cloud

📌 Installation Guide

1️⃣ Clone the Repository

git clone https://github.com/yourusername/crop-suitability-prediction.git
cd crop-suitability-prediction

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run the Streamlit App

streamlit run crop_suitability_prediction_system.py

🎯 How to Use

Input soil and climate parameters in the sidebar.

Click "Predict Crop" to get recommendations.

View top 3 recommended crops and their suitability scores.


🛠️ Model Training & Saving

If retraining is needed, run:

notebook.ipynb

This will save the trained model as crop_suitability_model.pkl.

🌍 Deployment

For deployment on Streamlit Cloud, AWS, or Heroku, ensure:

requirements.txt includes all dependencies.

The model (.pkl file) is accessible in the cloud environment.

📝 Future Enhancements

📡 Real-time sensor data integration for more dynamic predictions.

📱 Mobile-friendly interface for easier farmer access.

🌎 Expand dataset to include more diverse regions.

📊 Advanced analytics on crop performance over time.

🤝 Contributing

Contributions are welcome! Feel free to fork the repo, create a new branch, and submit a pull request.

📜 License

This project is licensed under the MIT License.

📞 Contact

For any inquiries, reach out via:
📧 Email: inioluwaadisa@gmail.com

🌱 Empowering Agriculture with Data Science! 🚀

