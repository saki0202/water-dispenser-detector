import os
import xml.etree.ElementTree as ET

xml_dir = r'C:\Users\sakis\2025_CV\water-dispenser-detector\data\new_positive'
output_file = os.path.join(xml_dir, 'info.lst')

lines = []

for fname in os.listdir(xml_dir):
    if fname.endswith('.xml'):
        tree = ET.parse(os.path.join(xml_dir, fname))
        root = tree.getroot()

        filename = root.find('filename').text
        path = os.path.join('data/positive_resized', filename)
        objs = root.findall('object')
        for obj in objs:
            bndbox = obj.find('bndbox')
            xmin = int(bndbox.find('xmin').text)
            ymin = int(bndbox.find('ymin').text)
            xmax = int(bndbox.find('xmax').text)
            ymax = int(bndbox.find('ymax').text)
            w = xmax - xmin
            h = ymax - ymin
            line = f"{path} 1 {xmin} {ymin} {w} {h}"
            lines.append(line)

with open(output_file, 'w') as f:
    f.write('\n'.join(lines))

print("info.lst saved.")
