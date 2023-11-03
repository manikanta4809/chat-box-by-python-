!pip install openai
import os
import openai
import tkinter as tk
# Define a function to be called when the button is pressed
def generate_output():
    prompt = input_entry.get()
    openai.api_key = '***************************************************'
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt}
        ]
    )
    
    # Extract the response text
    response_text = response.choices[0].message.content
    output_text = f"{response_text}" # Generate output text based on the input
    output_label.config(text=output_text) # Update the output label with the generated text

# Create a tkinter window
root = tk.Tk()
root.geometry('10000x10000')
root.title("Ask_Me_Anything")

# Create an entry widget for the user's input
input_label = tk.Label(root,text="Ask any question",font=("Arial", 20))
input_label.pack()

input_entry = tk.Entry(root,width=100,font=("arial",15))
input_entry.pack()


# Create a button to generate output when pressed
generate_button = tk.Button(root, text="Generate Output", command=generate_output,font=("Arial", 15),background="red")
generate_button.pack()

# Create a label to display the generated output
output_label = tk.Label(root, text="",font=("Arial", 15), background="yellow")
output_label.pack()

# Start the tkinter event loop
root.mainloop()
