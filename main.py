import openai 
import argparse
import PyPDF2

openai.api_key = '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'

def AIreadsThrough(pdf_path):
    with open(pdf_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        full_text = ""
        for page in pdf_reader.pages:

            full_text += page.extract_text() or ""


    if not full_text.strip():
        return "PDF format is invalid. I unfortunatly could't read your PDF :()."

    response  = openai.ChatCompletion.create(model = "gpt-3.5-turbo",
    messages = [
        {
            "role" : "system",
            "content" : "You are a productivity assistant. Extract tasks and generate a 24 hour plan for the next day from the summary."
        },
        {
            "role" : "user",
            "content" : f""" These are notes from work from a PDF. Clearly summarize in paragraph format and sumarize tasks from the PDF and create a detailed 24 hour plan based on those tasks. Include time slots (like 12:00 - 01:00 eat lunch).
                Return in the following format:

                Summary:

                
                Tasks to Do:
                - Task 1
                - Task 2
                - etc.


                24 Hour Plan:
                08:00 - ...
                12:00 - ...


                Notes:
                {full_text} """
        }
    ])

    return response.choices['choices'][0]['message']['content']
