from flask import render_template, request, session
import requests
import re
import os
import io
from flask import render_template, request, session, flash
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
import numpy as np
from config import basedir

from app.inference import bp

MODELS_TO_RUN = { 'juan': ['/v1.5-2500/', '/something_else']}


@bp.route('/inference', methods=['POST'])
def generate_image():
    query = request.form['query'].lower()
    user = session['username']

    if not query:
        flash("Please enter a prompt", "inval")

    



    return render_template('inference.html', view_type='finetuned', query=query, user=user) 
    
    



