from flask import Flask, render_template, request, url_for, redirect
import os
import logging
from config import Config
from extensions import db
from models import main_start_db