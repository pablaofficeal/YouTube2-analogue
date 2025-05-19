from flask import Flask, render_template, request, url_for, redirect
from config import Config
import os
import logging
from extensions import db
from models import main_start_db