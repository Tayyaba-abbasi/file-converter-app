# import streamlit as st
# import pandas as pd
# from PIL import Image
# import io
# import docx2pdf
# from pathlib import Path

# # Page configuration
# st.set_page_config(
#     page_title="File Converter App",
#     page_icon="🔄",
#     layout="centered"
# )

# # Custom CSS for styling
# st.markdown("""
# <style>
#     .main {
#         background-color: #f0f8ff;
#     }
#     .stButton>button {
#         background-color: #ff6b6b;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#     }
#     .stButton>button:hover {
#         background-color: #ff5252;
#     }
#     .title {
#         color: #2c3e50;
#         text-align: center;
#     }
# </style>
# """, unsafe_allow_html=True)

# # App title
# st.markdown("<h1 class='title'>📁 File Converter</h1>", unsafe_allow_html=True)
# st.write("✨ Transform your data between CSV & Excel formats with built-in cleaning & visualization!")

# # Supported conversions
# conversion_type = st.selectbox(
#     "Select Conversion Type",
#     ["Excel to CSV", "CSV to Excel"]
# )

# uploaded_file = st.file_uploader("Upload your file", type=None)

# if uploaded_file is not None:
#     # File info section
#     file_size = uploaded_file.size/1024  # Convert to KB
#     st.write(f"📄 File Name: {uploaded_file.name}")
#     st.write(f"📊 File Size: {file_size:.2f} KB")
    
#     try:
#         if conversion_type == "Excel to CSV":
#             if uploaded_file.name.endswith('.xlsx'):
#                 df = pd.read_excel(uploaded_file)
                
#                 # Data Preview
#                 st.subheader("Data Preview")
#                 st.dataframe(df.head())
                
#                 # Data Cleaning Options
#                 st.subheader("Data Cleaning Options")
#                 if st.checkbox("Remove Missing Values"):
#                     df = df.dropna()
#                 if st.checkbox("Remove Duplicates"):
#                     df = df.drop_duplicates()
                
#                 # Column Selection
#                 st.subheader("Select Columns to Keep")
#                 selected_columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
#                 df = df[selected_columns]
                
#                 # Data Visualization
#                 st.subheader("Data Visualization")
#                 if len(df.select_dtypes(include=['float64', 'int64']).columns) > 0:
#                     numeric_column = st.selectbox("Select column for visualization", 
#                                                 df.select_dtypes(include=['float64', 'int64']).columns)
#                     chart_type = st.radio("Select chart type", ["Bar", "Line", "Histogram"])
                    
#                     if chart_type == "Bar":
#                         st.bar_chart(df[numeric_column])
#                     elif chart_type == "Line":
#                         st.line_chart(df[numeric_column])
#                     else:
#                         st.histogram(df[numeric_column])
                
#                 # Download Button
#                 csv = df.to_csv(index=False)
#                 st.download_button(
#                     "Download CSV",
#                     csv,
#                     "converted.csv",
#                     "text/csv",
#                     key='download-csv'
#                 )
                
#         elif conversion_type == "CSV to Excel":
#             if uploaded_file.name.endswith('.csv'):
#                 df = pd.read_csv(uploaded_file)
                
#                 # Data Preview
#                 st.subheader("Data Preview")
#                 st.dataframe(df.head())
                
#                 # Data Cleaning Options
#                 st.subheader("Data Cleaning Options")
#                 if st.checkbox("Remove Missing Values"):
#                     df = df.dropna()
#                 if st.checkbox("Remove Duplicates"):
#                     df = df.drop_duplicates()
                
#                 # Column Selection
#                 st.subheader("Select Columns to Keep")
#                 selected_columns = st.multiselect("Choose columns", df.columns.tolist(), default=df.columns.tolist())
#                 df = df[selected_columns]
                
#                 # Data Visualization
#                 st.subheader("Data Visualization")
#                 if len(df.select_dtypes(include=['float64', 'int64']).columns) > 0:
#                     numeric_column = st.selectbox("Select column for visualization", 
#                                                 df.select_dtypes(include=['float64', 'int64']).columns)
#                     chart_type = st.radio("Select chart type", ["Bar", "Line", "Histogram"])
                    
#                     if chart_type == "Bar":
#                         st.bar_chart(df[numeric_column])
#                     elif chart_type == "Line":
#                         st.line_chart(df[numeric_column])
#                     else:
#                         st.histogram(df[numeric_column])
                
#                 # Download Button
#                 excel_buffer = io.BytesIO()
#                 df.to_excel(excel_buffer, index=False)
#                 st.download_button(
#                     "Download Excel",
#                     excel_buffer.getvalue(),
#                     "converted.xlsx",
#                     "application/vnd.ms-excel",
#                     key='download-excel'
#                 )

#     except Exception as e:
#         st.error(f"Error: {str(e)}")
        
