""" Entry point of the sim-search package """

import os
import logging
from dotenv import load_dotenv

load_dotenv()

JINA_API_KEY = os.getenv("JINA_API_KEY")
