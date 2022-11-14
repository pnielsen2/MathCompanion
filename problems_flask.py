#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template
import os, random
app = Flask(__name__)

@app.route('/')
def home():    
    file_name = random.choice(os.listdir("templates"))
    return render_template(file_name)
if __name__ == '__main__':
    app.run(port=80)


# In[ ]:




