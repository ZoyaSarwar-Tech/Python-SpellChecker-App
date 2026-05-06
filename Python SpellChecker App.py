import tkinter as tk
from textblob import TextBlob

def check_spelling():
    word=entry.get()

    blob=TextBlob(word)
    corrected=blob.correct()
    if word==str(corrected):
        result_label.config(text="Correct Spelling")
    else:
        result_label.config(text=f"Wrong! Did you mean {corrected}?")
root = tk.Tk()
root.title("Spell Checker")
root.geometry("600x400")
title = tk.Label(root,text="Spell Checker",font=("Arial",20))
title.pack(pady=10)
entry = tk.Entry(root,font=("Arial",20))
entry.pack(pady=10)
btn=tk.Button(root,text="Check Spelling",command=check_spelling)
btn.pack(pady=10)
result_label=tk.Label(root,font=("Arial",20))
result_label.pack(pady=10)
root.mainloop()