# st.success("✅ All files have been processed successfully! 🎉")


import streamlit as st
import pandas as pd
from PIL import Image
import io
import docx2pdf
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="File Converter App",
    page_icon="🔄",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main {
        background-color: #f0f8ff;
    }
    .stButton>button {
        background-color: #ff6b6b;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ff5252;
    }
    .title {
        color: #2c3e50;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# App title
st.markdown("<h1 class='title'>📁 File Converter 🚀</h1>", unsafe_allow_html=True)
st.write("✨ Transform your data between CSV & Excel formats with built-in cleaning & visualization! 🛠️")

# Supported conversions
conversion_type = st.selectbox(
    "🔄 Select Conversion Type",
    ["Excel to CSV", "CSV to Excel"]
)

uploaded_file = st.file_uploader("📤 Upload your file", type=None)

if uploaded_file is not None:
    # File info section
    file_size = uploaded_file.size/1024  # Convert to KB
    st.write(f"📄 **File Name:** {uploaded_file.name}")
    st.write(f"📊 **File Size:** {file_size:.2f} KB")
    
    try:
        if conversion_type == "Excel to CSV":
            if uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
                
                # Data Preview
                st.subheader("👀 Data Preview")
                st.dataframe(df.head())
                
                # Data Cleaning Options
                st.subheader("🧹 Data Cleaning Options")
                if st.checkbox("🧼 Remove Missing Values"):
                    df = df.dropna()
                if st.checkbox("🗑️ Remove Duplicates"):
                    df = df.drop_duplicates()
                
                # Column Selection
                st.subheader("📌 Select Columns to Keep")
                selected_columns = st.multiselect("🎯 Choose columns", df.columns.tolist(), default=df.columns.tolist())
                df = df[selected_columns]
                
                # Data Visualization
                st.subheader("📊 Data Visualization")
                if len(df.select_dtypes(include=['float64', 'int64']).columns) > 0:
                    numeric_column = st.selectbox("📈 Select column for visualization", 
                                                df.select_dtypes(include=['float64', 'int64']).columns)
                    chart_type = st.radio("📉 Select chart type", ["Bar", "Line", "Histogram"])
                    
                    if chart_type == "Bar":
                        st.bar_chart(df[numeric_column])
                    elif chart_type == "Line":
                        st.line_chart(df[numeric_column])
                    else:
                        import matplotlib.pyplot as plt
                        fig, ax = plt.subplots()
                        ax.hist(df[numeric_column], bins=20, color='skyblue', edgecolor='black')
                        st.pyplot(fig)
                
                # Download Button
                csv = df.to_csv(index=False)
                st.download_button(
                    "📥 Download CSV",
                    csv,
                    "converted.csv",
                    "text/csv",
                    key='download-csv'
                )
                
        elif conversion_type == "CSV to Excel":
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
                
                # Data Preview
                st.subheader("👀 Data Preview")
                st.dataframe(df.head())
                
                # Data Cleaning Options
                st.subheader("🧹 Data Cleaning Options")
                if st.checkbox("🗑️ Remove Duplicates"):
                    duplicates_count = df.duplicated().sum()  # Count duplicate rows
                    if duplicates_count > 0:
                       df = df.drop_duplicates()
                       st.success(f"🎉 {duplicates_count} duplicate rows removed successfully!")
                    else:
                         st.info("✅ No duplicate rows found!")


                
                # Column Selection
                st.subheader("📌 Select Columns to Keep")
                selected_columns = st.multiselect("🎯 Choose columns", df.columns.tolist(), default=df.columns.tolist())
                df = df[selected_columns]
                
                # Data Visualization
                st.subheader("📊 Data Visualization")
                if len(df.select_dtypes(include=['float64', 'int64']).columns) > 0:
                    numeric_column = st.selectbox("📈 Select column for visualization", 
                                                df.select_dtypes(include=['float64', 'int64']).columns)
                    chart_type = st.radio("📉 Select chart type", ["Bar", "Line", "Histogram"])
                    
                    if chart_type == "Bar":
                        st.bar_chart(df[numeric_column])
                    elif chart_type == "Line":
                        st.line_chart(df[numeric_column])
                    else:
                        import matplotlib.pyplot as plt
                        fig, ax = plt.subplots()
                        ax.hist(df[numeric_column], bins=20, color='skyblue', edgecolor='black')
                        st.pyplot(fig)
                
                # Download Button
                excel_buffer = io.BytesIO()
                df.to_excel(excel_buffer, index=False)
                st.download_button(
                    "📥 Download Excel",
                    excel_buffer.getvalue(),
                    "converted.xlsx",
                    "application/vnd.ms-excel",
                    key='download-excel'
                )

    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
        
st.success("✅ All files have been processed successfully! 🎉")
