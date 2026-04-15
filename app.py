from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hesap-makinesi', methods=['GET', 'POST'])
def hesap_makinesi():
    sonuc = None
    if request.method == 'POST':
        try:
            s1, s2 = float(request.form['s1']), float(request.form['s2'])
            islem = request.form['islem']
            if islem == 'topla': sonuc = s1 + s2
            elif islem == 'cikar': sonuc = s1 - s2
            elif islem == 'carp': sonuc = s1 * s2
            elif islem == 'bol': sonuc = s1 / s2 if s2 != 0 else "Hata"
        except: sonuc = "Hata"
    return render_template('hesap_makinesi.html', sonuc=sonuc)

@app.route('/vki', methods=['GET', 'POST'])
def vki():
    sonuc, durum = None, ""
    if request.method == 'POST':
        try:
            boy, kilo = float(request.form['boy'])/100, float(request.form['kilo'])
            cinsiyet, bel = request.form['cinsiyet'], float(request.form['bel'])
            v = round(kilo / (boy * boy), 1)
            sonuc = f"VKİ: {v}"
            if v < 18.5: durum = "Zayıf"
            elif v < 25: durum = "Normal"
            else: durum = "Kilolu"
            if (cinsiyet == 'Kadin' and bel > 88) or (cinsiyet == 'Erkek' and bel > 102):
                durum += " (Riskli Bel Çevresi!)"
        except: sonuc = "Hata"
    return render_template('vki.html', sonuc=sonuc, durum=durum)

@app.route('/alan', methods=['GET', 'POST'])
def alan():
    sonuc = None
    if request.method == 'POST':
        try:
            sekil = request.form['sekil']
            v1, v2 = float(request.form['v1']), float(request.form.get('v2', 0))
            if sekil == 'ucgen': sonuc = (v1 * v2) / 2
            elif sekil == 'cokgen': # v1=kenar sayısı, v2=kenar uzunluğu
                sonuc = round((v1 * v2**2) / (4 * math.tan(math.pi / v1)), 2)
        except: sonuc = "Hata"
    return render_template('alan.html', sonuc=sonuc)

if __name__ == '__main__':
    app.run(debug=True)