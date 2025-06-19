import os
import glob
import xml.etree.ElementTree as ET

input_dir = "data/positive"
output_file = "info.dat"

with open(output_file, "w") as out:
    for xml_file in glob.glob(os.path.join(input_dir, "*.xml")):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        image_file = root.find("filename").text
        for obj in root.iter("object"):
            bbox = obj.find("bndbox")
            xmin = int(bbox.find("xmin").text)
            ymin = int(bbox.find("ymin").text)
            xmax = int(bbox.find("xmax").text)
            ymax = int(bbox.find("ymax").text)
            width = xmax - xmin
            height = ymax - ymin
            out.write(f"{input_dir}/{image_file} 1 {xmin} {ymin} {width} {height}\n")
