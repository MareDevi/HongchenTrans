pip install -r requirements.txt
sudo pacman -S tesseract
sudo wget -P /usr/share/tessdata/ https://ghproxy.net/https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main/eng.traineddata
sudo wget -P /usr/share/tessdata/ https://ghproxy.net/https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main/chi_sim.traineddata