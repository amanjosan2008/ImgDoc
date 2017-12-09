#!/usr/bin/env python3

from tkinter import *
from tkinter import filedialog
import sys, glob, os, re
import tarfile
import imghdr, shutil
import subprocess
from pathlib import Path
from collections import Counter
from PIL import Image
from itertools import islice
from hashlib import md5
import imagehash
