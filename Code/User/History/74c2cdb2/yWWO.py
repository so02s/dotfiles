from flask import Flask, render_template, request
import requests
from decouple import config

api_url = "https://api.example.com/data"