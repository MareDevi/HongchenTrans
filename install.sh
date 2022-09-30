echo "1. ArchLinux based distributions
2. Debain based distributions"

echo -n "Please select your linux distribution > "
read text

if [ "$text" = "1" ]; then
  pip install -r requirements.txt
  sudo pacman -S tesseract
  sudo wget -P /usr/share/tessdata/ https://ghproxy.net/https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main/eng.traineddata
  sudo wget -P /usr/share/tessdata/ https://ghproxy.net/https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main/chi_sim.traineddata
elif [ "$text" = "2" ]; then
  pip install -r requirements.txt
  sudo apt-get install tesseract-ocr
  sudo wget -P /usr/local/share/tessdata/ https://ghproxy.net/https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main/eng.traineddata
  sudo wget -P /usr/local/share/tessdata/ https://ghproxy.net/https://raw.githubusercontent.com/tesseract-ocr/tessdata_fast/main/chi_sim.traineddata
fi