from flask import render_template, request, session
import requests
import re
import os
import io
from flask import render_template, request, session, flash
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
import numpy as np
from config import basedir, DEVICE
from app.inference import bp
import random
from multiprocessing import Pool

@bp.route('/inference', methods=['POST'])
def generate_image():
    query = request.form['query'].lower()
    user = session['username']
    model = request.form['model']
    model_path = basedir + f"/model_artifacts/{model}"
    print(model_path)
    with open(basedir+'/app/static/queries/queries.txt', 'a') as f:
        f.write(query)
        f.write('\n')

    
    print(f"user: {user}, model: {model}, query: {query}")
    if not query:
        flash("Please enter a prompt", "inval")

    currentModelPipe = StableDiffusionPipeline.from_pretrained(model_path, ignore_mismatched_sizes=True).to(DEVICE)
    image_urls = []
    for i in range(4):
        result_image = currentModelPipe(prompt=query, num_inference_steps=200).images[0]
        image_name = f"image_{random.randint(1, 1000000)}"
        result_image.save(basedir + f"/app/static/userimages/{image_name}.png")
        imageurl = os.environ.get("CLOUD_URL") + f"/static/userimages/{image_name}.png"
        image_urls.append(image_name)

    return render_template('inference.html', view_type='finetuned', query=query, model=model, image_urls=image_urls) 
    
    



