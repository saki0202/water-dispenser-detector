import os
import xml.etree.ElementTree as ET

xml_dir = r"C:\Users\sakis\2025_CV\water-dispenser-detector\data\final_positive"
output_file = os.path.join(xml_dir, "info.lst")

lines = []

for fname in os.listdir(xml_dir):
    if fname.endswith(".xml"):
        xml_path = os.path.join(xml_dir, fname)
        tree = ET.parse(xml_path)
        root = tree.getroot()

        image_file = root.find("filename").text
        img_path = os.path.join("data/final_positive", image_file)

        for obj in root.findall("object"):
            bndbox = obj.find("bndbox")
            xmin = int(bndbox.find("xmin").text)
            ymin = int(bndbox.find("ymin").text)
            xmax = int(bndbox.find("xmax").text)
            ymax = int(bndbox.find("ymax").text)
            w = xmax - xmin
            h = ymax - ymin

            line = f"{img_path} 1 {xmin} {ymin} {w} {h}"
            lines.append(line)

with open(output_file, "w") as f:
    f.write("\n".join(lines))

print("✅ info.lst generated!")
