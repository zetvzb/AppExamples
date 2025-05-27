import streamlit as st 
import pandas as pd 
import numpy as np

st.title('Example Streamlit App')

#Create sample data
data = pd.DataFrame({
    'Day': pd.date_range(start='2025-01-01', periods=10),
    'Value': np.random.randint(10, 100, size=10)
})

# Show data as a table
st.subheader("📊 Data Table")
st.dataframe(data)

# Show line chart
st.subheader("📉 Line Chart")
st.line_chart(data.set_index('Day'))

#To Run This 
#Open bash Terminal 

## streamlit run streamlit_example.py 