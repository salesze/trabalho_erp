from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

engine = create_engine("mysql+pymysql://root:Joao10203030!@localhost/erp_estoque")