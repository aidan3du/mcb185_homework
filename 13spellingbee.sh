#By Kenta and Aidan
cd ~/Code/MCB185/data
gunzip -c /Users/aidandu/Code/MCB185/data/dictionary.gz | grep "r" | grep -v -E "[bdefghjklmpqstuvwxy]+" | grep -E ".{4}"
