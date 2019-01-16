import shutil
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import codecs
import csv
import sqlite3

shutil.move("Merged/Hello.txt","Locale/Location/Hello.txt")
