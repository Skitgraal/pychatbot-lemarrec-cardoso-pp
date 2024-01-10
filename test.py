mot = "PaAUD"
mot_lowered = ""
for lettre in mot:
    if 64 < ord(lettre) < 91:
        mot_lowered += chr(ord(lettre) + 32)
    else:
        mot_lowered += lettre
print(mot_lowered)
def convert_lower(speeches_dir, cleaned_dir, filenames):
    for file in filenames:
        to_convert = speeches_dir + "/" + file
        lowered = cleaned_dir + "/" + file.split()[0] + "-lowered.txt"
        with open(to_convert, "r") as f, open(lowered, "w") as f2 :
            return None
def del_ponctuation(speeches_dir,cleaned_dir ):
    for filename in os.listdir(speeches_dir):
        with open(speeches_dir + '/' + filename, "r") as f1, open(cleaned_dir + '/' + filename + '2', "x") as f2:
            for ponc in f1.read() :
                if ord(ponc)>32 and ord(ponc)<48:
                    ponc =  " "
                f2.write(ponc)
def IDF(cleaned_dir,n):
    n=0
    for word in files:
        n=n+1
        o= word.keys()
        inverse= math.log(n/o)

