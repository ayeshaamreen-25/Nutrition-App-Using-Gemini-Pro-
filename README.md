# Nutrition App Using Gemini Pro
Welcome to the **Nutrition App**, a personalized guide to healthy eating and well-being powered by **Gemini Pro**. This innovative app provides users with calorie count of their food, tailored nutrition recommendations, and wellness tips to help them achieve a vibrant and fulfilling lifestyle.

## Key Features
- **Calorie Count**: Calorie estimate based on the user input image.
- **Meal Improvement Tips**: Easy-to-follow meal suggestions and tips for maintaining a balanced diet.
- **User Interaction**: A seamless interface for entering nutritional data, goals, and health metrics.
- **Real-time Insights**: Uses Gemini Pro’s pre-trained AI model for accurate food analysis and recommendations.

## How to Run the Project
### Prerequisites
Ensure you have the following installed:
- Python 3.12 or later
- `pip` for Python package management

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/ayeshaamreen-25/Nutrition-App-Using-Gemini-Pro-.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Nutrition-App-Using-Gemini-Pro-
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Get the API Key:
   Visit [Google AI Developer](https://ai.google.dev/) to generate your API key.
   Copy the key for use in the next step.
   
5. Set up the `.env` file for your **Google API key**:
   ```
   GOOGLE_API_KEY=your_google_api_key
   ```

### Launch the Application
1. Start the Streamlit server:
   ```bash
   streamlit run app.py
   ```
2. Open your browser and navigate to:
   `http://localhost:8080`
   
## Project Flow
### 1. User Input
- Users interact with a web or mobile UI to input their food image.
### 2. Data Collection & Transmission
- Inputs are securely transmitted using the Google API key.
### 3. API Interaction with Gemini Pro
- Data is sent to the Gemini Pro pre-trained model for analysis.
### 4. Output Generation
- The model processes data and provides personalized nutrition recommendations.

## Output Screenshots
![Screenshot (3)](https://github.com/user-attachments/assets/9d935647-7622-44d3-8bcf-7461a0d371a8)

![Screenshot (4)](https://github.com/user-attachments/assets/ca993711-64f9-46c8-a018-315e5335165f)




