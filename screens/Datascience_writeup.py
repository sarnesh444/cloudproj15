import streamlit as st

def l5():
    st.write("""Retail Question:  What categories are growing or shrinking with changing customer engagement?
            
            Data science Lifecycle
            
                1. Data Pre-Processing - The real-world data has issues, since the model is only as good as the data we feed into it, it is quite important to pre-process the data so that we handle missing values, normalize the data.
                2. Feature Engineering - Curse of dimensionality, so therefore we should normalize and pick only important features.
                3. Model - Building the model using techniques depending on the type of dataset eg. classification, time-series
                4. Model evalution - Determine the accuracy of model using technqiues like F-score
                5. Deployment - deploy the model for prediction on test data
                6. Re-train - retrain the model using latest data
            ---------------------------------------------------------------------------------------------------------------------------------    
            A. Time-series forecast
            
            A time series is a sequence taken at successive equally spaced points in time.
            Moving Averages model to determine the values of a future period using the pattern observed from the previous period.
            
            Model : Moving Averages
            
            Tracking the customer behaviour seasonally we can automate the inventory management and thereby improving the customer experience.
            ---------------------------------------------------------------------------------------------------------------------------------
            B. Clustering
            
            We can segment/cluster the customers based on spending behavior and push tailored notifications based on target market.
            
            Model: K Nearest Neighbors
            ---------------------------------------------------------------------------------------------------------------------------------
            C. Association Rule Mining
            
            We can provide better basket recommendations looking the items frequently purchased together.
            Eg. In a retail scenario we can place the items next to each other so that we can influence the spending behavior.
            
            Model:Apriori
            ---------------------------------------------------------------------------------------------------------------------------------
            """)