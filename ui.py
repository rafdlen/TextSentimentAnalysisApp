from tkinter import *
from sentiment_model import analyze
import webbrowser


def analyze_sentiment():
    text = text_to_analyze.get("1.0", "end-1c")  # Get the entered text from the widget
    result = analyze(text)  # Call the analyze function

    if result[0]['label'] == "POS":
        sentiment = "positive"
    elif result[0]['label'] == "NEG":
        sentiment = "negative"
    else:
        sentiment = "neutral"

    analysis_result_var.set("The sentiment of your text is: " + sentiment.upper())


def give_score():
    text = text_to_analyze.get("1.0", "end-1c")  # Get the entered text from the widget
    result = analyze(text)  # Call the analyze function
    score = round(result[0]['score'], 2) * 100

    score_result.set(f"The % score for your text is: {score}")

def open_diy_url():
    url = "https://huggingface.co/huggingface"  # Replace this with the desired URL
    webbrowser.open(url)

window = Tk()
window.geometry("800x600")
window.title("Text Sentiment Analysis App")

explanation_var = StringVar()
explanation_label = Label(window, textvariable=explanation_var)
explanation_var.set('''
Sentiment analysis, also known as opinion mining, is a natural language processing (NLP) technique used to determine the sentiment or emotional tone expressed 
in a piece of text. It involves analyzing the language used in the text to identify whether the sentiment conveyed is positive, negative, neutral.
                    ''')
explanation_label.pack(padx=15, pady=10, side=TOP, anchor="w")

label_var = StringVar()
text_to_analyze_label = Label(window, textvariable=label_var)
label_var.set("Enter the text for sentiment analysis:")
text_to_analyze_label.pack(padx=15, pady=10, side=TOP, anchor="w")

text_to_analyze = Text(window, height=10, width=200)
text_to_analyze.pack(padx=15)

analyze_button = Button(window, text="Analyze sentiment", width=15, command=analyze_sentiment)
analyze_button.pack(padx=15, pady=10, side=TOP, anchor="e")

heuristic_2 = StringVar()
heuristic_2_label = Label(window, textvariable=heuristic_2)
heuristic_2.set("**IMPORTANT: Clicking the button triggers a call to the external API, and the response time may vary depending on the API's current load and network conditions.**")
heuristic_2_label.pack(padx=0, pady=0, side=TOP, anchor="e")

label_var_1 = StringVar()
text_translated_label = Label(window, textvariable=label_var_1)
label_var_1.set("Your text translated to English:")
text_translated_label.pack(padx=15, pady=10, side=TOP, anchor="w")

# to be removed when microservice will be developed
temp_1 = StringVar()
temp_label = Label(window, textvariable=temp_1)
temp_1.set("Translated text will apear here when microservice will be available.")
temp_label.pack(padx=15, pady=10, side=TOP, anchor="w")

analysis_result_var = StringVar()
analysis_result_label = Label(window, textvariable=analysis_result_var)
analysis_result_var.set("The sentiment of your text is: ")
analysis_result_label.pack(padx=15, pady=10, side=TOP, anchor="w")

results_var = StringVar()
result_label = Label(window, textvariable=results_var)
result_label.pack()

score_button = Button(window, text="Give sentiment score", width=15, command=give_score)
score_button.pack(padx=15, pady=10, side=TOP, anchor="w")

score_result = StringVar()
score_result_label = Label(window, textvariable=score_result)
score_result.set("The % score for your text is: ")
score_result_label.pack(padx=15, pady=10, side=TOP, anchor="w")

advanced_string = StringVar()
advanced_label = Label(window, textvariable=advanced_string)
advanced_string.set("This app utilizes teh sentiment analysis model provided by Hugging Face. Click the button below for more advanced options: ")
advanced_label.pack(side=TOP, anchor="w")

diy_button = Button(window, text="Advanced options: Go to Hugging Face", width=25, command=open_diy_url)
diy_button.pack(side=TOP, anchor="w")

window.mainloop()
