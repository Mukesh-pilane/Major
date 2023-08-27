from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("lidiya/bart-large-xsum-samsum")

model = AutoModelForSeq2SeqLM.from_pretrained("lidiya/bart-large-xsum-samsum")
print(model('''We completed our research and development/pilot phase of the project with the first 40 test stories recorded. And this is where our journey took a diversion, as the spectacular psychedelic Sgt Peppers Gypsy Showman’s Caravan crossed out path. We had to pause the Bedtime Stories project in order to welcome in and develop the Peacing Together project. What we hadn’t known at the outset was that the caravan’s journey would take us back to the childhood dreams and sanctuary of the world’s greatest icons and greatest dreamers. One of John’s favourite childhood stories was Wind in the Willows. To us it was a magical discovery and insight to the caravan. John had said in an interview that he would have liked to, in later life, write stories for children. Sadly that dream was taken from him, but his caravan lives on and once the restoration is complete we hope that it will become the totem for the dream of delighting young souls.'''))