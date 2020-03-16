import base64
imgdata = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAMgAAADICAIAAAAiOjnJAAAABmJLR0QA/wD/AP+gvaeTAAAE/klEQVR4nO3dwXLbNhSG0brT93/ldJcFx2EFAh/ApOcsY4mk4n8wMHRx8fXjx4+/YLW/Tz8AfybBIiFYJASLhGCRECwS/3z7r19fX3tuf1nsGLrvzELJ5UYzjzHk/kZDP7136jf4kxGLhGCRECwSgkXi+8n7xcLvE2cmlTMz3xkzc+qFjzEzl9//GzRikRAsEoJFQrBIfDR5v9i2Pj40H595qm3vnXFqXf7Zb9CIRUKwSAgWCcEi8WTy3hmaFw8tec+sU2+71KlinoIRi4RgkRAsEoJF4l2T93sLZ81DL76/b9ejYOaPhuOMWCQEi4RgkRAsEk8m76emq129/G8xTZ75HmLmxc8YsUgIFgnBIiFYJD6avL+zYGNbRcrCK5+qotn/GzRikRAsEoJFQrBIfL1qlXlhI5eZivjuMbbt9T3OiEVCsEgIFgnBIrG728zCApWhSpih917cP/O22p6ZF9+/92LJpYxYJASLhGCRECwS36+8L5yBzjg1IZ250cx9t31bsIERi4RgkRAsEoJF4snkvWvk0s1Au+rybXP57jGK8iQjFgnBIiFYJASLxPdlMzO9WbbVq3SbMBdOk4cs7BgzU+qz5AMasUgIFgnBIiFYJNZvWO32ZL5kH+nQpU59wCHFtyNGLBKCRUKwSAgWiY8m79uqaO5tq8B5SXX5qRtdPLuvEYuEYJEQLBKCReL7splttef3uqNNZ6ar2+byXdv3mQ/44aWMWCQEi4RgkRAsEk9q3rv+jl2/9aHH6J5q5lIzP3VIE38IwSIhWCQEi8TuQ5q2LR93RzgN3WjGqa4++rzzXoJFQrBICBaJBa0i79/7kl2XC698b1tj96EXdz/9FSMWCcEiIVgkBIvE+j7v25rAnKrA2daxsvvfmKHbDCcJFgnBIiFYJBZ0m7m3bbPrS7o/vrPr5P2Nhpi8c5JgkRAsEoJF4vsNq/dmpskz6+PdhtUZLzmUalttj7IZThIsEoJFQrBIPGkVeap+Y+ZS3Xmk9zfqGtlfbDsc6kNGLBKCRUKwSAgWiQXdZk7tq7zojmHqbjTkJX8z3d/3JyMWCcEiIVgkBIvEgkOauhXhGd3O2BnbFtOHHuPiWZ3MhRGLhGCRECwSgkXiySFN92ZqTi62HQ41ZFtx/ba/MPR557chWCQEi4RgkXhXn/eXVNEstG2TrT7v/C8IFgnBIiFYJD6avHebMO9ffO/UMUxDttWed57N5Y1YJASLhGCRECwST1pFDtlW5d21X+++AJjZW3CqNeaHjFgkBIuEYJEQLBJPVt7/44pBDcby9168s+37tqNcZ1h5ZyvBIiFYJASLxIJWkQt1q9hdIdDCx7i/1MxTDV1Zn3feS7BICBYJwSLxUavIzlBrmoVFNd3XA0OPMfPemcNaZ658/96fjFgkBIuEYJEQLBIf1bxvqyqZeYyFE/Btjd2HTnYdcrzSyYhFQrBICBYJwSLxZMPqtnKObX80LNxV2/W1H/oIQ4o1fSMWCcEiIVgkBItE3m2ms3DZ+lSf965j/v2NFtYj/YoRi4RgkRAsEoJF4tWT964p/KmDT7uTXRduo11SRWPEIiFYJASLhGCReDJ57xrUdPPxhdUs915yKFW3t+BDRiwSgkVCsEgIFomPJu+/RYfxbUXfp45j7favFg3ljVgkBIuEYJEQLBLv6vPOH8OIRUKwSAgWCcEiIVgkBIuEYJH4F9M4+lvMH+kAAAAAAElFTkSuQmCC')
filename = 'lev9.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(imgdata)